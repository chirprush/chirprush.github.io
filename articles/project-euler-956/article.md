Hey, everyone! It's been quite a while hasn't it! What with the summer and
college work starting, I decided to put off blogging for a bit, and then that
bit eventually became quite a while (oops!). Although I haven't been blogging
for these past several months, the actual math work has still been going on
behind the scenes (some of the homework sets at college do tend to
slow down the process, but that's for a different article perhaps). I've been
missing the process of writing and what it can do for the both of us, so I
hope you're just as ready as I am to see some articles on elliptic curves,
number theoretic sum acceleration, and more. Until then, you'll have to wait.
It's time to go back to where the writing all started: Project Euler.

<div class="black-box">
**Problem.** Let \( \Omega(n) \) denote the number of prime factors (with multiplicity) of
\( n \). Define \( D(n, m) \) to be the sum of all divisors \( d \) of \( n \)
where \( \Omega(d) \) is divisible by \( m \).

Further, denote by \( n\$ \) the product
\[
    n \$ = 1! \times 2! \times \cdots \times n!
,\]
and denote by \( n\bigstar \) the product
\[
    n \bigstar = 1\$ \times 2\$ \times \cdots \times n \$
.\]
Find \( D(1\, 000 \bigstar, 1\, 000) \) modulo \( 999\, 999\, 001 \).
</div>

## Let Me Break it Down For You

Apologies for the bad heading joke. I just had to. For convenience, denote \( N
:= 1000, K := 1000, M := 999999001 \) so that we wish to find \( D(N \bigstar,
K) \) modulo \( M \).

One process that helps when breaking down more difficult problems is making
natural, incremental steps towards a goal and seeing where it leads us. One
natural step would be to assume we can find some prime factorization of \( N
\bigstar \). This assumption then breaks the problem into two smaller pieces

1. Computing a prime factorization for \( N \bigstar \)
2. Finding \( D(n, m) \) when we know the prime factorization of \( n \).

While these two pieces are still not immediately trivial, this is still a useful
mental framework for not getting a headache and actually solving the problem
(two things I like achieving!). 

I want to convince you that step (**1.**) is not so bad (where we take "bad" to be
in the sense of time complexity). Indeed, there are \( O(N / \log N) \)
primes up to \( N \), and we can compute them using a sieve in around \( O(N
\log N) \) time. Then, we can compute the factorization (stored as a dictionary)
for each \( i! \) for \( 1 \le i \le n \). Observe that we can use this list of
factorizations to produce a list of factorizations for \( i \$ \) for \( 1 \le i
\le n \): the factorization of \( i\$ \) is the prefix sum (where we sum the
exponents of each prime) of the factorial factorizations. The computation for \(
i\bigstar \) follows the same pattern (it is a prefix sum over each \( i\$ \)).
We can compute this in \( O(N^2 / \log N) \) time, which is plenty good.

Now that we're armed with some prime factorization from part (**1.**), we can
write \( N \bigstar = p_1^{e_1} p_2^{e_2} \cdots p_\ell^{e_\ell} \). Let's look
at part (**2.**) (i.e. the rest of the problem). We wish to determine some
simplified expression for \( D(p_1^{e_1} p_2^{e_2} \cdots p_\ell^{e_\ell}, K)
\). One could imagine trying to directly sum over all vectors of exponents that
have sum divisible by \( K \), but it doesn't really seem amenable to any fast
methods. Although not giving us an immediate solution, this is good, because we
know that we're being steered in some other direction.

So, what shall we do when we're looking for ideas? Play around! I won't
calculate explicit numerical examples here (if you want to get a better
understanding of the function I might recommend you do), but we can start with
some very simple cases. What is \( D(p^e, K) \)? Well, \( \Omega(p^e) = e \) for
any such prime power, so \( D(p^e, K) = 1 + p^K + \cdots + p^{cK} \) (you can quickly evaluate this with a geometric series!), where you
can imagine that the last prime power exponent is the greatest one that is less
than \( e \) (if you want to be specific, \( c = \lfloor e / K \rfloor \)). In particular, for the case of \( e < K \), \( D(p^e, K) \) is
just \( 1 \).

We roughly know the answer for prime powers, so what could we do to stitch them
together? Let's try finding some recursion/multiplicative property of \( D \).
For this, we'll have to make a small leap. Instead of only caring about one
residue class modulo \( K \) (i.e. caring about the prime factor counts
divisible by \( K \)), we'll have to take into account all residue classes. Let
\( D(n, m, r) \) denote the sum of the divisiors \( d \) of \( n \) such that \(
\Omega(d) \equiv r \pmod{m} \) (for a conceptual link, observe that \( D(n, m, 0) = D(n, m) \)). Now, observe the following
\[
    D(n p^e, K, r) = \sum_{i = 0}^{e} p^i D(n, K, (r - i) \bmod{K})
,\]
where \( n \) is coprime to \( p^e \) (notice that we aren't doing individual
primes but rather prime powers; if you worked out some examples, you've seen that
if the two numbers aren't coprime then you run into some misleading double
counting. Try it!). This might look like a bunch of symbols on the screen, but
it encodes a very natural intuition. Since \( D \) sums over factors of \( n p^e \),
let's call this factor \( d \), then \( d \) has some power (not necessarily
positive) of \( p \) inside it. We can go casewise on this power, call it \( i
\). Since \( p^i \mid d \), we can definitely multiply it in the sum. Now, we
must consider what factors of \( n \) divide \( d \). Since \( p^i \) has \( i
\) prime factors, we want the rest of \( d \) to have \( (r - i) \bmod{K} \)
prime factors to compensate. Summing over all cases gives us the above formula!

The existence of this formula smells like some DP (apply the recursive formula
to build up each prime factor until you have \( N \bigstar \)), but let's work
out some time complexities before we commit to this algorithm. At each stage, we
need to compute \( K \) values, each \( D(n, K, r) \) for \( 0 \le r < K \).
Computing this takes \( e_i \) additions (not to mention any other modular
arithmetic operations since we want the answer modulo \( M \), but pretend these
don't exist for now). Thus, the time complexity would be something like \(
O((e_1 + e_2 + \cdots + e_\ell)K) \). This is definitely a problem. Since \(
\nu_p (n!) = O(n) \), we can imagine that \( \nu_p(n \$) = O(n^2) \) and thus \(
\nu_p(n \bigstar) = O(n^3) \) by prefix sums. Since there are \( O(N / \log N)
\) primes up to \( N \), this looks roughly like \( O(N^4 K / \log N) \), which
is definitely not happening.

We need some speedups!

## Hints of Convolution and Slight Overkill

Let's remind ourselves that we're working modulo \( M \) (\( M \) is prime if
you haven't already checked). When I first saw the summation above, my first
instinct was a convolution. Indeed, \( D(np^e, K, r) \) is the convolution (with
indices modulo \( K \)) of \( D(p^e, K, r) \) and \( D(n, K, r) \) (where all of
these are treated as arrays indexed by \( r \)). 

Another quick observation is that since \( K \mid M - 1 \), we can some find \( K
\)th root of unity \( \omega \) modulo \( M \). This opens up a lot of
interesting ideas. Unfortunately, and fortunately, I was thinking about
cyclotomic integers at the time, so I missed some other cool, less technical
solutions.

The big observation is that, upon seeing this convolution, we can think about
polynomials instead of just plain old arrays of numbers. Indeed, suppose we wish
to find \( D(p_1^{e_1} p_2^{e_2} \cdots p_\ell^{e_\ell}, K, r) \) for any \( 0
\le r < K \). Then, consider the polynomial
\[
    f(X) = (1 + p_1 X + \cdots + p_1^{e_1} X^{e_1}) \cdots (1 + p_\ell X + \cdots + p_\ell^{e_\ell} X^{e_\ell})
.\]
The sum of the terms of the coefficients in front of every term of degree
congruent to \( r \) modulo \( K \) is then precisely our answer. Framed in this
manner, it is clear that a [roots of unity
filter](https://artofproblemsolving.com/community/c1340h1003741_roots_of_unity_filter?srsltid=AfmBOorgYiA0CNB5iDFLlw8qlH_4-cH9AObiDH_90W-7e_ewovLeURhx)
would work (using our root \( \omega \) instead of complex numbers, of
course). Indeed, unfortunately (as I said earlier), I missed this, which is a
bit of an oops since I really shouldn't have. I think I just got too excited
seeing something with cyclotomic integers because I was thinking about them a
little bit earlier (I might make a blog post later about how you can efficiently
implement them with SIMD, but we'll see).

Fortunately, by viewing this as a slightly harder problem, I learned a lot more!
I viewed the problem as evaluating \( f(X) \) over the ring \( \mathbf{Z}_M [X]/(X^K - 1) \).

In other words, we can treat our polynomial as an array \( f[i] \), where \(
f(x) = \sum_{i = 0}^{K-1} f[i] \omega^i \), where \( \omega \) is a \( K \)th
root of unity once again. It then suffices to figure out how to quickly multiply
these polynomials modulo \( X^K - 1 \) while keeping the coefficients modulo \(
M \). Once we have the multiplied polynomials, it suffices to just output the
constant term as the answer. How shall we do this polynomial multiplication?
We'll do this how any other fast polynomial multiplication algorithm works: the
fast Fourier transform!

## The Algorithm

As at the start of the problem, we separated it into two parts based on some
assumption for ease of cognitive load and clarity. Let's do this again! I'm
going to outline what the algorithm is for finding an answer so the reader can

1. Recap what we've gone through, and
2. See how everything fits together so that the transform is the only remaining
   key piece we need to figure out.

So, let's go through our algorithm!

1. First, we can find a primitive root \( \zeta \) modulo \( M \) and then set
   \( \omega := \zeta^{(M-1)/K} \) to get a \( K \)th root of unity modulo \( M
   \).
2. Next, we can factorize \( N \bigstar = p_1^{e_1} \cdots p_\ell^{e_\ell} \) using some prefix sums.
3. For each \( i \in \{1, \ldots, \ell \} \) do the following:
    * Let \( a[i][j] \) be an array (indexed by \( 0 \le j < K \)) such that
    \[
        a[i][j] = p_i^{j} + p_i^{j + K} + \cdots + p^{j + T K} \bmod{M}
    ,\]
    where \( T = \left\lfloor \frac{e_i - j}{K} \right\rfloor \). Equivalently,
    \[
        a[i][j] = p_i^j \frac{p_i^{(T+1)K} - 1}{p_i^K - 1} \bmod{M}
    .\]

    * Compute \( \hat{a}[i] = \textsf{NTT}([a[i][0], \ldots, a[i][K-1]], \omega) \)
4. Compute \( \hat{d}[j] = \hat{a}[1][j] \times \hat{a}[2][j] \times \cdots \times \hat{a}[\ell][j] \).
5. Compute \( d = \textsf{INTT}(\hat{d}, \omega) \)
6. Output \( d[0] \).

Indeed, we using the NTT ([number-theoretic
transform](https://mathworld.wolfram.com/NumberTheoreticTransform.html)) to
efficiently multiply polynomials over our ring. Another way to intuit our
algorithm is that we are utilizing the [convolution
theorem](https://en.wikipedia.org/wiki/Convolution_theorem). If you notice, this
algorithm actually gives us the answer to \( D(N\bigstar, K, r) \) (contained in
array \( d \)) for all \( r \) all at once. That's why this solution is probably
a little bit more overkill than using a simple roots of unity sieve.

Now, it suffices to figure out what's going on behind the transform algorithm
itself.

## The (Fast) Number-Theoretic Transform

We shall now work under \( \mathbf{F}_p \) so I don't have to put congruences
everywhere.

Suppose \( x \in \mathbf{F}_p^L \) is an array of length \( L \) and \( \omega \in \mathbf{F}_p \) is an \( L
\)th root of unity. We wish to find its number-theoretic transform, \( \hat{x}
\), which is the array such that
\[
    \textsf{NTT}(x, \omega) := \hat{x}[k] = \sum_{i = 0}^{L - 1} x[i] \omega^{ik}
.\]
But, of course, if we naively evaluate it like this, we run into time problems.
This would be an \( O(L^2) \) algorithm! We can instead build a fast recursive
algorithm.

For our base case, notice that when \( L = 1 \), \( \hat x = x \). Now, let \( q
\) be the smallest prime factor of \( L \). Since \( L > 1 \), we have that \( q > 1 \). We typically call \( q \) the *radix* (typically you'll only see radix
\( 2 \) algorithms because people zero pad their arrays until \( L \) is a
power of \( 2 \), but we can't do this because it would destroy our answer),
because we are going to separate the NTT of length \( L \) into \( q \) NTTs
of length \( \ell := L / q \).

For \( r \in \{0, 1, \ldots, q - 1 \} \), let
\[
    x_r = \bigl[x[r], x[q + r], \ldots, x[q (\ell - 1) + r] \bigr]
,\]
so that \( x_r \) is an array of length \( \ell \) of all the coefficients with
indices that are congruent to \( r \) mod \( q \). Moreover, compute \( \hat{x}_r = \textsf{NTT}(x_r, \omega^q) \) (as \( \omega^q \) is an \(
\ell \)th root of unity), their number-theoretic transforms.

Now comes the key insight. Observe that
\begin{align*}
    \hat{x}[k] &= \sum_{i = 0}^{\ell q - 1} x[i] \omega^{ik} \\
    &= \sum_{r = 0}^{q - 1} \sum_{j = 0}^{\ell - 1} x[qj + r] \omega^{(qj + r)k}
    \\
    &= \sum_{r = 0}^{q - 1} \omega^{rk} \sum_{j = 0}^{\ell - 1} x[qj + r] \left( \omega^q \right)^{jk} \\
    &= \sum_{r = 0}^{q - 1} \omega^{rk} \hat{x}_r[k]
.\end{align*}
We can calculate the NTT of \( x \) efficiently using the sub-NTTs (fun fact:
the \( \omega^{rk} \) coefficients are usually called twiddle factors)!

Now, let's look at the time complexity. At each recursive level of the NTT,
there are \( t \) calls of with arrays of length \( L / t \). At each call, we
iterate over the array of length \( L / t \) perform \( q \) operations with the
twiddle factors. For our purposes, \( q \) is small enough to be constant (\( K
\) in our case is \( 2^3 5^3 \) so \( q \in \{2, 5 \} \)), so one level of calls
is just \( O(L) \) time. Since we divide by a prime factor each time, there are
at most \( O(\log L) \) levels. Thus, the time complexity is \( O(L \log L) \),
which is the desired faster speedup compared to \( O(L^2) \) naively.

Inverting the NTT is just a case of applying the NTT with \( \omega^{-1} \)
and then dividing each coefficient by \( L \). There's not much to say there.
Thus, we've completed the necessary steps to finish the problem.

Yippee!

## Conclusions

While I tried to give good exposition, motivation, and background for the
techniques used in this problem, I couldn't explain everything in a
self-contained manner. In fact, doing so would probably give me a big headache!
However, I encourage the reader to look up and read in more depth some of the
number-theoretic or algebraic notions mentioned in this writeup. These are some
really beautiful results that, used together, solve problems an efficient,
elegant manner. That being said, it is also partly my fault. I think I'm rusty!
This isn't so surprising given the long break, but it's another piece of
motivation for me to get better at explaining ideas. I'm definitely going to
look towards more visuals soon (hopefully maybe it'll be really cool I just need
to figure out like all of OpenGL and lots of numerics).

ALSO! Look out for more articles in the future! There's a bunch of stuff I want
to cover, and I'm praying to everything that I don't get swamped with homework
that stops me from writing. Thank you for reading, and if you skimmed down here,
thank you for skimming too (now go back and read) (bring those average literacy
rates up buckaroo).
