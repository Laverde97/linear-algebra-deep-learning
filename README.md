# Linear Algebra for Deep Learning 

Bilingual, hands-on review of the linear algebra behind machine learning, deep learning, and tensors — from scalars to PCA, based on Chapter 2 of *Deep Learning* (Goodfellow, Bengio & Courville).

Revisión bilingüe y práctica del álgebra lineal detrás del machine learning, el deep learning y los tensores — de escalares a PCA, basada en el Capítulo 2 de *Deep Learning* (Goodfellow, Bengio y Courville).

## 🎯 Pre-Workshop Preparation 

**Use these materials before attending the Tensors Workshop.** Each notebook takes roughly 10–15 minutes; working through all 14 takes about 2–3 hours total, and can be split across several sessions. Everything runs in Google Colab — no local install required.

**Usa estos materiales antes de asistir al Taller de Tensores.** Cada notebook toma entre 10 y 15 minutos; completar los 14 toma en total cerca de 2–3 horas, y puede dividirse en varias sesiones. Todo se ejecuta en Google Colab — no necesitas instalar nada localmente.

Recommended order / Orden recomendado:

| # | Topic / Tema |
|---|---|
| 00 | Google Colab setup / Preparación de Google Colab |
| 1 | Scalars, vectors, matrices, and tensors / Escalares, vectores, matrices y tensores |
| 2 | Matrix–vector and matrix–matrix multiplication / Multiplicación de matrices y vectores |
| 3 | Identity and inverse matrices / Matrices identidad e inversa |
| 4 | Linear dependence and span / Dependencia lineal y span |
| 5 | Norms / Normas |
| 6 | Special matrices and vectors / Matrices y vectores especiales |
| 7 | Eigendecomposition / Descomposición en autovalores |
| 8 | Singular Value Decomposition (SVD) / Descomposición en valores singulares |
| 9 | Moore–Penrose pseudoinverse / Pseudoinversa de Moore–Penrose |
| 10 | Trace / Traza |
| 11 | Determinant / Determinante |
| 12 | Principal Component Analysis (PCA) / Análisis de componentes principales |
| Appendix / Apéndice | CPU/GPU frameworks: NumPy, TensorFlow, PyTorch |

## Languages

| | |
|---|---|
| 🇬🇧 **English** | [Slides](https://laverde97.github.io/linear-algebra-deep-learning/en/slides/) · [Exercises](en/exercises/) · [English README](en/README.md) |
| 🇪🇸 **Español** | [Diapositivas](https://laverde97.github.io/linear-algebra-deep-learning/es/slides/) · [Ejercicios](es/exercises/) · [README en español](es/README.md) |

## Slides

- 🇬🇧 [Open the English slides](https://laverde97.github.io/linear-algebra-deep-learning/en/slides/)
- 🇪🇸 [Abrir las diapositivas en español](https://laverde97.github.io/linear-algebra-deep-learning/es/slides/)

## Interactive exercises / notebooks

Every exercise notebook opens directly in Google Colab — no setup needed beyond the [00 setup notebook](en/exercises/00_setup_colab.ipynb). Full tables with per-notebook Colab links live in [`en/README.md`](en/README.md) and [`es/README.md`](es/README.md).

Todos los notebooks se abren directamente en Google Colab — no necesitas más preparación que el [notebook 00 de preparación](es/exercises/00_setup_colab.ipynb). Las tablas completas con enlaces a Colab por notebook están en [`en/README.md`](en/README.md) y [`es/README.md`](es/README.md).

## Recommended topics before the Tensors Workshop 

- Vectors and matrices / Vectores y matrices
- Matrix multiplication / Multiplicación de matrices
- Tensor shapes / Formas (`shape`) de los tensores
- Transpose / Transposición
- Linear dependence / Dependencia lineal
- Norms / Normas
- Eigendecomposition / Descomposición en autovalores
- SVD / Descomposición en valores singulares
- Pseudoinverse / Pseudoinversa
- PCA / Análisis de componentes principales
- Matrix factorizations / Factorizaciones matriciales

## 📐 SVD and Matrix Factorization / SVD y factorización de matrices

**Arriving from a blog post about SVD or matrix factorizations?** This section is for you. SVD and its relatives are core tools for:

- **Dimensionality reduction** — projecting high-dimensional data onto a smaller number of informative directions.
- **Low-rank approximation** — reconstructing a matrix (or image) from its most important components.
- **Compression** — storing an approximate version of a matrix using far fewer numbers.
- **PCA** — a direct application of eigendecomposition/SVD to find directions of maximum variance.
- **Tensor decomposition** — the same low-rank idea generalized beyond matrices to n-dimensional tensors.
- **Machine learning** — from recommender systems to model compression and adaptation techniques (e.g. LoRA-style low-rank updates).

These notebooks build the concepts up in order, each with a runnable Colab lab:

| Concept | English notebook | Notebook en español |
|---|---|---|
| Special matrices & vectors (diagonal, symmetric, orthogonal) | [06 Special matrices](en/exercises/06_special_matrices_vectors.ipynb) | [06 Matrices especiales](es/exercises/06_special_matrices_vectors.ipynb) |
| Eigendecomposition | [07 Eigendecomposition](en/exercises/07_eigendecomposition.ipynb) | [07 Eigendecomposition](es/exercises/07_eigendecomposition.ipynb) |
| **Singular Value Decomposition (SVD)** | [08 SVD](en/exercises/08_svd.ipynb) | [08 SVD](es/exercises/08_svd.ipynb) |
| Moore–Penrose pseudoinverse | [09 Pseudoinverse](en/exercises/09_pseudoinverse.ipynb) | [09 Pseudoinversa](es/exercises/09_pseudoinverse.ipynb) |
| PCA (eigendecomposition/SVD in practice) | [12 PCA](en/exercises/12_pca.ipynb) | [12 PCA](es/exercises/12_pca.ipynb) |

The matching slide sections are in the [English deck](https://laverde97.github.io/linear-algebra-deep-learning/en/slides/#eigendecomposition) and [Spanish deck](https://laverde97.github.io/linear-algebra-deep-learning/es/slides/#descomposición-en-autovalores-eigendecomposition), sections 2.6–2.9 and 2.12.

This repository is meant to **complement**, not duplicate, in-depth blog coverage of SVD and matrix factorizations (such as Ravi Kalia's posts) — use it to build or refresh the linear-algebra prerequisites, then read the deeper material with the notation and intuition already in hand.

Este repositorio busca **complementar**, no duplicar, publicaciones más profundas sobre SVD y factorización de matrices — úsalo para construir o repasar los prerrequisitos de álgebra lineal, y luego lee el material más avanzado con la notación y la intuición ya asimiladas.

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

The Quarto site publishes a bilingual landing page and both slide decks. Shared assets live in [`shared/`](https://github.com/Laverde97/linear-algebra-deep-learning/tree/main/shared) to avoid duplication.

El sitio de Quarto publica una portada bilingüe y ambas presentaciones. Los recursos comunes están en [`shared/`](https://github.com/Laverde97/linear-algebra-deep-learning/tree/main/shared) para evitar duplicados.

## Local preview / Vista previa local

```bash
quarto preview
```

The notebooks can be opened directly from each language guide, run in Google Colab with no installation, or run locally with the dependencies in `shared/requirements.txt`.

Los notebooks se pueden abrir desde la guía de cada idioma, ejecutar en Google Colab sin instalación, o ejecutar localmente con las dependencias de `shared/requirements.txt`.
