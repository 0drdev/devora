from app.modules.fidelity.checks import analyze, strip_data_images


def test_conserva_estructura_sin_advertencias():
    md = "# Título\n\n- uno\n- dos\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n[ir](https://x.example)\n\n![alt](img)"
    assert analyze(md, ".docx") == []


def test_imagen_sin_alt_avisa():
    assert analyze("![](img)\n", ".pdf")


def test_vacio_avisa_sin_perdida_silenciosa():
    assert analyze("   \n", ".pptx") == ["No se pudo extraer texto del documento."]


def test_pdf_escaneado_orienta_sobre_ocr():
    (warnings,) = analyze("   \n", ".pdf")
    assert "escaneado" in warnings and "OCR" in warnings


def test_base64_se_reemplaza_por_marcador():
    md = "texto\n\n![](data:image/png;base64,iVBOR...)\n\nmás"
    clean, n = strip_data_images(md)
    assert n == 1
    assert "data:image" not in clean
    assert "imagen-1.png" in clean
    assert "más" in clean
