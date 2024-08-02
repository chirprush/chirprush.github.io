## Problem

<div class="side-box">
**Problem.** Suppose we have a graph with \( n \) vertices and a permutation \( a \) of the numbers \( 1 \) through \( n \), and we add an edge on the graph for every pair of vertices \( (i, j) \) if
\[
    | i - j | + | a_i - a_j | \le k
.\]
Determine the permutation \( a \) for which the number of distinct cliques in the graph is a minimum.
</div>

Note: A *clique* is defined to be a complete subgraph of a graph.

**Constraints.** We have that

- \( 1 \le t \le 1600 \),
- \( 2 \le n \le 40 \),
- \( 1 \le k \le 2n \)

## Solution

We shall first tackle the problem of creating a clique of size \( m \). Immediately, we see that \( m \le \min\{n, k\} \).

**Claim.** A clique of size \( m \) is constructible with cost \( m \) at the very least.

*Proof.* Observe first that any cost for a clique of size \( m \) cannot be lower than \( m \) because the maximum value of \( |i - j| \) is achieved when \( i = 1 \) and \( j = m \), and \( |a_i - a_j| \ge 1 \), so their sum must be greater than or equal to \( m \) for some pair of vertices \( (i, j) \).

We provide the following construction for a permutation that costs only \( m \) and results in a clique of size \( m \):
\[
    a: \left\lceil m / 2 \right\rceil, (\left\lceil m / 2 \right\rceil - 1), \ldots, 1, m, (m-1), \ldots, (m + 1 - \left\lceil m / 2 \right\rceil)
,\]
though because the math is a tad gruesome, we shall not verify here that the sequence does in fact fulfill the cost conditions stated above. \( \blacksquare \)


Now since we have that a clique of size \( m \) is constructible and \( m \le \min\{n, k\} \), the solution is rather obvious (simply form as many cliques of greatest size that we can). We also trivially have that when \( k \ge n \), the minimum clique number is \( 1 \), which seems to be a rather good sanity check. In particular, we also have a closed form for the minimum number of cliques needed:
\[
    \textsf{cliques} = \left\lceil \frac{n}{\min\{n, k\}} \right\rceil
.\]
