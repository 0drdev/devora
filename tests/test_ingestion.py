import pytest

from app.modules.ingestion.formats import SUPPORTED_FORMATS, ValidationError, validate_upload


def test_matriz_acepta_formatos_clave():
    for ext in [".pdf", ".docx", ".pptx", ".xlsx", ".png", ".mp3", ".zip"]:
        assert validate_upload(f"doc{ext}", 100) == ext


def test_tipo_no_soportado_lista_formatos():
    with pytest.raises(ValidationError) as exc:
        validate_upload("app.exe", 100)
    assert ".pdf" in str(exc.value.message)


def test_sobredimensionado_en_espanol():
    with pytest.raises(ValidationError) as exc:
        validate_upload("doc.pdf", 26 * 1024 * 1024)
    assert "límite" in str(exc.value.message)
    assert len(SUPPORTED_FORMATS) >= 15
