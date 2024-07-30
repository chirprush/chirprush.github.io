## Preface
I'm not quite familiar with many of the high-spec current algorithms that are used to find eigenvalues and eigenvectors with numeric stability, but I suppose they make great use of the characteristic polynomial and other math shenanigans that I probably am not all too familiar with nor sound all too interesting. Thus, it would seem fun to circumvent all that and create a highly scuffed algorithm to locate an eigenvector (potentially multiple?) using geometrical intuition, which seems far more easy to work with.

\[
    \gdef\grad{\operatorname{grad}}
    \gdef\vvec#1{\mathbf{#1}}
\]

## Ideas
Suppose we have a real matrix \( A \) (with non-zero determinant) which we wish to find an eigenvector of. Traditionally, an eigenvector of \( A \) is defined to be any vector \( \vvec{v} \) such that
\[
    A \vvec{v} = \lambda \vvec{v}
,\]
where \( \lambda \) is the corresponding eigenvalue. In geometric terms, the origin, the point described by \( \vvec{v} \), and the image of \( \vvec{v} \) under \( A \) must be collinear. Motivated by this, we can instead characterize an eigenvector of \( A \) differently. Observe that
\[
    \cos{\theta} = \frac{A\vvec{v} \cdot \vvec{v}}{\| A \vvec{v} \| \| \vvec{v} \|}
.\]
Principally, this value is \( -1 \) or \( 1 \) whenever \( \vvec{v} \) is an eigenvector. To simplify this, we shall take
\[
    \cos^2{\theta} = \frac{( A\vvec{v} \cdot \vvec{v} )^2}{\| A \vvec{v} \|^2 \| \vvec{v} \|^2}
\]
as our metric for how "close", \( \vvec{v} \) is to being an eigenvector, with \( 0 \) representing that \( \vvec{v} \) is orthogonal to an (all?) eigenvector and \( 1 \) representing that \( \vvec{v} \) is in fact an eigenvector.

In order to simplify matters slightly, we shall want to take \( \| \vvec{v} \| = 1 \). This would guarantee that each \( \vvec{v} \) that we find such that \( \cos^2{\theta} = 1 \) is part of a different family (I wonder what the right term is for this) of eigenvectors. Since we want to travel around in space however and doing so is cumbersome on a sphere, we will leave the magnitude unfixed for now. Thus, our metric is given by
\[
    \Gamma_A (\vvec{v}) := \frac{(A \vvec{v} \cdot \vvec{v})^2}{\| A \vvec{v} \|^2 \| \vvec{v} \|^2}
,\]
and this is differentiable, meaning it naturally emits a gradient which we shall now hope to derive. Consider the partial derivative taken for some component \( v_k \). Observe that (using shorthand notation for partial derivatives for typing convenience)
\[
    \partial_{v_k} \Gamma_A (\vvec{v}) = \frac{\| A \vvec{v} \|^2 \| \vvec{v} \|^2 \partial_{v_k} (A \vvec{v} \cdot \vvec{v})^2 - (A\vvec{v} \cdot \vvec{v})^2 \partial_{v_k} \| A \vvec{v} \|^2 \| \vvec{v} \|^2}{\| A \vvec{v} \|^4 \| \vvec{v} \|^4}
.\]
So now we must find some expressions for the following
\[
    \partial_{v_k} (A\vvec{v} \cdot \vvec{v})^2, \quad \partial_{v_k} \| A \vvec{v} \|^2 \| \vvec{v} \|^2
.\]
We shall tackle these in parts. We first note that
\[
    A \vvec{v} = \begin{bmatrix} \vvec{u}_1 & \vvec{u}_2 & \cdots & \vvec{u}_n \end{bmatrix} \vvec{v} = \begin{bmatrix} \vvec{w}_1 \\ \vvec{w}_2 \\ \vdots \\ \vvec{w}_n \end{bmatrix} \vvec{v} = \begin{bmatrix}
        \vvec{w}_1 \cdot \vvec{v} \\
        \vvec{w}_2 \cdot \vvec{v} \\
        \vdots \\
        \vvec{w}_n \cdot \vvec{v} \\
    \end{bmatrix} = \begin{bmatrix}
        A_{11} v_1 + A_{12} v_2 + \cdots + A_{1n} v_n \\
        A_{21} v_1 + A_{22} v_2 + \cdots + A_{2n} v_n \\
        \vdots \\
        A_{n1} v_1 + A_{n2} v_2 + \cdots + A_{nn} v_n
    \end{bmatrix}
.\]
By basic rules of derivatives, we have that
\[
\begin{align*}
    \partial_{v_k} (A \vvec{v} \cdot \vvec{v})^2 &= 2 (A \vvec{v} \cdot \vvec{v}) \, \partial_{v_k} (A \vvec{v} \cdot \vvec{v}) \\
    &= 2 (A \vvec{v} \cdot \vvec{v}) (A \vvec{v} \cdot \partial_{v_k} (\vvec{v}) + \partial_{v_k} (A \vvec{v}) \cdot \vvec{v}) \\
    &= 2 (A \vvec{v} \cdot \vvec{v}) (\vvec{w}_k \cdot \vvec{v} + \vvec{u}_k \cdot \vvec{v}) \\
    &= 2 (A \vvec{v} \cdot \vvec{v}) ((\vvec{w}_k + \vvec{u}_k) \cdot \vvec{v})
.\end{align*}
\]
Similarly, for the second expression, we have
\[
\begin{align*}
    \partial_{v_k} \| A \vvec{v} \|^2 \| \vvec{v} \|^2 &= \| A \vvec{v} \|^2 \, \partial_{v_k} \left( \| \vvec{v} \|^2 \right) + \partial_{v_k} \left( \| A \vvec{v} \|^2 \right) \| \vvec{v} \|^2 \\
    &= 2 v_k \| A \vvec{v} \|^2 + \| \vvec{v} \|^2 \sum_{i = 1}^{n} \partial_{v_k} (\vvec{w}_i \cdot \vvec{v})^2 \\
    &= 2 v_k \| A \vvec{v} \|^2 + 2 \| \vvec{v} \|^2 \sum_{i = 1}^{n} (\vvec{w}_i \cdot \vvec{v}) \, \partial_{v_k} (\vvec{w}_i \cdot \vvec{v}) \\
    &= 2 v_k \| A \vvec{v} \|^2 + 2 \| \vvec{v} \|^2 \sum_{i = 1}^{n} A_{ik} \, (\vvec{w}_i \cdot \vvec{v}) \\
    &= 2 v_k \| A \vvec{v} \|^2 + 2 \| \vvec{v} \|^2 (A \vvec{v} \cdot \vvec{u}_k)
.\end{align*}
\]
I've no doubt that these values are terribly inefficient to compute, but it's interesting that the expression isn't entirely intractable.

With the general expression for the partial derivative determined, we can now calculate the gradient as per usual:
\[
    \grad \Gamma_A (\vvec{v}) = \begin{bmatrix}
        \partial_{v_1} \Gamma_A (\vvec{v}) \\
        \partial_{v_2} \Gamma_A (\vvec{v}) \\
        \vdots \\
        \partial_{v_n} \Gamma_A (\vvec{v})
    \end{bmatrix}
.\]
This allows us to define a sequence of converging guesses \( \vvec{g}_1, \vvec{g}_2, \cdots \) where \( \vvec{g}_1 \) is determined by some intial choice and subsequent values in the sequence are determined by the recursion
\[
    \vvec{g}_n = \operatorname{normalize} \bigl(\vvec{g}_{n-1} + \gamma_n \grad \Gamma_A (\vvec{g}_{n-1}) \bigr)
,\]
where \( \gamma_n \) is some sequence that denotes a learning rate for steps of the gradient ascent process. In total, each calculation of \( \grad \Gamma_A (\vvec{g}_n) \) takes \( O(n^2) \) time.

## Results

Actually this works with surpising success. One can probably uniformly distribute points around the unit ball and then run the process, although that is another order of magnitude slower probably.

An interesting exercise would be to determine the convergence rate of this algorithm generally.
