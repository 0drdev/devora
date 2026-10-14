"""Rutas API: conversión efímera (nada se retiene en el servidor)."""
from __future__ import annotations

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

from app.modules.conversion.adapter import convert_bytes
from app.modules.ingestion import guards
from app.modules.ingestion.formats import ValidationError, validate_upload
from app.modules.privacy.logging import log_conversion
from app.modules.privacy.sanitize import download_name, safe_filename

router = APIRouter()


@router.post("/api/convert")
async def convert(file: UploadFile = File(...)):
    name = safe_filename(file.filename or "documento")
    try:
        data = await file.read()
        validate_upload(name, len(data))
        guards.check_bytes(data, name)
        result = convert_bytes(data, name)
    except ValidationError as exc:
        log_conversion(name, len(data), False)
        return JSONResponse(status_code=400, content={"error": exc.message})
    except RuntimeError as exc:
        log_conversion(name, len(data), False)
        return JSONResponse(status_code=503, content={"error": str(exc)})
    except Exception:  # noqa: BLE001 - mensaje genérico en español
        log_conversion(name, len(data), False)
        return JSONResponse(
            status_code=422,
            content={"error": "No se pudo convertir el documento. Prueba con otro archivo."},
        )
    log_conversion(name, len(data), True)
    return {
        "filename": name,
        "markdown": result.markdown,
        "warnings": result.warnings,
        "download_name": download_name(name),
    }
