import io
import sys
import types

import pytest

from app.modules.conversion import adapter


class _FakeResult:
    markdown = "# hola"


class _FakeMD:
    instance = None

    def __init__(self, *args, **kwargs):
        _FakeMD.instance = (args, kwargs)
        self.calls = []

    def convert_stream(self, stream, file_extension=None):
        self.calls.append(("convert_stream", file_extension, stream.read()))
        return _FakeResult()

    def convert(self, *args, **kwargs):  # pragma: no cover
        raise AssertionError("no debe usarse convert() genérico")


def _instalar_fake(monkeypatch):
    mod = types.ModuleType("markitdown")
    mod.MarkItDown = _FakeMD
    monkeypatch.setitem(sys.modules, "markitdown", mod)


def test_usa_convert_stream_sin_plugins(monkeypatch):
    _instalar_fake(monkeypatch)
    res = adapter.convert_bytes(b"[x](https://example.com)", "doc.md")
    assert res.markdown == "# hola"
    args, kwargs = _FakeMD.instance
    assert kwargs.get("enable_plugins") is False


def test_enlaces_no_disparan_descargas(monkeypatch):
    _instalar_fake(monkeypatch)
    inst = _FakeMD()
    monkeypatch.setattr("markitdown.MarkItDown", lambda *a, **k: inst)
    adapter.convert_bytes(b"[x](https://example.com/y.pdf)", "doc.md")
    assert inst.calls and inst.calls[0][0] == "convert_stream"
    assert all("https://" not in str(c[1]) for c in inst.calls)


def test_sin_markitdown_mensaje_claro(monkeypatch):
    monkeypatch.delitem(sys.modules, "markitdown", raising=False)
    import builtins
    real_import = builtins.__import__

    def falso(name, *args, **kwargs):
        if name == "markitdown":
            raise ImportError("nope")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", falso)
    with pytest.raises(RuntimeError, match="Python >= 3.10"):
        adapter.convert_bytes(b"hola", "a.txt")
