from pathlib import Path


def test_aviso_y_confirmacion_visibles():
    html = Path("templates/index.html").read_text(encoding="utf-8")
    js = Path("static/app.js").read_text(encoding="utf-8")
    assert "Nada se guarda en base de datos" in html
    assert "purgado" in js
