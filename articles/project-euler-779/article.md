## Problem

<div class="side-box">
**Problem.** Let \( p(n) \) denote the smallest prime that divides \( n \) and let \( \alpha (n) = \nu_{p(n)}(n) \). For positive integers \( K \), define
\[
    f_K(n) = \frac{\alpha(n) - 1}{(p(n))^K}
,\]
and let
\[
    \overline{f_K} = \lim_{N \to \infty} \frac{1}{N} \sum_{n = 2}^{N} f_K (n)
.\]
Find the value of
\[
    \sum_{K = 1}^{\infty} \overline{f_K}
.\]
</div>

## Solution

Let \( A \) denote the answer that we're looking for. Our first step will be to notice that prime power in the denominator of \( f_K(n) \) looks very sus and geometric series like, so we'll interchange the sums. In particular,
\[
\begin{align*}
    A &= \sum_{K = 1}^{\infty} \lim_{N \to \infty} \frac{1}{N} \sum_{n = 2}^{N} f_K(n) \\
    &= \lim_{N \to \infty} \frac{1}{N} \sum_{n = 2}^{N} \sum_{K = 1}^{\infty}  f_K(n) \\
    &= \lim_{N \to \infty} \frac{1}{N} \sum_{n = 2}^{N} \sum_{K = 1}^{\infty}  \frac{\alpha(n) - 1}{(p(n))^K} \\
    &= \lim_{N \to \infty} \frac{1}{N} \sum_{n = 2}^{N} \frac{\alpha(n) - 1}{p(n) - 1}.
\end{align*}
\]
Our second step will be to notice that \( p(n) \) and \( \alpha(n) \) are really just functions of the smallest prime factor. With this, we wish to transform the sum so that we go casewise based off of the smallest prime factor and its exponent, multiplying by the number of times such a number appears in the interval \( [2, N] \).
\[
\begin{align*}
    A &= \lim_{N \to \infty} \frac{1}{N} \sum\limits_{\substack{p \textrm{ prime,} \\ p \le N}} \sum_{a = 1}^{m} \frac{a - 1}{p - 1} \cdot P_{\le N}(p, a),
\end{align*}
\]
where \( m := \lfloor \log_{p} N \rfloor \) and \( P_{\le N}(p, a) \) counts the number of naturals \( x \) less than or equal to \( N \) such that \( p \) is the smallest prime factor of \( x \) and \( \nu_{p}(x) = a \). Thus it suffices to determine an expression for \( P_{\le N} (p, a) \).

Observe that there are \( \lfloor N / p^a \rfloor \) multiples of \( p^a \) in the interval. We would like to remove all multiples that contain a prime factor less than or equal to \( p \). Suppose that \( p = p_k \), where \( (p_n) \) is the sorted sequence of prime numbers. By inclusion-exclusion,
\[
    P_{\le N}(p_k, a) = \sum_{Q \subseteq P_k} (-1)^{|Q|} \left \lfloor \frac{N}{p_k^a \cdot Q_1 Q_2 \cdots Q_{|Q|}}\right\rfloor
,\]
where \( P_k := \{ p_1, p_2, \ldots, p_{k} \} \) and each \( Q_i \) is just the \( i \)th element of \( Q \). This result lends itself to a very nice approximation:
\[
    P_{\le N}(p_k, a) = \frac{N}{p_k^a} \left( 1 - \frac{1}{p_1} \right) \left( 1 - \frac{1}{p_2} \right) \cdots \left( 1 - \frac{1}{p_{k}} \right) + o(N)
.\]
This transforms our sum to be
\[
\begin{align*}
    A &= \lim_{N \to \infty} \sum\limits_{\substack{p_k \textrm{ prime,}  \\ p \le N}} \left( 1 - \frac{1}{p_1} \right) \left( 1 - \frac{1}{p_2} \right) \cdots \left( 1 - \frac{1}{p_{k}} \right) (p_k-1)^{-1} \sum_{a = 1}^{m} \frac{a - 1}{p_k^a} \\
    &= \lim_{N \to \infty} \sum\limits_{\substack{p_k \textrm{ prime,}  \\ p \le N}} \left( 1 - \frac{1}{p_1} \right) \left( 1 - \frac{1}{p_2} \right) \cdots \left( 1 - \frac{1}{p_{k}} \right) (p_k-1)^{-1} \frac{(m-1)p_k^{-m} - m p_k^{-m + 1} + 1}{(p_k-1)^2} \\
    &= \lim_{N \to \infty} \sum\limits_{\substack{p_k \textrm{ prime,}  \\ p \le N}} \left( 1 - \frac{1}{p_1} \right) \left( 1 - \frac{1}{p_2} \right) \cdots \left( 1 - \frac{1}{p_{k}} \right) (p_k-1)^{-3}.
\end{align*}
\]
Since we would like the answer within \( 12 \) decimal places of precision, it suffices to prime sieve up only a couple powers of \( 10 \) and then simply sum all of the terms.

This was a really cool problem.
