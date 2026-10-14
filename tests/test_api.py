import sys
import types

from fastapi.testclient import TestClient

from app.main import create_app


class _FakeResult:
    markdown = "# Hola"


class _FakeMD:
    def __init__(self, *a, **k):
        pass

    def convert_stream(self, stream, file_extension=None):
        return _FakeResult()


def _cliente(monkeypatch):
    mod = types.ModuleType("markitdown")
    mod.MarkItDown = _FakeMD
    monkeypatch.setitem(sys.modules, "markitdown", mod)
    return TestClient(create_app())


def test_convert_ok_con_download_name(monkeypatch):
    client = _cliente(monkeypatch)
    r = client.post("/api/convert", files={"file": ("informe.docx", b"x", "application/octet-stream")})
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["markdown"] == "# Hola"
    assert body["download_name"] == "informe.md"
    assert body["warnings"] == []


def test_convert_rechaza_tipo(monkeypatch):
    client = _cliente(monkeypatch)
    r = client.post("/api/convert", files={"file": ("app.exe", b"x", "application/octet-stream")})
    assert r.status_code == 400
    assert "soportado" in r.json()["error"]
