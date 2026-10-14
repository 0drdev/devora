"""Fábrica FastAPI: composición modular, sin estado persistente."""
from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.routes_api import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(title="Devora — Conversor efímero a Markdown", version="0.1.0")
    app.include_router(api_router)
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        with open("templates/index.html", encoding="utf-8") as fh:
            return fh.read()

    return app


app = create_app()
