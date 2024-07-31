## Problem

<div class="side-box">
**Problem.** We must find \( n \) distinct integers such that
\[
    \max(a_1, a_2, \ldots, a_n) - \min(a_1, a_2, \ldots, a_n) = \sqrt{a_1 + a_2 + \cdots + a_n}
.\]
</div>

## Solution

**Observation.** WLOG, let \( a_1 < a_2 < \cdots < a_n \). The condition then turns into
\[
\begin{align*}
    a_n - a_1 &= \sqrt{a_1 + a_2 + \cdots + a_n} \\
    (a_n - a_1)^2 &= a_1 + a_2 + \cdots + a_n.
\end{align*}
\]
We shall assume this ordering for the sequence moving forward.

### First Attempt (Integer Overflow)

Suppose that we turn this into an arithemtic sequence. Let
\[
    a_i = a_1 + (i-1)d
.\]
This transforms our condition into
\[
\begin{align*}
    (n-1)^2 d^2 &= n a_1 + \frac{n(n-1)}{2} \cdot d \\
    \implies a_1 &= \frac{(n-1)^2 d^2}{n} - \frac{(n-1)d}{2} \\
    &= (n-1)d \left( \frac{(n-1)d}{n} - \frac{1}{2} \right).
\end{align*}
\]
If we take \( d \) to be equal to \( 2n \), then we get
\[
    a_1 = n(n-1)(4n - 5)
,\]
which is always an integer for \( n \ge 2 \), which is rather reassuring.

The only problem is that this sequence of integers quickly blows up for larger \( n \). Unfortunately, the problem gives the constraint that \( 1 \le a_i \le 10^9 \), which means that we'll have to play around a bit more.

### Correct Attempt

Let us step away from arithmetic progressions and be a bit more general in our reasoning. Let us consider sequences such that \( a_n = a_1 + k \) for some integer \( k \ge n - 1 \). Thus, the main condition turns into
\[
    k^2 = a_1 + a_2 + \cdots + a_n
.\]
Let \( K \) be the integer value such that
\[
    k^2 = n a_1 + K + k
,\]
which tells us that
\[
    a_1 = (k^2 - k - K) / n
,\]
so all we have to do is find valid values of \( k, K \) such that \( n \mid k^2 - k - K \), and then we win.

In order to get an idea of the values we can give to \( K \), we may bound it as follows:
\[
\begin{align*}
    \frac{(n-1)(n-2)}{2} \le K &\le (k - 1) + (k - 2) + \cdots + (k - n + 2) \\
    &= (n-2)k - \frac{(n-1)(n-2)}{2}.
\end{align*}
\]
This gives us an interval of length
\[
    (n-2)k - (n-1)(n-2) + 1
,\]
which is greater than \( n \) for \( k \ge n + 1 \) for all \( n \ge 3 \) (so I suppose we can just hardcode the case for \( n = 2 \)).

Motivated by this, let's suppose that \( k \equiv 1 \pmod{n} \) and \( K \equiv 0 \pmod{n} \), so that the divisibility condition always hold true. With the above work, we can see that \( k = n + 1 \), which allows us to determine the valid value of \( K \) through examining the interval.
