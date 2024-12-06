This was actually a rather nice problem I had pinned for quite a while on
Project Euler, so I'm glad I got around to actually solving it.

<div class="black-box">
**Problem.** Write \( (1 + \sqrt{7})^k = \alpha(k) + \beta(k) \sqrt{7} \).
Now, define \( g(x) \) to be the the smallest positive integer \( k \) such that we
simultaneously have
\begin{align*}
    \alpha(k) &\equiv 1 \pmod{x}, \\
    \beta(k) &\equiv 0 \pmod{x}
,\end{align*}
and \( g(x) = 0 \) if there does not exist any \( k \). Calculate
\[
    G(N) = \sum_{x = 2}^{N} g(x)
\]
for \( N = 10^6 \).
</div>

At first this seems like a chaining of very arbitrary definitions, but we can
unravel this a bit more.

## Some Basic Observations

Our first thing that we'll notice is that the choice of equivalence classes
modulo \( x \) being \( 1 \) and \( 0 \) is not at all arbitrary. In particular,
\( \alpha(0) \) and \( \beta(0) \) satisfy these congruences, although \( 0 \) is not
a positive integer. This does hint that we'll be doing some work with orders and
periods.

In particular, we are motivated to realize that since \( g(x) \) intuitively
represents a period, it is lcm-multiplicative. That is, for \( k = p_1^{e_1}
p_2^{e_2} \cdots p_m^{e_m} \),
\[
    g(k) = \operatorname{lcm} \left( g(p_1^{e_1}), g(p_2^{e_2}), \ldots, g(p_m^{e_m}) \right)
,\]
so now it suffices to determine the value of \( g \) for prime powers only.

Some things should still be in the back of one's mind while solving this, though. We still haven't determined when a solution exists, which is rather important to know.

## An Erroneous Solution Path

In a similar vein to solving for \( \cos(x) \) in terms of complex
exponentials, let's see that
\begin{align*}
    \alpha(k) &\equiv \frac{(1 + \sqrt{7})^k + (1 - \sqrt{7})^k}{2} \pmod{x}, \\
    \beta(k) &\equiv \frac{(1 + \sqrt{7})^k - (1 - \sqrt{7})^k}{2 \sqrt{7}} \pmod{x}
.\end{align*}
Notice that, if we could find our solutions to \( m^2 \equiv 7 \pmod{p} \), it
would be trivial to obtain a direct expression for \( \alpha(k) \) and \(
\beta(k) \). With this direct expression, we could quickly check values until we
arrived at the desired congruences.

There are some implicit assumptions that we should be aware of while trying this
solution path. It may not be the case that \( \sqrt{7} \in \mathbb{Z}/x \mathbb{Z} \). In fact, number theory tells us that we can only have this square root if \( 7 \) is a quadratic residue modulo \( x \). *Does this mean that there exists no solution (and thus \( g(x) = 0 \)) for \( x \) where \( 7 \) is a quadratic nonresidue?*

Unfortunately, **no**. Consider that \( 7 \) is a quadratic nonresidue modulo \( 13 \). However, with a bit of work, the reader can verify that \( g(13) = 168 \). This fact (especially with \( 13 \) being prime) effectively kills the solution path. We simply do not gain any information for \( x \) where \( 7 \) is a quadratic nonresidue.

## No Way It's \( GL(2, p^n) \)

That didn't work out, so let's return to the start of the problem. We want an
efficient way to compute the coefficients, so we're motivated to consider a
recurrence of some kind. Notice that
\[
    (1 + \sqrt{7})^k = (1 + \sqrt{7})^{k - 1} (1 + \sqrt{7})
,\]
and multiplying everything out and writing in terms of \( \alpha(k) \) and \( \beta(k) \) gives
\begin{align*}
    \alpha(k) &= \alpha(k - 1) + 7 \beta(k - 1), \\
    \beta(k) &= \alpha(k - 1) + \beta(k - 1)
,\end{align*}
and we can indeed take these under congruences. Since it suffices to only
consider prime powers by our initial observations, take \( x = p^n \). Thus,
\begin{align*}
    \alpha(k) &\equiv \alpha(k - 1) + 7 \beta(k - 1) \pmod{p^n}, \\
    \beta(k) &\equiv \alpha(k - 1) + \beta(k - 1) \pmod{p^n}
.\end{align*}
Taking a bit of inspiration from a [previous blog
post](https://chirprush.github.io/articles/matrix-modular-arithmetic/index.html), we can introduce some
linear algebra and group theory here. Define \( \mathbf{v}_k = \begin{bmatrix}
 \alpha(k) & \beta(k) \end{bmatrix}^T \) so that
\begin{align*}
    \mathbf{v}_k &= \begin{bmatrix}
        1 & 7 \\
        1 & 1
    \end{bmatrix} \mathbf{v}_{k - 1} \pmod{p^n} \\
    \implies \mathbf{v}_k &= \begin{bmatrix}
        1 & 7 \\
        1 & 1
    \end{bmatrix}^k \begin{bmatrix}
        1 \\
        0
    \end{bmatrix} \pmod{p^n}
.\end{align*}
For convenience, denote this matrix by \( A \).

Now, since we want to find when \( \mathbf{v}_k \equiv \begin{bmatrix} 1 & 0 \end{bmatrix}^T \pmod{p^n} \) it suffices to find the smallest \( k \) such that
\[
    \begin{bmatrix}
        1 & 7 \\
        1 & 1
    \end{bmatrix}^k \equiv
    \begin{bmatrix}
        1 & 0 \\
        0 & 1
    \end{bmatrix} \pmod{p^n}
,\]
where all congruences are taken elementwise. This \( k \) is precisely the order
of the matrix. This approach is particularly nice because it also tells us which
cases do not have solutions. Since the determinant of A  is \( -6 \), we can say
that \( g(x) = 0 \) precisely when \( \gcd(x, 6) > 1 \). This is the case
because (analyzing the determinants of the left and right side) \( (-6)^k
\not\equiv 1 \pmod{x} \) ever for such \( x \).

While it's hard to pin down what this order is as we vary the modulus, \( p^n
\), we can identify a multiple of it quite easily. In particular, the cyclic
group generated by taking powers of \( A \) is a subgroup of the group of \(
2\times 2 \) matrices with elements over \( \mathbb{Z}/p^n \mathbb{Z} \)
(otherwise known as \( GL(2, p^n) \)). As a consequence of [Lagrange's
Theorem](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)), the
order of \( A \) must divide the order of \( GL(2, p^n) \), which is given by
\[
    |GL(2, p^n)| = (p^{2n} - p^{2n - 1})(p^{2n} - p^{2n - 2}) = p^{4n - 3} (p - 1)^2 (p + 1)
.\]
If we test the factors of this expression for each \( x = p^n \) and find the
smallest factor \( k \) where \( A^k \equiv I_2 \), then we've essentially
solved the problem. The only thing left to check now is the big question: **is the
time complexity viable?**

First, let's try and get an estimate of the number of factors of \( |GL(2, p^n)| \). Observe that
\begin{align*}
    \sigma(|GL(2, p^n)|) &\le \sigma(p^{4n - 3}) \sigma((p - 1)^2) \sigma(p + 1) \\
    &\le (4n - 2) \sigma(p - 1) 2^{\omega(p - 1)} \sigma(p + 1) \\
    &= O(n (\log p)^3)
,\end{align*}
where \( \omega(\cdot) \) denotes the [distinct prime
factors](https://en.wikipedia.org/wiki/Prime_omega_function), and we have used
that \( \sigma(n) = O(\log n) \) and \( \omega(n) = O(\log \log n) \) (see the
Appendix for proofs).

If we create a least prime factor sieve we can easily factor and find these
factors in \(  O(n \log p) \) time, which is dominated by the number of factors
anyway so that's not a problem. However, we're finding the factors over
every prime power less than or equal to \( N \), so we should check that the
time complexity of the entire program is viable. Observing that
\begin{align*}
    \sum_{p \le N} \sum_{n = 1}^{\lfloor \log_p N \rfloor} n (\log p)^3 &\le
    \sum_{p \le N} \lfloor \log_p N \rfloor^2 (\log p)^3 \\
    &\le (\log N)^2 \sum_{p \le N} \log p \\
    &\le (\log N)^2 \int_2^N \log x \, d\pi(x) \\
    &= O(N (\log N)^2)
,\end{align*}
we see that our solution is indeed viable. The actual program I wrote takes
quite a while to compute the answer, though, so either I could be off by a
factor somewhere, or it's just a consequence of a huge constant.

Happy December everybody >:)

## Remarks

Solving any problem on Project Euler unlocks the solution forum, where you get
to see other people's solutions to the problem. Looking at these solutions,
there was actually two observations that I very regretfully missed.

Firstly, the people on the forums made the observation that \( g(p^n) = p^{n - 1}g(p) \). This one simplification reduces the computation time immensely, as now we need only compute \( g(p) \) for each prime less than \( 10^6 \), as opposed to each pure prime power. Now,  we could normally proceed and iterate over the factors of \( (p^2 - 1)(p^2 - p) \), but we actually can do better. This is where the second observation comes in.

Instead of considering the group of invertible matrices modulo \( p \) to obtain
a multiple of the order of the matrix for the recurrence relation, we can
identify an even smaller, richer embedding that reduces the upper bound of the
order. In particular, we may view \( 1 + \sqrt{7} \) as an element of \(
\mathbb{F}_p (\sqrt{7}) \), i.e. the field of order \( p \) adjoin \( \sqrt{7}
\). There are two cases for the order of this field:

1. Case: \( 7 \) is a quadratic residue modulo \( p \). In this case,
    \[
        (x - (1 - \sqrt{7}))(x - (1 + \sqrt{7})) = x^2 - 2x - 6
    \]
    is reducible over \( \mathbb{F}_p \), so \( \mathbb{F}_p (\sqrt{7}) \cong
    \mathbb{F}_p \). The multiplicative order of any element is thus a factor of
    \( p - 1 \).
2. Case: \( 7 \) is a quadratic nonresidue modulo \( p \). In this case,
    \[
        (x - (1 - \sqrt{7}))(x - (1 + \sqrt{7})) = x^2 - 2x - 6
    \]
    is irreducible over \( \mathbb{F}_p \). The multiplicative order is then \( p^2 - 1 \).

Since we have that \( \operatorname{lcm}(p - 1, p^2 - 1) = p^2 - 1 \), we know that \( g(p)
\mid (p^2 - 1) \), so it suffices to check the factors of \( p^2 - 1 \).

## Appendix: Asymptotics for \( \sigma(n), \omega(n) \)

In order to determine the asymptotics for \( \sigma(n) \) and \( \omega(n) \),
we'll actually find their average order. That is, we shall show that
\[
    \frac{1}{N} \sum_{n = 1}^{N} \sigma(n) = O(\log N)
,\]
and
\[
    \frac{1}{N} \sum_{n = 1}^{N} \omega(n) = O(\log \log N)
.\]
For convenience let \( d(n, k) : \mathbb{N}^2 \to \{0, 1\} \) be the function
where \( d(n, k) = 0 \) if \( k \nmid n \) and \( d(n, k) = 1 \) if \( k
\mid n \).

For the erstwhile function, observe that
\begin{align*}
    \frac{1}{N} \sum_{n = 1}^{N}  \sigma(n) &= \frac{1}{N} \sum_{n = 1}^N
    \sum_{k = 1}^N d(n, k) \\
    &= \frac{1}{N} \sum_{k = 1}^{N} \sum_{n = 1}^{N} d(n, k) \\
    &= \frac{1}{N} \sum_{k = 1}^N \left \lfloor \frac{N}{k} \right \rfloor \\
    &= O \left( \sum_{k = 1}^N \frac{1}{k} \right) \\
    &= O(\log N)
,\end{align*}
as it is well known that the [Harmonic
numbers](https://en.wikipedia.org/wiki/Harmonic_number) grow at a rate of \(
\log N \).

For the latter function, notice that
\begin{align*}
    \frac{1}{N} \sum_{n = 1}^N \omega(n) &= \frac{1}{N} \sum_{n = 1}^N \sum_{p \le N} d(n, p) \\
    &= \frac{1}{N} \sum_{p \le N} \sum_{n = 1} d(n, p) \\
    &= \frac{1}{N} \sum_{p \le N} \left\lfloor \frac{N}{p} \right\rfloor \\
    &= O \left( \sum_{p \le N} \frac{1}{p} \right) \\
    &= O(\log \log N)
,\end{align*}
since the sum of the reciprocal of the primes grows at a rate of \( \log \log N \).
