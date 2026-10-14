# Flujo git de Devora

## Configuración (una vez por máquina)

```bash
git config --global user.name "0drdev"
git config --global user.email "tu-email@example.com"
```

## Trabajo diario

```bash
git status --short        # revisa qué cambió
git add -A                # prepara todo (respeta .gitignore)
git commit -m "Mensaje claro en español"
git push origin main
```

## Antes de cada cambio grande

```bash
git pull --rebase origin main   # trae lo último sin merges
```

## Ramas (para experimentar sin romper main)

```bash
git checkout -b nombre-rama
# ... trabaja, commit, push ...
git push -u origin nombre-rama
```

## Reglas del repo

- Nunca versionar: venvs (`.venv*/`), `node_modules/`, `__pycache__/`, secretos (`.env`).
- Todo eso ya está en `.gitignore`; si algo así aparece en `git status`, avisa antes de `git add`.
- Commits en español, una idea por commit.

## Arreglos comunes

```bash
git restore --staged <archivo>   # saca un archivo del staged (no lo borra)
git log --oneline -5            # historial corto
git diff                        # qué cambió sin preparar
```
