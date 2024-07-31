## Problem

<div class="side-box">
**Problem.** Let \( A(n, k) \) be the number of \( 2 \times n \) matrices such the sum of the entries in each contiguous \( 2 \times k \) submatrix is \( k \).

\vspace{0.3cm}

Determine \( A(10^{16}, 10^8) \) modulo \( 10^9 + 7 \).
</div>

## Solution

A key observation to make for this problem is that one can choose the entries of the first initial \( 2 \times k \) submatrix, and by a sliding window technique, we see that this choice determines the rest of the entire \( 2 \times n \) matrix up to reflections of each row. In particular, knowing the \( i \)th row tells us some very helpful information about all rows of the form \( i + mk \) for integer \( m \):

- If the row is \( (0, 0) \), then so are all the rows.
- If the row is \( (1, 1) \), then again so are all the rows.
- If the row is \( (0, 1) \) or \( (1, 0) \), then all of the aforementioned rows can be either \( (0, 1) \) or \( (1, 0) \).

This motivates one to go casewise on the number of each type of row that appear in the initial chosen submatrix. In particular, we shall index a submatrix by the tuple \( (a_{00}, a_{11}, a_{01}, a_{10}) \). Finding the number of total matrices then amounts to summing over all cases and then determining the number of \( 2 \times n \) matrices with the parameters of the initially chosen \( 2 \times k \) submatrix.

We shall note that for a valid tuple, there are
\[
    \binom{k}{a_{00}, a_{11}, a_{01}, a_{10}}
,\]
initial submatrices, and thus since the submatrix gets copied over \( n/k - 1 \) times, there are
\[
    \binom{k}{a_{00}, a_{11}, a_{01}, a_{10}} 2^{(n/k - 1)(a_{01} + a_{10})}
,\]
full size matrices. This means that our answer should be
\[
    A(n, k) = \sum_{2a_{11} + a_{01} + a_{10} = k} \binom{k}{a_{00}, a_{11}, a_{01}, a_{10}} 2^{(n/k - 1)(a_{01} + a_{10})}
.\]
We shall index instead by \( l = a_{01} + a_{10} \), noting that it must be the same parity as \( k \), which transforms our sum into
\[
\begin{align*}
    A(n, k) &= \sum_{\substack{l = 0, \\ l \equiv_2 k}}^{k} \binom{k}{l} \binom{k - l}{m - l} \sum_{i = 0}^{l} \binom{l}{i} 2^{(n/k - 1)l} \\
    &= \sum_{\substack{l = 0, \\ l \equiv_2 k}}^{k} \binom{k}{l} \binom{k - l}{(k-l)/2} 2^{nl/k} \\
    &= \sum_{\substack{l = 0, \\ l \equiv_2 k}}^{k} \frac{k!}{l! \cdot ((k-l)/2)!^2} 2^{nl/k}.
\end{align*}
\]
Precomputing factorials, powers, and modular inverses, this should be rather quick to compute, running maybe in roughly \( O(k \log{k}) \) time (just eyeballing it).
