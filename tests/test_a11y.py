"""Accesibilidad estática verificable sin navegador."""
import re
from pathlib import Path

HTML = Path("templates/index.html").read_text(encoding="utf-8")
CSS = Path("static/app.css").read_text(encoding="utf-8")
JS = Path("static/app.js").read_text(encoding="utf-8")


def test_html_semantico_y_foco():
    assert "<main" in HTML and "<h1" in HTML
    assert 'for="file"' in HTML
    assert ":focus-visible" in CSS or "focus-visible" in CSS
    assert 'tabindex="' not in HTML or 'tabindex="-1"' in HTML


def test_live_regions_para_estado():
    assert HTML.count('aria-live="polite"') >= 2
    assert 'role="status"' in HTML


def test_acciones_accesibles_con_confirmacion():
    for bid in ["copiar", "descargar", "descartar"]:
        assert f'id="{bid}"' in HTML
    assert "clipboard.writeText" in JS
    assert "confirm.textContent" in JS


def test_movimiento_reducido_y_responsive():
    assert "prefers-reduced-motion" in CSS
    assert 'name="viewport"' in HTML


def test_errores_en_espanol_sin_tecnicalidades():
    from app.modules.ingestion.formats import ValidationError
    from app.modules.ingestion.guards import check_bytes

    try:
        check_bytes(b"", "a.pdf")
    except ValidationError as exc:
        assert "Traceback" not in exc.message
        assert re.search(r"[áéíóúñ]", exc.message)
