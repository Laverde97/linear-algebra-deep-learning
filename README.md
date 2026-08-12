# Álgebra lineal para Deep Learning — Quarto + Google Colab

🎓 **Presentación interactiva publicada en GitHub Pages**

👉 [Abrir presentación: Álgebra lineal para Deep Learning](https://laverde97.github.io/linear-algebra-deep-learning/)

Proyecto de clase basado en la enumeración del **Capítulo 2: Linear Algebra** de *Deep Learning* (Goodfellow, Bengio y Courville). El contenido de la presentación es una explicación pedagógica propia, orientada a un público inicialmente no técnico, y cada apartado se replica con un laboratorio ejecutable en Google Colab.

## Objetivo

## Objetivo

Construir una clase de aproximadamente **3 horas** que conecte el álgebra lineal con aplicaciones modernas de IA usando:

- datos aleatorios simulados;
- MNIST;
- IMDB Reviews;
- imágenes RGB en formato de entrada ImageNet y práctica opcional con ImageNet-v2;
- NumPy, TensorFlow y PyTorch;
- CPU y GPU en Google Colab.

## Presentación

La fuente es `index.qmd` y se renderiza con **Quarto RevealJS**.

```bash
quarto preview index.qmd
```

## Laboratorios

| Apartado | Tema | Colab |
|---|---|---|
| 00 | Preparación de Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/00_setup_colab.ipynb) |
| 2.1 | Escalares, vectores, matrices y tensores | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/01_scalars_vectors_matrices_tensors.ipynb) |
| 2.2 | Multiplicación de matrices y vectores | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/02_multiplying_matrices_vectors.ipynb) |
| 2.3 | Matrices identidad e inversa | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/03_identity_inverse_matrices.ipynb) |
| 2.4 | Dependencia lineal y span | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/04_linear_dependence_span.ipynb) |
| 2.5 | Normas | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/05_norms.ipynb) |
| 2.6 | Matrices y vectores especiales | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/06_special_matrices_vectors.ipynb) |
| 2.7 | Eigendecomposition | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/07_eigendecomposition.ipynb) |
| 2.8 | SVD | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/08_svd.ipynb) |
| 2.9 | Pseudoinversa Moore–Penrose | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/09_pseudoinverse.ipynb) |
| 2.10 | Operador traza | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/10_trace_operator.ipynb) |
| 2.11 | Determinante | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/11_determinant.ipynb) |
| 2.12 | PCA | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/12_pca.ipynb) |
| Extra | CPU/GPU con NumPy, TensorFlow y PyTorch | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laverde97/linear-algebra-deep-learning-quarto/blob/main/notebooks/13_cpu_gpu_frameworks.ipynb) |

## Publicación en GitHub Pages

El repositorio está preparado para publicarse como:

`https://laverde97.github.io/linear-algebra-deep-learning-quarto/`

Consulta `SETUP_GITHUB.md` para los pasos de creación del repositorio, primer publish y permisos de GitHub Actions.

## Estructura

```text
.
├── index.qmd
├── styles.scss
├── _quarto.yml
├── references.bib
├── requirements.txt
├── SETUP_GITHUB.md
├── notebooks/
│   ├── 00_setup_colab.ipynb
│   ├── 01_scalars_vectors_matrices_tensors.ipynb
│   ├── ...
│   └── 13_cpu_gpu_frameworks.ipynb
└── .github/workflows/publish.yml
```

## Nota sobre ImageNet

Para una clase en vivo no se descarga el ImageNet original. El laboratorio demuestra la estructura tensorial RGB con una imagen compatible con modelos preentrenados en ImageNet. También incluye una celda opcional para **ImageNet-v2**, que conserva el espacio de 1.000 clases de ImageNet2012 pero implica una descarga de alrededor de 1.18 GiB en su configuración estándar.

## Fuentes principales

- *Deep Learning*, Chapter 2 — https://www.deeplearningbook.org/contents/linear_algebra.html
- Quarto RevealJS — https://quarto.org/docs/presentations/revealjs/
- Quarto + GitHub Pages — https://quarto.org/docs/publishing/github-pages.html
- TensorFlow Datasets: MNIST, IMDB Reviews e ImageNet-v2.

## Uso del contenido

Los ejemplos, explicaciones y código de este repositorio son material pedagógico original inspirado en los conceptos del capítulo. No se incluye una reproducción completa ni una traducción íntegra del texto del libro.
