"""Rebuild the English teaching files from the Spanish source files."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

REPLACEMENTS = {
    "blob/main/es/exercises/": "blob/main/en/exercises/",
    "Álgebra lineal para Deep Learning": "Linear Algebra for Deep Learning",
    "De escalares a PCA · Capítulo 2 + laboratorios reproducibles en Google Colab": "From scalars to PCA · Chapter 2 + reproducible Google Colab labs",
    "La pregunta que guía la clase": "The question that guides the class",
    "¿Cómo convierte una computadora números, imágenes y texto en objetos matemáticos que puede procesar un modelo de IA?": "How does a computer turn numbers, images, and text into mathematical objects that an AI model can process?",
    "Datos reales": "Real-world data", "Números": "Numbers", "Operaciones": "Operations", "Modelo de IA": "AI model",
    "Objetivos de aprendizaje": "Learning objectives", "Al terminar, el grupo podrá:": "By the end, learners will be able to:",
    "Reconocer **escalar, vector, matriz y tensor** a partir de datos reales.": "Identify **scalars, vectors, matrices, and tensors** in real-world data.",
    "Interpretar `shape`, `ndim`, batch y canales.": "Interpret `shape`, `ndim`, batches, and channels.",
    "Entender por qué la multiplicación matricial aparece en redes neuronales.": "Understand why matrix multiplication appears in neural networks.",
    "Explicar de forma intuitiva inversa, rango, normas, autovectores, SVD y PCA.": "Explain inverses, rank, norms, eigenvectors, SVD, and PCA intuitively.",
    "Replicar **cada apartado 2.1–2.12** en Google Colab.": "Reproduce **each section from 2.1–2.12** in Google Colab.",
    "Mover tensores entre **NumPy, TensorFlow y PyTorch**, incluyendo CPU/GPU.": "Move tensors among **NumPy, TensorFlow, and PyTorch**, including CPU/GPU.",
    "Ruta de 3 horas": "Three-hour roadmap", "preguntas, transiciones y una pausa corta": "questions, transitions, and a short break",
    "objetos, productos, inversa, span": "objects, products, inverse, span", "normas, matrices especiales, eigen": "norms, special matrices, eigen",
    "datasets + frameworks": "datasets + frameworks", "Escalares": "Scalars", "Vectores": "Vectors", "Matrices": "Matrices",
    "Un **escalar** es la forma más simple de dato:": "A **scalar** is the simplest form of data:",
    "un único valor numérico o simbólico. Puede": "a single numerical or symbolic value. It can",
    "representar una constante o una variable": "represent a constant or a",
    "univariante.": "univariate variable.", "En aprendizaje automático, normalmente": "In machine learning, we usually",
    "trabajamos con escalares reales:": "work with real-valued scalars:", "Representa un solo valor": "Represents a single value",
    "No tiene dimensiones ni dirección": "It has no dimensions or direction", "Puede ser real o complejo": "It can be real or complex",
    "Aunque parecen simples, los escalares son": "Although they seem simple, scalars are",
    "fundamentales: muchos hiperparámetros de": "fundamental: many model hyperparameters,",
    "un modelo, como la tasa de aprendizaje $\\lambda$, el": "such as learning rate $\\lambda$, the",
    "número de épocas o un umbral, suelen": "number of epochs, or a threshold, are often",
    "expresarse como valores escalares.": "expressed as scalar values.", "Un <span>escalar</span>": "A <span>scalar</span>",
    "un solo valor": "one value", "Cuatro objetos, una misma idea": "Four objects, one idea",
    "Objeto": "Object", "Matriz": "Matrix", "Explicación simple": "Simple explanation", "Ejemplo de datos": "Data example", "Shape típica": "Typical shape",
    "Dimensión / rango del tensor": "Tensor dimension / rank", "un número": "one number", "edad": "age", "lista ordenada": "ordered list",
    "una persona": "one person", "tabla 2D": "2D table", "100 personas × 4 variables": "100 people × 4 variables",
    "arreglo con 3 ejes": "array with 3 axes", "imagen RGB": "RGB image", "arreglo con 4 ejes": "array with 4 axes",
    "lote de imágenes RGB": "batch of RGB images", "arreglo con 5 ejes": "array with 5 axes", "lote de videos": "batch of videos",
    "arreglo con 6 ejes": "array with 6 axes", "lote de secuencias de video": "batch of video sequences",
    "Abrir laboratorio": "Open lab", "Multiplicación de Matrices y Vectores": "Matrix and Vector Multiplication",
    "Matrices identidad e inversa": "Identity and Inverse Matrices", "Dependencia lineal y span": "Linear Dependence and Span",
    "Tipos especiales de matrices y vectores": "Special Types of Matrices and Vectors",
    "Descomposición en autovalores (Eigendecomposition)": "Eigendecomposition",
    "Descomposición en autovalores": "Eigendecomposition", "Descomposición en valores singulares": "Singular Value Decomposition",
    "Pseudoinversa de Moore–Penrose": "Moore–Penrose Pseudoinverse",
    "El Operador Traza (Trace Operator)": "The Trace Operator", "El Operador Traza": "The Trace Operator",
    "Determinante": "Determinant", "Ejemplo: Principal Components Analysis": "Example: Principal Components Analysis",
    "El álgebra no cambia; cambia dónde se ejecuta": "The algebra stays the same; where it runs changes",
    "misma operación": "same operation", "Repositorio y laboratorios": "Repository and labs", "Estructura preparada para GitHub Pages:": "Structure prepared for GitHub Pages:",
    "URL prevista": "Expected URL", "Fuentes y créditos": "Sources and credits", "Contenido pedagógico original basado en los conceptos del capítulo; no reproduce el texto completo del libro.": "Original teaching content based on the chapter concepts; it does not reproduce the full text of the book.",
    "La idea para llevarse": "Key takeaway", "Deep learning trabaja con representaciones. El álgebra lineal nos da el lenguaje para describirlas, transformarlas, medirlas y comprimirlas.": "Deep learning works with representations. Linear algebra gives us the language to describe, transform, measure, and compress them.",
    "Entender": "Understand", "Ejecutar": "Run", "Visualizar": "Visualize", "Conectar con IA": "Connect to AI",
    "**Objetivo:** comprender el concepto, verlo con números y conectarlo con IA/deep learning. Ejecuta las celdas en orden.": "**Goal:** understand the concept, see it with numbers, and connect it to AI/deep learning. Run the cells in order.",
    "Preparación de Google Colab": "Google Colab Setup", "Cómo trabajar": "How to work",
    "Multiplicación de matrices y vectores": "Matrix and vector multiplication", "Producto punto: combinar características": "Dot product: combining features",
    "Producto matriz-vector": "Matrix-vector product", "Producto matriz-matriz: una capa densa": "Matrix-matrix product: a dense layer",
    "Idea clave": "Key idea", "Intuición": "Intuition", "En datos: direcciones principales de variación": "In data: principal directions of variation",
    "Conexión con ML": "Connection to ML", "Conexión con IA": "Connection to AI", "Escalares, vectores, matrices y tensores": "Scalars, vectors, matrices, and tensors",
    "Datos aleatorios simulados": "Simulated random data", "una imagen también es una matriz": "an image is also a matrix",
    "el texto debe convertirse en números": "text must be converted into numbers", "imagen RGB y dimensión batch": "RGB image and batch dimension",
    "Opcional: ImageNet-v2 real": "Optional: real ImageNet-v2", "El mismo tensor en tres ecosistemas": "The same tensor in three ecosystems",
    "Para explicar al grupo": "To explain to the group", "Dependencia lineal y espacio generado": "Linear dependence and span",
    "Dependencia lineal": "Linear dependence", "todas las combinaciones posibles": "all possible combinations", "Redundancia en un dataset simulado": "Redundancy in a simulated dataset",
    "Matriz identidad": "Identity matrix", "Inversa": "Inverse", "Resolver Ax=b": "Solving Ax=b", "¿Qué pasa si no hay inversa?": "What if there is no inverse?",
    "Medir el “tamaño” de un vector": "Measuring the ‘size’ of a vector", "Norma de Frobenius para matrices": "Frobenius norm for matrices",
    "Distancia entre dos imágenes MNIST": "Distance between two MNIST images", "Regularización: intuición": "Regularization: intuition",
    "Matrices y vectores especiales": "Special matrices and vectors", "Diagonal e identidad": "Diagonal and identity",
    "Matriz simétrica": "Symmetric matrix", "Vectores unitarios y ortogonales": "Unit and orthogonal vectors",
    "One-hot: un vector especial muy usado en clasificación": "One-hot: a special vector widely used in classification",
    "Factorizar una matriz": "Factoring a matrix", "Compresión con MNIST": "Compression with MNIST", "Error de reconstrucción": "Reconstruction error",
    "Cuando una inversa normal no aplica": "When a regular inverse does not apply", "Relación con mínimos cuadrados": "Relationship to least squares",
    "Operador traza": "Trace operator", "Traza = suma de la diagonal": "Trace = sum of the diagonal", "Identidad con la norma de Frobenius": "Identity involving the Frobenius norm",
    "Invariancia cíclica": "Cyclic invariance", "como cambio de área/volumen": "as an area/volume change", "cero = colapso de dimensión": "zero = dimensional collapse",
    "comprimir conservando tanta variación como sea posible": "compressing while preserving as much variation as possible",
    "dimensiones": "dimensions", "Reconstrucción con 20 componentes": "Reconstruction with 20 components", "¿Cuántos componentes necesito?": "How many components do I need?",
    "Apéndice · Tensores": "Appendix · Tensors", "mover explícitamente al dispositivo": "move explicitly to the device", "Mensaje de clase": "Class takeaway",
    "No comenzar con fórmulas. Preguntar al grupo: “¿Qué ve una computadora cuando le mostramos una foto?”. Llevarlos a la idea de representación numérica.": "Do not start with formulas. Ask the group, ‘What does a computer see when we show it a photo?’ Guide them toward the idea of numerical representation.",
    "Evitar decir que tensor “siempre significa 3D”.": "Avoid saying that tensor ‘always means 3D’.",
    "En frameworks modernos, tensor es el término general para arreglos n-dimensionales.": "In modern frameworks, tensor is the general term for n-dimensional arrays.",
    "Un escalar puede verse como un tensor de rango 0.": "A scalar can be viewed as a rank-0 tensor.",
    "Explicar la progresión:": "Explain the progression:", "Imagen RGB": "RGB image", "Lote de imágenes": "Batch of images",
    "Abrir laboratorio 2.1 en Colab": "Open lab 2.1 in Colab",
    "1. Abre el notebook con el botón **Open in Colab**.": "1. Open the notebook with the **Open in Colab** button.",
    "2. Ejecuta cada celda con `Shift + Enter`.": "2. Run each cell with `Shift + Enter`.",
    "4. Los laboratorios usan NumPy como base y comparan TensorFlow/PyTorch cuando aporta valor.": "4. The labs use NumPy as a foundation and compare TensorFlow/PyTorch when useful.",
    "vector con 100 elementos": "vector with 100 elements", "matriz: 100 filas × 4 columnas": "matrix: 100 rows × 4 columns",
    "lote de 32 imágenes RGB": "batch of 32 RGB images", "La **forma** (`shape`) será nuestro lenguaje común durante toda la clase.": "**Shape** will be our shared language throughout the class.",
    "Una neurona artificial toma entradas, las multiplica por pesos y suma los resultados.": "An artificial neuron takes inputs, multiplies them by weights, and adds the results.",
    "Muchas observaciones pueden procesarse en una sola operación.": "Many observations can be processed in a single operation.",
    "Si `X` contiene un batch y `W` contiene varios conjuntos de pesos, `X @ W` produce varias salidas por ejemplo.": "If `X` contains a batch and `W` contains several sets of weights, `X @ W` produces several outputs per example.",
    "Con MNIST": "With MNIST",
    "Las redes neuronales parecen complejas, pero una gran parte del cálculo interno se reduce a **multiplicaciones de matrices + funciones no lineales**.": "Neural networks may seem complex, but much of their internal computation reduces to **matrix multiplications + nonlinear functions**.",
    "Es el “1” de las matrices: multiplicar por ella deja el objeto igual.": "It is the ‘1’ of matrices: multiplying by it leaves the object unchanged.",
    "En código numérico es preferible `solve` a calcular la inversa explícitamente.": "In numerical code, `solve` is preferable to computing the inverse explicitly.",
    "Las soluciones cerradas aparecen en regresión lineal y mínimos cuadrados, pero en deep learning a gran escala se prefieren métodos iterativos de optimización.": "Closed-form solutions appear in linear regression and least squares, but large-scale deep learning favors iterative optimization methods.",
    "Un vector es redundante si puede construirse como combinación de otros.": "A vector is redundant if it can be constructed as a combination of others.",
    "Variables redundantes pueden generar multicolinealidad, inestabilidad y cálculos innecesarios. El rango ayuda a saber cuánta información lineal independiente existe.": "Redundant variables can cause multicollinearity, instability, and unnecessary computation. Rank tells us how much independent linear information exists.",
    "L1 tiende a favorecer muchos pesos exactamente pequeños/cero; L2 penaliza pesos grandes de forma suave.": "L1 tends to encourage many weights to be exactly small/zero; L2 penalizes large weights smoothly.",
    "Matrices diagonales simplifican transformaciones, matrices simétricas aparecen en covarianzas y vectores one-hot representan categorías.": "Diagonal matrices simplify transformations, symmetric matrices appear in covariance calculations, and one-hot vectors represent categories.",
    "Un autovector mantiene su dirección bajo una transformación lineal; su autovalor indica cuánto se escala.": "An eigenvector keeps its direction under a linear transformation; its eigenvalue indicates how much it is scaled.",
    "Esta idea es el corazón geométrico de PCA: encontrar direcciones donde los datos varían más.": "This idea is the geometric heart of PCA: finding the directions along which data varies most.",
    "SVD escribe una matriz como `A = U Σ Vᵀ` y funciona también para matrices no cuadradas.": "SVD writes a matrix as `A = U Σ Vᵀ` and also works for non-square matrices.",
    "SVD permite aproximaciones de bajo rango, compresión y análisis de estructura. Conceptos similares aparecen en técnicas modernas de compresión/adaptación de modelos.": "SVD enables low-rank approximations, compression, and structural analysis. Similar concepts appear in modern model compression and adaptation techniques.",
    "La pseudoinversa generaliza la idea a matrices rectangulares o sistemas sin solución exacta única.": "The pseudoinverse generalizes the idea to rectangular matrices or systems without a unique exact solution.",
    "La pseudoinversa produce la solución de mínimos cuadrados en problemas lineales y ayuda a entender qué significa “mejor aproximación” cuando no existe una solución exacta.": "The pseudoinverse produces the least-squares solution to linear problems and clarifies what ‘best approximation’ means when no exact solution exists.",
    "La traza permite escribir expresiones de varianza, covarianza y normas de manera compacta, algo frecuente en derivaciones de optimización y probabilidades.": "The trace expresses variance, covariance, and norms compactly, which is common in optimization and probability derivations.",
    "Determinantes aparecen en cambios de variables, densidades gaussianas y análisis de transformaciones. Un determinante cero revela pérdida de una dimensión.": "Determinants appear in changes of variables, Gaussian densities, and transformation analysis. A zero determinant reveals the loss of a dimension.",
    "PCA muestra el principio de **representación compacta**: reemplazar cientos de variables por un número menor de direcciones informativas. Es una puerta conceptual hacia embeddings y representaciones latentes.": "PCA demonstrates **compact representation**: replacing hundreds of variables with fewer informative directions. It is a conceptual gateway to embeddings and latent representations.",
    "Comparar la misma operación matricial en tres marcos. No buscamos un benchmark científico; buscamos ver **dispositivo, forma y transferencia**.": "Compare the same matrix operation in three frameworks. We are not seeking a scientific benchmark; we want to observe **device, shape, and transfer**.",
    "TensorFlow — el runtime elige CPU/GPU disponible": "TensorFlow — the runtime selects the available CPU/GPU",
    "El álgebra es la misma. Lo que cambia entre frameworks es la API, la gestión de dispositivos, autograd y el ecosistema. Las GPU son especialmente eficientes al ejecutar muchas operaciones tensoriales en paralelo.": "The algebra is the same. What changes across frameworks is the API, device management, autograd, and the ecosystem. GPUs are especially efficient at running many tensor operations in parallel.",
    "Empezamos con información tabular. Un solo valor es un **escalar**, una fila es un **vector**, toda la tabla es una **matriz**.": "We begin with tabular information. A single value is a **scalar**, one row is a **vector**, and the whole table is a **matrix**.",
    "MNIST tiene dígitos manuscritos de 28×28 píxeles. Un píxel es un escalar; una imagen es una matriz; muchas imágenes forman un tensor.": "MNIST contains 28×28-pixel handwritten digits. One pixel is a scalar; one image is a matrix; many images form a tensor.",
    "Las palabras se transforman en identificadores de tokens. Luego las secuencias se igualan a una longitud fija para formar una matriz/tensor.": "Words are transformed into token identifiers. The sequences are then padded to a fixed length to form a matrix/tensor.",
    "En una práctica en vivo no conviene descargar el ImageNet original. Usamos una imagen RGB en el formato que consumen modelos preentrenados en ImageNet. El notebook deja también una celda **opcional** para ImageNet-v2 (descarga grande).": "Downloading the original ImageNet is impractical in a live session. We use an RGB image in the format consumed by ImageNet-pretrained models. The notebook also includes an **optional** ImageNet-v2 cell (large download).",
    "ImageNet-v2 usa el mismo espacio de 1.000 clases que ImageNet2012 y contiene 10.000 imágenes. **Advertencia:** la configuración por defecto ronda 1.18 GiB de descarga, por eso no se ejecuta por defecto en una clase corta.": "ImageNet-v2 uses the same 1,000-class space as ImageNet2012 and contains 10,000 images. **Warning:** the default configuration downloads about 1.18 GiB, so it is not run by default in a short class.",
    "Una operación muy común en deep learning: sumar un vector a cada fila de una matriz sin copiarlo manualmente.": "A common deep learning operation: adding a vector to every row of a matrix without copying it manually.",
    "> La IA no “ve” fotografías, palabras o personas como nosotros. Ve **estructuras numéricas con forma**. El tensor es el contenedor general que permite organizar esas estructuras.": "> AI does not ‘see’ photographs, words, or people as we do. It sees **shaped numerical structures**. A tensor is the general container used to organize those structures.",
    "Escalar": "Scalar", "Lote de videos": "Batch of videos", "Normas": "Norms", "Tensores": "Tensors",
    "2.8–2.12 · SVD, pseudoinversa, traza, determinante, PCA": "2.8–2.12 · SVD, pseudoinverse, trace, determinant, PCA",
    "distribuidos en": "spread across",
    "Regla de lectura de formas": "Shape reading rule",
    "En Colab puedes activar GPU en **Runtime > Change runtime type > T4 GPU**.": "In Colab, you can enable a GPU under **Runtime > Change runtime type > T4 GPU**.",
    "Dependencia lineal y espacio generado (span)": "Linear dependence and span",
    "autovalores y autovectores": "eigenvalues and eigenvectors",
    "Apéndice · Tensores en CPU/GPU: NumPy, TensorFlow y PyTorch": "Appendix · Tensors on CPU/GPU: NumPy, TensorFlow, and PyTorch",
    "Objetivo": "Goal",
    "Si existe `A⁻¹`, entonces `A⁻¹A = I`.": "If `A⁻¹` exists, then `A⁻¹A = I`.",
}


def translate(text: str) -> str:
    for source, target in sorted(REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(source, target)
    return text


# English slides use the translated images under en/images/ instead of the
# Spanish originals under shared/images/. Mapping is explicit (Spanish
# filename -> English filename) and applied only to shared/images/ path
# references, so it cannot affect unrelated text.
IMAGE_PATH_MAP = {
    "SCALAR_VECTOR_MATRIZ_TENSOR.png": "SCALAR_VECTOR_MATRIX_TENSOR.png",
    "Vectores.png": "Vectors.png",
    "Matrices.png": "Matrices.png",
    "Dim_Tensores.png": "Dim_Tensors.png",
    "Broadcasting.png": "Broadcasting.png",
    "Multi_Vect_matri.png": "Multi_Vect_Matrix.png",
    "Identidad_Inversa.png": "Identity_Inverse.png",
    "Dependencia_Lineal.png": "Linear_Dependence.png",
    "Norms.png": "Norms.png",
    "Tipos_Especiales_M_V.png": "Special_Types_M_V.png",
    "Eigendecomposition.png": "Eigendecomposition.png",
    "SVD.png": "SVD.png",
    "Moore_Penrose_Pseudoinverse.png": "Moore_Penrose_Pseudoinverse.png",
    "Trace_Operator.png": "Trace_Operator.png",
    "Determinante.png": "Determinant.png",
    "PCA.png": "PCA.png",
    "Tensor.png": "Tensor.png",
}


def translate_image_paths(text: str) -> str:
    for es_name, en_name in IMAGE_PATH_MAP.items():
        text = text.replace(f"shared/images/{es_name}", f"en/images/{en_name}")
    return text


CODE_REPLACEMENTS = {
    "edades": "ages", "peso": "weight", "altura": "height", "ingresos": "income", "datos": "data",
    "# característica completamente redundante": "# completely redundant feature",
    "Penalización L1:": "L1 penalty:", "Penalización L2²:": "L2² penalty:",
    "Verificación A@x =": "Check A@x =", "No es invertible:": "Not invertible:",
    "Escalar:": "Scalar:", "Vector (una persona):": "Vector (one person):", "Matriz (100 personas):": "Matrix (100 people):",
    "Una imagen:": "One image:", "Escalar (un píxel):": "Scalar (one pixel):", "Vector (una fila):": "Vector (one row):",
    "Matriz (una imagen):": "Matrix (one image):", "Una imagen RGB:": "One RGB image:", "Batch de 1 imagen:": "Batch of 1 image:",
    "Reconstrucción correcta:": "Correct reconstruction:", "Imagen:": "Image:", "valores singulares:": "singular values:",
    "label='datos'": "label='data'", "Regresión lineal vía pseudoinversa": "Linear regression via pseudoinverse",
    "label='dígito'": "label='digit'", "Compresión:": "Compression:",
    "Arriba: original | Abajo: reconstrucción PCA (20 componentes)": "Top: original | Bottom: PCA reconstruction (20 components)",
    "Área escalada por": "Area scaled by", "Autovectores de la matriz de covarianza": "Eigenvectors of the covariance matrix",
    "Pesos:": "Weights:", "label='transformado'": "label='transformed'",
    "Etiqueta:": "Label:", "resultado:": "result:", "Traza:": "Trace:", "Suma diagonal:": "Diagonal sum:",
    "Autovectores (columnas):": "Eigenvectors (columns):", "Autovalores:": "Eigenvalues:", "Covarianza:": "Covariance:",
    "Reducido:": "Reduced:", "Varianza explicada total:": "Total explained variance:", "Varianza explicada:": "Explained variance:",
    "MNIST proyectado a 2 componentes principales": "MNIST projected onto 2 principal components",
    "de varianza → {k} componentes": "of variance → {k} components",
    "n componentes": "n components", "varianza acumulada": "cumulative variance",
    "label='ajuste'": "label='fit'",
    "Combinaciones lineales de dos vectores independientes": "Linear combinations of two independent vectors",
}


def translate_code(text: str) -> str:
    for source, target in CODE_REPLACEMENTS.items():
        text = text.replace(source, target)
    return text


def main() -> None:
    source = ROOT / "es/slides/index.qmd"
    target = ROOT / "en/slides/index.qmd"
    # Image paths are mapped before word translation: several Spanish image
    # filenames (e.g. Vectores.png, Identidad_Inversa.png) share substrings
    # with translated words (Vectores, Inversa), so mapping paths first
    # avoids the word translation corrupting the filename mid-path.
    slides = translate_image_paths(source.read_text(encoding="utf-8"))
    slides = translate(slides)
    target.write_text(slides, encoding="utf-8")

    for source in sorted((ROOT / "es/exercises").glob("*.ipynb")):
        notebook = json.loads(source.read_text(encoding="utf-8"))
        for cell in notebook["cells"]:
            translator = translate if cell["cell_type"] == "markdown" else translate_code
            cell["source"] = [translator(line) for line in cell.get("source", [])]
        target = ROOT / "en/exercises" / source.name
        target.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
