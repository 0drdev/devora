"""Auditoría: el código y manifiestos no deben traer persistencia."""
from pathlib import Path

PROHIBIDO = [
    "sqlite", "postgres", "psycopg", "sqlalchemy", "DATABASE_URL",
    "boto3", "azure-storage-blob", "volumes:",
]

RAICES = ["app", "templates", "static"]
MANIFIESTOS = ["Dockerfile", "render.yaml", "docker-compose.yml"]


def test_sin_persistencia():
    archivos = []
    for raiz in RAICES:
        p = Path(raiz)
        if p.exists():
            archivos += [f for f in p.rglob("*") if f.is_file()]
    archivos += [Path(m) for m in MANIFIESTOS if Path(m).exists()]
    hallazgos = []
    for f in archivos:
        try:
            texto = f.read_text(encoding="utf-8").lower()
        except (UnicodeDecodeError, OSError):
            continue
        for token in PROHIBIDO:
            if token.lower() in texto:
                hallazgos.append(f"{f}:{token}")
    assert hallazgos == []
