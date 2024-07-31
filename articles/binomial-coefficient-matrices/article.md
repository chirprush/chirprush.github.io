## Main Idea


**Idea.** Consider \( (n + 1) \times (n + 1) \) matrices of the form \( A_{ij} = \binom{i - 1}{j - 1} \), with the convention that \( \binom{i}{j} = 0 \) for \( j > i \). Denote these matrices by \( B_n \). What kind of properties do these matrices (and perhaps similar ones) have?


**Example.** The first few such matrices are
\[
    B_0 = \begin{bmatrix}
        1
    \end{bmatrix},
    B_1 = \begin{bmatrix}
        1 & 0 \\
        1 & 1
    \end{bmatrix},
    B_2 = \begin{bmatrix}
        1 & 0 & 0 \\
        1 & 1 & 0 \\
        1 & 2 & 1
    \end{bmatrix},
    B_3 = \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        1 & 1 & 0 & 0 \\
        1 & 2 & 1 & 0 \\
        1 & 3 & 3 & 1
    \end{bmatrix}
.\]


## Exploration

Immediately we can see that by definition such matrices are lower unitriangular, as for any such matrix \( A \), \( A_{ij} = 0 \) for \( j > i \) and \( A_{ii} = \binom{i - 1}{i - 1} = 1 \). This is also obvious from the examples.

With this structure comes a few properties:

- \( \det B_n = 1 \).
- \( \det (B_n - \lambda I) = (\lambda - 1)^{n + 1} \).
- \( B_n \) is not diagonalizable.

### Evaluating A Tranpose Product

**Question.** What is \( B_n B_n^T \)?

Using Mathematica, we can gain the intuition that the answer should be \( (B_n B_n^T)_{ij} = \binom{i + j - 2}{i - 1} = \binom{i + j - 2}{j - 1} \). We can prove this is true by observing that
\[
\begin{align*}
    (B_n B_n^T)_{ij} &= \sum_{k = 0}^{n} (B_n)_{ik} (B_n^T)_{kj} \\
    &= \sum_{k = 1}^{n} \binom{i - 1}{k - 1} \binom{j - 1}{k - 1} \\
    &= \sum_{k = 0}^{\min(i - 1, j - 1)} \binom{i - 1}{k} \binom{j - 1}{j - 1 - k}.
\end{align*}
\]
If we WLOG let \( i \ge j \), then Vandermonde's identity tells us that \( (B_n B_n^T)_{ij} \) indeed is \( \binom{i + j - 2}{j - 1}  \).

### Evaluating The Inverse

**Question.** What is the inverse of \( B_n \)?

Since \( B_n \) is unitriangular, it's very easy to work out some small examples, so let us do so. For \( B_3 \), we have
\[
\begin{align*}
    \begin{bmatrix}
        1 & 0 & 0 & 0 & \bigm| & b_1 \\
        1 & 1 & 0 & 0 & \bigm| & b_2 \\
        1 & 2 & 1 & 0 & \bigm| & b_3 \\
        1 & 3 & 3 & 1 & \bigm| & b_4
    \end{bmatrix} &\longrightarrow
    \begin{bmatrix}
        1 & 0 & 0 & 0 & \bigm| & b_1 \\
        0 & 1 & 0 & 0 & \bigm| & b_2 - b_1 \\
        1 & 2 & 1 & 0 & \bigm| & b_3 \\
        1 & 3 & 3 & 1 & \bigm| & b_4
    \end{bmatrix} \\
    &\longrightarrow 
    \begin{bmatrix}
        1 & 0 & 0 & 0 & \bigm| & b_1 \\
        0 & 1 & 0 & 0 & \bigm| & b_2 - b_1 \\
        0 & 0 & 1 & 0 & \bigm| & b_3 - 2b_2 + b_1 \\
        1 & 3 & 3 & 1 & \bigm| & b_4
    \end{bmatrix} \\
    &\longrightarrow 
    \begin{bmatrix}
        1 & 0 & 0 & 0 & \bigm| & b_1 \\
        0 & 1 & 0 & 0 & \bigm| & b_2 - b_1 \\
        0 & 0 & 1 & 0 & \bigm| & b_3 - 2b_2 + b_1 \\
        0 & 0 & 0 & 1 & \bigm| & b_4 - 3b_3 + 3b_2 - b_1
    \end{bmatrix},
\end{align*}
\]
which I suppose is somewhat obvious. This tells us that
\[
    B_3^{-1} = \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        -1 & 1 & 0 & 0 \\
        1 & -2 & 1 & 0 \\
        -1 & 3 & -3 & 1
    \end{bmatrix}
,\]
which allows one to guess that \( (B_n^{-1})_{ij} = (-1)^{i + j} (B_n)_{ij} = (-1)^{i + j} \binom{i - 1}{j - 1} \). Let's try and prove this. We have that
\[
    (B_n B_n^{-1})_{ij} = \delta_{ij}
,\]
so we must have that (credits to this [aops thread](https://artofproblemsolving.com/community/c7h1973655p13689198) for the idea)
\[
\begin{align*}
    (B_n B_n^{-1})_{ij} &= \sum_{k = 1}^{n+1} (B_n)_{ik} (B_n^{-1})_{kj} \\
    &= \sum_{k = 1}^{n + 1} (-1)^{k + j} \binom{i - 1}{k - 1} \binom{k - 1}{j - 1} \\
    &= \sum_{k = 0}^{n} (-1)^{k + 1 + j} \binom{i - 1}{k} \binom{k}{j - 1}  \\
    &= \binom{i - 1}{j - 1} (-1)^{1 + j} \sum_{k = 0}^{n} (-1)^k \binom{i - 1 - (j - 1)}{k - (j - 1)}.
\end{align*}
\]
For \( j > i \), this is trivially \( 0 \), so we'll assume from now on that \( j \le i \).
\[
\begin{align*}
    (B_n B_n^{-1})_{ij}  &= \binom{i - 1}{j - 1} (-1)^{1 + j} \sum_{k = j - 1}^{i - 1} (-1)^k \binom{i - 1 - (j - 1)}{k - (j - 1)} \\
    &= \binom{i - 1}{j - 1} (-1)^{1 + j} \sum_{k = 0}^{i - j} (-1)^{k + j - 1} \binom{i - j}{k} \\
    &= \binom{i - 1}{j - 1} \sum_{k = 0}^{i - j} (-1)^k \binom{i - j}{k} \\
    &= \binom{i - 1}{j - 1} (1 - 1)^{i - j},
\end{align*}
\]
which is \( 0 \) for \( j < i \) and \( 1 \) only for \( j = i \), which is what we wished to show.

## Applications

Knowing the inverse actually allows one to calculate a formula for the number of derangements of \( n \) objects without using the inclusion-exclusion principle, denoted by \( D_n \). In particular, we can show combinatorially that
\[
    \sum_{i = 0}^{k} \binom{k}{i} D_i = k!
,\]
for all \( 0 \le k \le n \). We can turn this into a matrix equation and solve to realize that
\[
    \begin{bmatrix}
        D_0 \\
        D_1 \\
        \vdots \\
        D_{n}
    \end{bmatrix} =
    B_{n}^{-1} \begin{bmatrix}
        0! \\
        1! \\
        \vdots \\
        n!
    \end{bmatrix}
,\]
which shows that
\[
\begin{align*}
    D_n &= \sum_{k = 0}^{n} (-1)^k \binom{n}{n - k} (n-k)! \\
    &= \sum_{k = 0}^{n} (-1)^k \frac{n!}{k!} \\
    &= n! \sum_{k = 0}^{n} \frac{(-1)^k}{k!}.
\end{align*}
\]
