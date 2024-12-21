Hey everyone! It's almost winter break, and I should probably get to working more on college apps, so here's a short and sweet result in the meantime :)

The proof below may at first seem like it was pulled out of nowhere, but it does
actually have some proper backstory. I was playing around with the generating
function for partitions for a Project Euler problem (at the time I hadn't
actually made the connection that it was the generating function for
partitions), and at some point I thought it would be cool to attempt deriving an
asymptotic using a partial fraction decomposition, so I wished for a way to
factor the denominator of the generating function. Although this didn't really
go to plan, I still stumbled upon a really cool and somewhat random identity.

## The Result

<div class="black-box">
**Theorem.** For natural \( n \) we have that
\[
    \sum_{k = 1}^{n} \phi(k) \left \lfloor \frac{n}{k} \right \rfloor = \frac{n(n + 1)}{2}
.\]
</div>

*Proof.* The proof we'll give arises from a very interesting double counting
argument. Consider the polynomial
\[
    p_n(x) = \prod_{k = 1}^n (x^k - 1)
.\]
There are a couple properties apparent from writing the polynomial this way. In
particular, each factor \( x^k - 1 \) has \( k \) roots, precisely the \( k \)th
roots of unity. Thus, we can ascertain the overall degree as
\[
    \deg p_n(x) = \sum_{k = 1}^n \deg (x^k - 1) = \sum_{k = 1}^{n} k = \frac{n(n+1)}{2}
.\]
But, using double counting, there is another way to write the polynomial: we can
look at the multiplicity of each root of unity factor on its own. For example,
\( p_2(x) = (x - 1)(x^2 - 1) = (x-1)^2 (x+1) \). If we then add up the
multiplicities of each root of the polynomial, we get the degree again. Thus it
suffices to answer the following question: for coprime \( j, k \) (because
otherwise we can reduce them) what is the multiplicity of \( \alpha_{jk} := \exp(2 \pi i j / k)
\) in \( p_n(x) \)?

Coupling together the fact that \( \alpha_{jk} \) can only be a root of \( x^m - 1 \) if \( k \mid m \) and that its multiplicity in \( x^m - 1 \) is at most one, we can see that the multiplicity of \( \alpha_{jk} \) in \( p_n(x) \) is \( \lfloor n / k \rfloor \), precisely the number of numbers less than or equal to \( n \) that are a multiple of \( k \). This holds irrespective of \( j \), of which there are \( \phi(k) \) valid values (since \( j \) is coprime to \( k \)). The sum of the multiplicities of each \( \alpha_{jk} \) for a fixed \( k \) is then \( \phi(k) \lfloor n / k \rfloor \). Taking \( k \) from \( 1 \) to \( n \), we then recover
\[
    \sum_{k = 1}^{n} \phi(k) \left \lfloor \frac{n}{k} \right \rfloor = \deg
    p_n(x) = \frac{n(n + 1)}{2}
,\]
which is precisely what we wished to prove. \( \blacksquare \)

We remark that the most concise way to express this idea is the following
remarkable equivalence of products:
\[
    \prod_{k = 1}^{n} (x^k - 1) = \prod_{k = 1}^{n} \Phi_k(x)^{\lfloor n / k \rfloor}
,\]
where \( \Phi_k(x) \) is the \( k \)th cyclotomic polynomial in \( x \). This
comes as a consequence of the well-known identity
\[
    \prod_{d \mid n} \Phi_d(x) = x^n - 1
.\]
In fact, this is merely a statement about how the cyclotomic polynomials and
roots of unity polynomials are multiplicative bases for each other, which
has some interesting consequences I hope to perhaps write about in the future.

Happy holidays! >:)
