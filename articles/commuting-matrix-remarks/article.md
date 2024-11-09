\[
    \gdef\vec#1{\mathbf{#1}}
\]

Just yesterday in linear class, we reached Chapter 2, which started with a
review on matrix properties and a couple anti-patterns to look out for. One of
the warnings from the text, that \( AB \ne BA \) in general, sparked some nice
discussion on the commutativity of pairs of matrices. In particular, we took a
close look at the ending predicate of the warning: that \( A \) and \( B \) do
not commute *in general*.

Naturally, this leads one to question when \( A \) and \( B \) do commute, and I
was asked to provide some examples. My first thought went to \( B \) being a
polynomial (or even a power series; a prototypical example would be the matrix
exponential) in \( A \), as integer powers of \( A \) must commute with \( A \) by
construction. While this worked fine for offering an example in class, it also led
me to wonder something rather interesting:

<div class="side-box">
**Question.** Let \( A \) and \( B \) be \( n \times n \) matrices that commute. Must \( B \) be
a polynomial in \( A \)?
</div>

## Refining the Question

Before we go straight into tackling the question, there are a couple pieces of
information we can use to refine it slightly. Namely, notice that:

1. There is an asymmetry in the problem. Instead of saying that one matrix can
   be written as a polynomial in the other, we mandate that \( B \) must be a
   polynomial in \( A \). This allows for some trivial pathological answers in
   the negative to our question; for example, take \( A = \mathbf{0} \) so that
   in general \( B \) obviously cannot be a polynomial in \( A \).

   To handle this, we'll keep the asymmetry (it's hard to reason without good
   labels after all) but additionally require that \( A \) must be invertible so
   that we don't run into silly counterexamples.
2. By the [Cayley-Hamilton
   theorem](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem), we
   can actually write higher powers of \( A \) as linear combinations of lower
   powers of \( A \). This means we can write all matrices of the form \( A^k \),
   where \( k \ge n \) as linear combinations of \( I_n, A, A^2, \ldots, A^{n-1} \), so
   our desired polynomial is of degree \( n - 1 \).

Using these, we can turn our question in a more robust problem statement:

<div class="side-box">
**Problem.** Let \( A \) be an \( n \times n \) invertible matrix, and suppose \( B \) commutes with \( A \).
Must there exist a polynomial \( P \) of degree \( n - 1 \) such that \( P(A) = B \)?
</div>

## Tackling the Problem

At this point, we can now fully tackle the problem statement, which usually just
involves looking at different properties of what we're given and quite a bit of
trial and error.

After a bit of thinking, we arrive at the following insight: some sets of
matrices form closed rings under standard addition and subtraction. Suppose we
have some ring \( R \) of matrices that is a proper (i.e. not the entire)
subring of \( M_{n \times n}(\mathbb{R}) \). If we take \( A \) to be inside \(
R \) and \( B \) a matrix outside of \( R \) that commutes with \( A \), we can
find a counterexample, as \( P(A) \in R \) while \( B \not\in R \).

While this sounds complicated, the actual counterexamples we can find are rather
anticlimactic. For instance, let
\[
    A = \begin{bmatrix}
        1 & 0 \\
        0 & 1
    \end{bmatrix}, \qquad
    B = \begin{bmatrix}
        1 & 1 \\
        0 & 1
    \end{bmatrix}
.\]
Clearly the two matrices commute (the identity matrix commutes with all matrices),
but \( A \) doesn't have any off-diagonal elements so obviously
\( B \) cannot be a polynomial in \( A \). Thus the answer to our original
question is in the negative.

This is somewhat a sad result, but some more assumptions allow for us to
save it slightly. Let's additionally assume that \( A \) is diagonalizable with
distinct eigenvalues. Then we have the following claim:

<div class="side-box">
**Claim.** If \( A \) is diagonalizable with \( n \) distinct eigenvalues, then
\( B \) must also be diagonalizable.
</div>

*Proof.* Suppose \( (\lambda, \vec{v}) \) is an eigenpair of \( A \). Observe that by the commutativity of \( A \) and \( B \),
\[
    \begin{align*}
    A(B \vec{v}) &= BA \vec{v} \\
    &= B \lambda \vec{v} \\
    &= \lambda (B \vec{v}).
    \end{align*}
\]
This tells us that \( B \vec{v} \) is in the \( \lambda \)-eigenspace of \( A
\), which has dimension \( 1 \) (because we assumed \( n \) distinct
eigenvalues). But since \( \vec{v} \) is also in this eigenspace, \( \vec{v} \)
and \( B \vec{v} \) must be multiples, as neither get annihilated due to our
assumptions. Equivalently, \( \vec{v} \) is an eigenvector of \( B \). We may
repeat this for all eigenvectors of \( A \) to see that \( B \) has \( n \)
linearly independent eigenvectors, making it diagonalizable. \( \blacksquare \)

From this, we can write \( A = Q^{-1} S Q \) and \( B = Q^{-1} T Q \) and
observe that \( P(A) = Q^{-1} P(S) Q \) by the properties of diagonalizations.
If we wish to have \( P(A) = B \), then we must have that \( P(S) = T \). But
since the entries of \( S \) (the eigenvalues of \( A \)) are all distinct, this
reduces to finding a polynomial where \( P(S_{ii}) = T_{ii} \) for \( 1 \le i
\le n \). There always exists a degree \( n - 1 \) polynomial for which this is
true, so we can indeed write \( B \) as a polynomial in \( A \) as desired.
