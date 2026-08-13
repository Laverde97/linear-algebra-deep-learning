# Guía docente — grupo no técnico

## Principio pedagógico

No iniciar con símbolos. Iniciar con un dato que el grupo reconoce y preguntar qué necesita hacer el computador para procesarlo. El recorrido recomendado es:

**objeto real → números → forma → operación → significado en IA**.

## 2.1 Escalares, vectores, matrices y tensores

Frase de entrada: **“Para una computadora, casi todo termina convertido en números.”**

Ejemplos: edad = escalar; datos de una persona = vector; base de personas = matriz; conjunto de imágenes = tensor. Con MNIST, insistir en que nosotros vemos un dígito y el computador ve una matriz de intensidades. Con IMDB, mostrar que el texto primero se tokeniza. Con una imagen RGB, explicar que el tercer eje corresponde a canales de color.

Pregunta al grupo: “¿Qué significa el 32 en `(32, 224, 224, 3)`?” Respuesta: el tamaño del batch.

## 2.2 Multiplicación

Frase de entrada: **“Una neurona combina información multiplicando entradas por pesos.”**

Usar primero tres características y tres pesos. Después mostrar que una matriz permite hacer esa misma operación para muchos ejemplos de una sola vez. Finalmente conectar MNIST: 784 píxeles por 10 salidas.

## 2.3 Identidad e inversa

Analogía: la identidad es una operación que no cambia nada; la inversa intenta deshacer una transformación. Evitar presentar la inversión como método recomendado de cálculo: en NumPy mostrar `solve`.

## 2.4 Dependencia y span

Analogía: si una variable es simplemente el doble de otra, no aporta una nueva dirección de información. Dibujar una línea para una dirección y un plano para dos direcciones independientes.

## 2.5 Normas

Frase de entrada: **“Necesitamos una regla para decir qué tan grande o qué tan diferente es algo.”**

Comparar dos imágenes MNIST con L1 y L2. Conectar con similitud, distancias y regularización.

## 2.6 Matrices especiales

Presentar solo lo esencial: diagonal = escalamiento sencillo; simétrica = covarianza; ortogonal = direcciones perpendiculares normalizadas; one-hot = categoría como posición.

## 2.7 Eigendecomposition

Evitar una derivación larga. Explicar que existen direcciones especiales que no cambian de orientación cuando aplicamos una transformación. En una nube de datos, esas direcciones ayudan a descubrir ejes naturales de variación.

## 2.8 SVD

Esta debe ser visual. Mostrar una imagen MNIST reconstruida con `k=1,3,5,10,20`. Preguntar cuándo vuelve a ser reconocible. El mensaje es que una matriz puede aproximarse usando sus componentes más importantes.

## 2.9 Pseudoinversa

Usar regresión lineal con ruido. Explicar que cuando no existe una solución perfecta, la pseudoinversa busca una solución que minimiza el error cuadrático.

## 2.10 Traza

No dedicar demasiado tiempo. Definirla como suma de la diagonal y mostrar su relación con la norma de Frobenius. Presentarla como una notación compacta que aparece en derivaciones.

## 2.11 Determinante

Usar geometría: un cuadrado se transforma en un paralelogramo. El valor absoluto del determinante dice cuánto cambió el área. Si vale cero, el área colapsa y la transformación pierde una dimensión.

## 2.12 PCA

Cerrar el capítulo con MNIST. Pasar de 784 dimensiones a 2 para visualizar y a 20 para reconstruir. Conectar con la idea moderna de representaciones compactas y embeddings, aclarando que PCA es lineal y mucho más simple que una red profunda.

## Cierre

Preguntar: “¿Qué tienen en común una reseña de cine, una imagen y una tabla de personas?” La respuesta esperada: **todos pueden convertirse en tensores y procesarse mediante operaciones de álgebra lineal**.
