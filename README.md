# Linear Algebra for Deep Learning / Álgebra lineal para Deep Learning

Workshop materials are available in both English and Spanish. Choose a language:

| Language / Idioma | Slides / Diapositivas | Exercises / Ejercicios | Guide / Guía |
|---|---|---|---|
| English | [Open slides](https://laverde97.github.io/linear-algebra-deep-learning/en/slides/) | [Open exercises](en/exercises/) | [English README](en/README.md) |
| Español | [Abrir diapositivas](https://laverde97.github.io/linear-algebra-deep-learning/es/slides/) | [Abrir ejercicios](es/exercises/) | [README en español](es/README.md) |

## Repository structure / Estructura

```text
.
├── en/
│   ├── slides/
│   ├── exercises/
│   └── README.md
├── es/
│   ├── slides/
│   ├── exercises/
│   └── README.md
├── shared/          # images, styles, code, and common resources
└── README.md
```

The Quarto site publishes a bilingual landing page and both slide decks. Shared assets live in `shared/` to avoid duplication.

El sitio de Quarto publica una portada bilingüe y ambas presentaciones. Los recursos comunes están en `shared/` para evitar duplicados.

## Local preview / Vista previa local

```bash
quarto preview
```

The notebooks can be opened directly from each language guide or run locally with the dependencies in `shared/requirements.txt`.

Los notebooks se pueden abrir desde la guía de cada idioma o ejecutar localmente con las dependencias de `shared/requirements.txt`.
