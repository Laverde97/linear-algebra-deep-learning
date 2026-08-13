# Teaching guide — non-technical audience

## Teaching principle

Do not begin with symbols. Start with familiar data and ask what a computer must do to process it. Follow this sequence:

**real object → numbers → shape → operation → meaning in AI**.

## 2.1 Scalars, vectors, matrices, and tensors

Opening line: **“For a computer, almost everything is eventually converted into numbers.”**

Use age as a scalar, one person's data as a vector, a table of people as a matrix, and a collection of images as a tensor. With MNIST, emphasize that we see a digit while the computer sees a matrix of intensities. Explain tokenization with IMDB and color channels with an RGB image. Ask what `32` means in `(32, 224, 224, 3)`: the batch size.

## 2.2 Multiplication

Opening line: **“A neuron combines information by multiplying inputs by weights.”** Start with three features and three weights; then show how a matrix processes many examples at once. Connect this to MNIST: 784 pixels and 10 outputs.

## 2.3 Identity and inverse

The identity changes nothing; an inverse attempts to undo a transformation. Do not present matrix inversion as the recommended numerical method—show `solve` in NumPy.

## 2.4 Dependence and span

If one variable is twice another, it adds no new direction of information. Draw a line for one direction and a plane for two independent directions.

## 2.5 Norms

Opening line: **“We need a rule for saying how large or how different something is.”** Compare two MNIST images using L1 and L2, then connect norms to distance and regularization.

## 2.6 Special matrices

Keep the essentials: diagonal means simple scaling; symmetric appears in covariance; orthogonal means normalized perpendicular directions; one-hot represents a category by position.

## 2.7 Eigendecomposition

Avoid a long derivation. Explain that certain directions do not rotate under a transformation. In a point cloud, these directions reveal natural axes of variation.

## 2.8 SVD

Make this visual. Reconstruct an MNIST image with `k=1,3,5,10,20` and ask when it becomes recognizable. The message: a matrix can be approximated using its most important components.

## 2.9 Pseudoinverse

Use noisy linear regression. When no perfect solution exists, the pseudoinverse finds one that minimizes squared error.

## 2.10 Trace

Define it briefly as the sum of the diagonal and show its relationship to the Frobenius norm. It is compact notation often used in derivations.

## 2.11 Determinant

Use geometry: a square becomes a parallelogram. The determinant's absolute value tells how area changes; zero means the area collapses and the transformation loses a dimension.

## 2.12 PCA

Close with MNIST. Reduce 784 dimensions to 2 for visualization and to 20 for reconstruction. Connect compact representations to embeddings while clarifying that PCA is linear and much simpler than a deep network.

## Closing question

Ask: “What do a movie review, an image, and a table of people have in common?” Expected answer: **all can be converted into tensors and processed with linear algebra operations**.
