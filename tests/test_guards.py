import io
import zipfile

import pytest

from app.modules.ingestion.formats import ValidationError
from app.modules.ingestion.guards import check_bytes


def test_vacio_falla_en_espanol():
    with pytest.raises(ValidationError, match="vacío"):
        check_bytes(b"", "a.pdf")


def test_pdf_protegido_sin_parcial():
    with pytest.raises(ValidationError, match="protegido"):
        check_bytes(b"%PDF /Encrypt resto", "doc.pdf")


def test_zip_danado():
    with pytest.raises(ValidationError, match="dañado"):
        check_bytes(b"no-es-zip", "a.zip")


def test_zip_valido_pasa():
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("hola.txt", "hola")
    check_bytes(buf.getvalue(), "a.zip")
