import time

from app.modules.privacy.store import EphemeralStore


def test_purga_libera_contenido():
    store = EphemeralStore()
    path = store.put("s1")
    path.joinpath("doc.pdf").write_bytes(b"x")
    assert "s1" in store
    assert store.purge("s1") is True
    assert "s1" not in store
    assert not path.exists()


def test_expiracion_automatica():
    store = EphemeralStore()
    store.put("s1")
    n = store.purge_expired(now=time.time() + 16 * 60)
    assert n == 1
    assert "s1" not in store
