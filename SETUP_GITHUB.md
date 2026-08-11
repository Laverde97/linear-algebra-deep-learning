# Publicación en GitHub Pages

Repositorio preparado para: `Laverde97/linear-algebra-deep-learning-quarto`

## 1. Crear el repositorio

En GitHub, crear un repositorio público llamado:

`linear-algebra-deep-learning-quarto`

## 2. Subir el proyecto

```bash
git init
git add .
git commit -m "Initial Quarto linear algebra lecture"
git branch -M main
git remote add origin https://github.com/Laverde97/linear-algebra-deep-learning-quarto.git
git push -u origin main
```

## 3. Habilitar permisos para GitHub Actions

En GitHub:

`Settings > Actions > General > Workflow permissions > Read and write permissions`

## 4. Primera publicación

Con Quarto instalado:

```bash
quarto publish gh-pages
```

A partir de ahí, el workflow `.github/workflows/publish.yml` vuelve a publicar en cada `push` a `main`.

La URL esperada será:

`https://laverde97.github.io/linear-algebra-deep-learning-quarto/`

## 5. Probar localmente

```bash
quarto preview index.qmd
```
