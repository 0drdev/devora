# Devora — Conversor efímero a Markdown (guía local)

Requisito: Python 3.12 (Markitdown exige >= 3.10; ver `.python-version`).
En esta máquina con Python 3.9 solo corre el esqueleto y los tests que no
requieren Markitdown; la conversión real se verifica en Docker o en el
despliegue gratuito.

## 1. Entorno

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Verificación

```bash
pytest -q
markitdown --version
uvicorn app.main:app --reload
# Abrir http://127.0.0.1:8000/health -> {"status":"ok"}
```

## 3. Docker

```bash
docker build -t conversor-md:local .
docker run --rm -p 8000:8000 conversor-md:local
```

## 3b. Frontend (Tailwind v4)

La UI usa Tailwind compilado (`static/app.css` versionado; Render no
necesita Node). Tras editar `templates/` o `static/input.css`:

```bash
pnpm install
pnpm run build:css
```

## 4. Notas de privacidad

- Sin base de datos ni volúmenes: todo vive en memoria o `tempfile`.
- Los logs solo registran tipo, tamaño y resultado, nunca contenido.
- Plataforma acordada: Render Free (`render.yaml`).
- Límites acordados: 10 MB/archivo, 15 min retención, ZIP 200 MB;
  ajustables con `MAX_UPLOAD_MB`, `RETENTION_MINUTES`, `MAX_ZIP_MB`.
