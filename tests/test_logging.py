import logging

from app.modules.privacy.logging import log_conversion


def test_logs_sin_contenido(caplog):
    secreto = "SECRETO-UNICO-123"
    with caplog.at_level(logging.INFO, logger="conversor"):
        log_conversion("doc.pdf", 10, True)
    texto = "\n".join(r.getMessage() for r in caplog.records)
    assert secreto not in texto
    assert "doc.pdf" not in texto
    assert "ext=.pdf" in texto
