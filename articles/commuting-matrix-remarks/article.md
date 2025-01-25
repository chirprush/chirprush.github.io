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

<div class="black-box">
**Question.** Let \( A \) and \( B \) be \( n \times n \) matrices that commute.
Must one of the matrices be a polynomial of the other?
</div>

## Refining the Question

Before we go straight into tackling the question, there are a couple pieces of
information we can use to refine it slightly. Namely, notice that:

1. There is a symmetry in the problem. Call a pair of matrices \( (A, B) \)
   *good* if the matrices commute and have one that can be written as a
   polynomial in the other. Obviously a good pair satisfies our problem, and it
   seems reasonable that if a pair \( (A, B) \) is good then \( (B, A) \) should
   be good.

   Indeed, considering the problem this way (as opposed to ordaining \( A \) to
   be a polynomial in \( B \) or vice versa) helps to eliminate otherwise
   unsatisfying counterexamples. If we take \( B = I_n \) and \( A \) to be any
   non-diagonal matrix, obviously they commute and \( A \) is not a polynomial
   in \( B \) (any polynomial in \( B \) can only be diagonal). However, \( B \)
   is trivially a polynomial in \( A \).
2. By the [Cayley-Hamilton
   theorem](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem), we
   can actually write higher powers of \( A \) as linear combinations of lower
   powers of \( A \). This means we can write all matrices of the form \( A^k \),
   where \( k \ge n \) as linear combinations of \( I_n, A, A^2, \ldots, A^{n-1} \), so
   our desired polynomial is of degree \( n - 1 \). The existence of such a
   polynomial allows one to show that even \( A^{-1} \) (if it exists) is a
   polynomial in \( A \).

Using these, we can turn our question in a more robust problem statement:

<div class="black-box">
**Problem.** Let \( A, B \) be \( n \times n \) matrices that commute.
Must there exist a polynomial \( P \) of degree at most \( n - 1 \) such that \( P(A) = B \) or \( P(B) = A \)?
</div>

## Tackling the Problem

At this point, we can now fully tackle the problem statement, which usually just
involves looking at different properties of what we're given and quite a bit of
trial and error.

One of my first steps was algebraically bashing out commutativity and
polynomiability (definitely not a word) for \( 2 \times 2 \) matrices, utilizing the fact that
any such polynomial need only be degree \( 1 \). It turns out in this case
(unless I'm making some weird mistakes with division by zero) that they are
equivalent! So, what happens if we go up a dimension?

It turns out that we actually run into some problems. Consider the matrices
\[
    A = \begin{bmatrix}
        0 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 0
    \end{bmatrix}, \quad
    B = \begin{bmatrix}
        0 & 0 & 1 \\
        0 & 0 & 0 \\
        0 & 0 & 0
    \end{bmatrix}
.\]
You can check for yourself that these matrices both commute: \( AB = BA =
\mathbf{0} \). For polynomials, however, we run into some problems. By simple
matrix multiplication \( A^2 = A \) and \( B^2 = \mathbf{0} \). As such, a
polynomial sending \( A \) to \( B \) or \( B \) to \( A \) would have to be
linear. This is clearly absurd! Indeed, even though the matrices commute,
neither can be written as a polynomial in the other.

Upon first reaction, I thought things could be patched up with invertibility in
some way, but a little more thinking shows that this also isn't possible!
Consider the matrices
\[
    A = \begin{bmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 2
    \end{bmatrix}, \quad
    B = \begin{bmatrix}
        2 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 2
    \end{bmatrix}
.\]
These are diagonal matrices, so they clearly commute. Polynomials in diagonal
matrices are easy to control because they distribute into the diagonal elements.
This behavior leads to trouble. If we suppose \( P(A) = B \), then \( P(1) \)
must be both \( 2 \) and \( 1 \). If we suppose \( P(B) = A \), then \( P(2) \)
must be both \( 1 \) and \( 2 \)! Thus, essentially due to having non-distinct
eigenvalues, there cannot exist such a polynomial.

While our property unfortunately does not hold in general for matrices with
non-distinct eigenvalues, this seem sharp in a way. In particular, let's
additionally assume that \( A \) is diagonalizable with distinct eigenvalues.
Then we have the following claim:

<div class="black-box">
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

Although we've worked with matrices throughout this article, you can essentially
substitute a finite dimensional linear transformation in and achieve the same
results. This begs the question, *what about infinite dimensional linear
transformations*? Can I write the Fourier transform as a polynomial in
convolutions with arbitrary functions? Does this even make sense to say? I'm not
too familiar with infinite dimensional linear algebra, but this seems like the
perfect gateway. Stay tuned!

*Editing remarks: this article originally structured the initial discussion
differently and gave a rather unsatisfying counterexample that was hardly a
counterexample. I couldn't stop thinking about the problem afterwards, so I had
to fix it. In addition, I've added a conclusion looking towards further results/exploration.*
