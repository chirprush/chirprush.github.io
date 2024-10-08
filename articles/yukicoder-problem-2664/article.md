## Problem

<div class="side-box">
**Problem.** Given integers \( n, m \) determine whether or not there exists a
sequence \( X_1, X_2, \ldots, X_n \) such that each \( X_i \) is
greater than \( 1 \) and for each given pair of indices \( (a_1, b_1), (a_2, b_2),
\ldots, (a_m, b_m) \), \( X_{a_i} + X_{b_i} \) is prime.
</div>

## Solution

Obviously, create a graph with the vertices being each \( X_i \) and the
edges between them representing the given pairs. For an edge \( (a_1, b_1)
\), we can have its weight be given by \( X_{a_1} + X_{b_1} \), so we must
determine whether it is possible to assign values to the vertices so that
all edge weights are prime.

Observe that since each \( X_i \) is greater than \( 1 \), the minimum value we can have for an edge weight is \( 4 \). This means that the only even prime, \( 2 \) is ruled out. Thus, we have that for any pair \( (a_i, b_i) \)
\[
\begin{align*}
    X_{a_i} + X_{b_i} &\equiv 1 \pmod{2} \\
    \implies X_{a_i} &\equiv X_{b_i} + 1 \pmod{2}.
\end{align*}
\]
That is to say, adjacent vertices must always have opposite parity.

Supposing that we have such an arrangement that preserves this parity
condition, it is trivial to see that it is always possible to construct an
arrangement. We shall choose each even value to be \( 2 \) and each odd value to be \( 3 \). Even if there were a distinctness condition, however, it's highly likely that we would be able to construct such a sequence regardless.

We shall now describe how to code this. Denote the graph generated by our definition above by \( G \) and suppose this graph emits connected components \( G_1, G_2, \ldots, G_k \). For each component \( G_i \) we may arbitrarily choose some vertex \( x_i \) and run DFS on this vertex once (note we do not need to check both cases of \( x_i = 0, 1 \) due to symmetry) to check whether the component is two-colorable. Thus, our answer is given by
\[
    \bigwedge_{i = 1}^k \textsf{dfs}(G_i)
,\]
where \( \wedge \) represents logical AND.

For the curious reader, this question is simply asking whether there exists a <a href="https://en.wikipedia.org/wiki/Graph_coloring">two-coloring</a> for the graph.
