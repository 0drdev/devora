from app.modules.privacy.sanitize import download_name, safe_filename, temp_dir


def test_path_traversal_neutralizado():
    assert "/" not in safe_filename("../../etc/passwd")
    assert "\\" not in safe_filename("..\\secret\\x.pdf")


def test_download_name_derivado():
    assert download_name("informe anual.DOCX") == "informe_anual.md"


def test_temp_aislado_fuera_del_repo(tmp_path):
    d = temp_dir()
    try:
        assert d.exists() and str(d) not in str(tmp_path)
    finally:
        import shutil
        shutil.rmtree(d, ignore_errors=True)
