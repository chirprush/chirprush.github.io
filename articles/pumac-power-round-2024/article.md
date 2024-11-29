This year was actually my first participating in
[PUMAC](https://jason-shi-f9dm.squarespace.com/) and it was a really cool
experience! Our team placed 6th for the team round which was honestly a
surprise, and the day of the competition was certainly challenging, but what
stood out to me the most was the power round.

The concept of the PUMAC power round is rather simple: your team is thrown
straight into a specifically chosen topic in pure mathematics and given roughly
a week to figure it out, solving proof-based problems along the way. Personally,
I think this is a really cool contrast to the standard math competition
experience, which is based on solving hard, concrete problems in a very small
amount of time. It's a great window into higher level mathematics (in fact,
the contest itself had a question that was stated to be an active area of
resesarch).

[This year's power
round](https://static1.squarespace.com/static/570450471d07c094a39efaed/t/673a4bada1036103a5a7897f/1731873709355/Power2024_Updated_1117.pdf)
introduced the field of measure theory (the formalization of volumes and
dimensions to even perhaps pathological sets) to give a rigorous exploration and
characterization of fractals. Below is my attempt to capture the essence of the
commentary given, and a compartmentalization of our team solutions, at least as
far as we got during the contest window. I hope you enjoy!

*Note: there are some minor changes and conventions that should be pointed out.
Namely, \( \subset \) during this contest denotes subset or subset equals. In
addition, I will **switch around the order** of some problems if it is more
conducive for understanding. Much of the exposition is structured similarly to
the power round document (all credit to the contest organizers for this), but
I will occasionally interject with some intuition.*

## Measures

The first half of contest document is spent building up the idea of the
Hausdorff measure, the quintessential tool for working with fractals later on.
This rising action starts with the definition of \( \sigma \)-algebras and a
measure itself.

**Definition.** A **\( \sigma \)-algebra** \( \Sigma \) on a set \( X \) is a set of subsets
of \( X \) satisfying the following rules:

1. The empty set \( \emptyset \) is in \( \Sigma \)
2. For any set \( A \) in \( \Sigma \), its complement (i.e. the set
   containing all elements that \( A \) doesn't) is in \( \Sigma \)
3. For any [countable](https://en.wikipedia.org/wiki/Countable_set) list of
   sets in \( \Sigma \), their union (i.e. the set containing all elements in
   any set of the list) is in \( \Sigma \).
4. For any countable list of sets in \( \Sigma \), their intersection (i.e. the
   set containing all elements that appear in all sets of the list) is in \(
   \Sigma \).

To check understanding, let's take a look at our first problem of the power
round.

<div class="black-box" id="problem201">
**Problem 2.0.1.** Which of the following sets are \( \sigma \)-algebras over \( X
= \{ 0, 1, 2, 3 , 4 \} \)?

1. \( \Sigma = \{ \emptyset, X \} \)
2. \( \Sigma = \{ \emptyset, 0, 1, 2, 3, 4, X \} \)
3. \( \Sigma = \{ \emptyset, \) \( \{ 0, 1 \}, \) \( \{ 2, 3, 4 \}, \) \( \{ 0, 1, 2, 3, 4 \} \} \)
4. \( \Sigma = \{ \emptyset, \) \( \{ 0 \}, \) \( \{ 1 \}, \) \( \{ 0, 1 \}, \) \( \{ 1, 2 \}, \) \( \{ 1, 2, 3, 4 \}, \) \( \{ 0, 2, 3, 4 \}, X \} \)
</div>

<details class="solution">
<summary>Solution 2.0.1.</summary>
<div class="solution-contents">

1. Yes. The empty set and its complement, \( X \), are in \( \Sigma \). Their
   intersections and unions are also just either of the sets.
2. No. A \( \sigma \)-algebra should contain only subsets of \( X \). It should not contain elements of \( X \) itself.
3. Yes. One may verify all the rules are satisfied.
4. No. The complement of \( \{ 1, 2 \} \) is \( \{0, 3, 4 \} \), but this isn't
   in \( \Sigma \).

</div>
</details>

This certainly doesn't feel conducive to measuring volumes, and it's certainly
esoteric on first glance. Indeed, as with many things in pure mathematics,
we're trading off the confusion of working backwards from intuition with the
promise of rigour and consistency. Before we get into the "why" of \( \sigma
\)-algebras, let's first take a look at the definition of a measure so their
interplay can help us better understand what's going on.

**Definition.** We call a function \( \mu : \Sigma \to \mathbb{R} \cup \{
\infty \} \) a **measure** over a \( \sigma \)-algebra \( \Sigma \) if

1. \( \mu(\emptyset) = 0 \)
2. \( \mu(E) \ge 0 \) for all \( E \in \Sigma \)
3. For any set \( \{ E_i \}_{i = 1}^\infty \subset \Sigma \) of *disjoint* sets,
\[
\mu \left( \bigcup_{i = 1}^\infty E_i \right) = \sum_{i = 1}^\infty
\mu(E_i)
.\]

This definition much better codifies how we intuitively view volumes. Condition
1 tells us that empty sets should have \( 0 \) volume. Condition 2 tells us that
volumes can't be negative. Condition 3 tells us that the volume of a set is the
sum of the volumes of its smaller pieces. It should
be noted that there are many different ways of defining valid measures on sets.
This definition merely tells us what conditions a function should obey for it to
be considered a part of the class of functions called a measure.

The reason why we work over a \( \sigma \)-algebra (in particular we assume to
be working with the [Borel algebra](https://en.wikipedia.org/wiki/Borel_set) over \( \mathbb{R}^n \))
is because assigning measure values to every single subset of \( \mathbb{R}^n \)
either ends up with the measure being equivalently \( 0 \) or just blowing up to
infinity all the time. See more discussion
[here](https://stats.stackexchange.com/questions/199280/why-do-we-need-sigma-algebras-to-define-probability-spaces). For the contest, it suffices to take this at face value, although I do recommend the curious reader to go more in depth.

Combining together a set, a \( \sigma \)-algebra over that set, and a measure
over the \( \sigma \)-algebra gives a measure space.

The next few problems concern themselves with examples and useful properties of
measures that are referenced in later problems.

<div class="black-box" id="problem202">
**Problem 2.0.2.** Let \( X \) be any set and \( \Sigma = \mathcal{P}(X) \).
Let \( \mu : \Sigma \to \mathbb{R} \cup \{ \infty \} \) be defined as \( \mu(A)
= \#A \), the cardinality of \( A \) if \( A \subset X \) is finite and \(
\infty \) if \( A \) is infinite.

1. Verify that \( \Sigma \) forms a \( \sigma \)-algebra over \( X \).
2. Verify that \( \mu \) forms a measure over \( (X, \Sigma) \).

This is called the **counting measure**.
</div>

<details class="solution">
<summary>Solution 2.0.2.</summary>
<div class="solution-contents">

These follow straightforwardly from the definitions. The below solution is a
bit verbose, but this is intentional to avoid fallacies (or just a lack of rigour) arising from improperly
handling infinites.

1. Clearly \( \Sigma \) contains the empty set and is closed under complements,
countable unions, and countable intersections, as it is the power set of \( X \)
containing all possible sets.
2. For the first condition, \( \mu(\emptyset) = \# \emptyset = 0 \). For the
second condition, observe that set cardinalities are always strictly
non-negative, so this is satisfied. For the third condition, observe that by
the principle of inclusion exclusion,
\begin{align*}
    \mu \left( \bigcup_{i = 1}^\infty E_i \right) &= \lim_{n \to \infty} \mu \left( \bigcup_{i = 1}^n E_i \right) \\
    &= \lim_{n \to \infty} \# \left( \bigcup_{i = 1}^n E_i \right)  \\
    &= \lim_{n \to \infty} \sum_{\emptyset \ne I \subset \{ 1, 2, \ldots, n \}} (-1)^{\#I + 1} \cdot \# \left( \bigcap_{i \in I} E_i \right),
\end{align*}
but since \( E_i \cap E_j = \emptyset \) for \( i \ne j \), terms with \( \# I > 1 \) vanish. Thus, the expression is equal to
\begin{align*}
    \lim_{n \to \infty} \sum_{i = 1}^n \# E_i &= \lim_{n \to \infty} \sum_{i = 1}^n \mu(E_i) \\
    &= \sum_{i = 1}^\infty \mu(E_i).
\end{align*}

</div>
</details>

<div class="black-box" id="problem203">
**Problem 2.0.3.** Verify that in a measure space \( (X, \Sigma, \mu) \) with
\( A, B \in \Sigma \), if \( A \subset B \) then \( \mu(A) \le \mu(B) \).
</div>

<details class="solution">
<summary>Solution 2.0.3.</summary>
<div class="solution-contents">

Observe that \( \mu(B) = \mu(A \cup (B \setminus A)) = \mu(A) + \mu(B \setminus A) \), since \( A \) and \( B \setminus A \) are disjoint. But since measures are strictly non-negative, this gives us that \( \mu(A) \le \mu(B) \).

</div>
</details>

<div class="black-box" id="problem204">
**Problem 2.0.4.** Let \( (X, \Sigma, \mu) \) a measure space. Show that for
any countable \( \{ E_i \}_{i = 1}^\infty \subset \Sigma \),
\[
    \mu \left( \bigcup_{i = 1}^\infty E_i \right) \le \sum_{i = 1}^\infty \mu(E_i)
.\]
This is called **countable subadditivity**.
</div>

<details class="solution">
<summary>Solution 2.0.4.</summary>
<div class="solution-contents">

Define \( A_1 := E_1 \), \( A_i := E_i \setminus \bigcup_{k = 1}^{i - 1} E_k \) so that each \( A_i \) is mutually disjoint. In addition, notice that \( A_i \subset E_i \) so that, by the previous problem, \( \mu(A_i) \le \mu(E_i) \). Observe that
\begin{align*}
    \mu \left( \bigcup_{i = 1}^{\infty} E_i \right) &= \mu \left( \bigcup_{i = 1}^{\infty} A_i \right) \\
    &= \sum_{i = 1}^{\infty} \mu(A_i) \\
    &\le \sum_{i = 1}^{\infty} \mu(E_i)
.\end{align*}

</div>
</details>

<div class="black-box" id="problem205">
**Problem 2.0.5.** Let \( X \) be any set and \( \Sigma = \mathcal{P}(x) \). Let \( x_0 \in X \) be a designated point in \( X \). Now, define \( \mu : \Sigma \to \overline{\mathbb{R}} \) so that \( \mu(A) = 1 \) if \( x_0 \in A \), and \( \mu(A) = 0 \) otherwise. Is \( (X, \Sigma, \mu) \) a measure space?
</div>

<details class="solution">
<summary>Solution 2.0.5.</summary>
<div class="solution-contents">

Yes, \( (X, \Sigma, \mu) \) is a valid measure space. Note that we've already proven \( \Sigma \) to be a valid \( \sigma \)-algebra in Problem 2.0.2, so it suffices to prove that \( \mu \) is a valid measure, considering each condition of the definition of a measure:

1. Clearly \( \mu(\emptyset) = 0 \), as \( x_0 \not\in \emptyset \).
2. The range of \( \mu \) is \( \{0, 1 \} \) by definition, so it is nonnegative.
3. Let \( E = \bigcup_{i = 1}^\infty E_i \). We shall consider two cases (1) when \( x_0 \in E \) and (2) when \( x_0 \not\in E \).

    For the first case, observe that if \( x_0 \in E \) then \( \mu(E) = 1 \) by definition. Further, if \( x_0 \in E \) and each \( E_i \) is disjoint, there must be a unique \( k \) where \( x_0 \in E_k \). Then,
    \[
        \sum_{i = 1}^\infty \mu(E_i) = \sum_{i = 1}^\infty \mathbf{1} \{ i = k \} = 1
    .\]
    Thus, countable additivity is satisfied for this case.

    For the second case, observe that \( \mu(E) = 0 \) by definition. In addition, if \( x_0 \not\in E \), then \( x_0 \not\in E_i \) for all \( i \). This implies that,
    \[
        \sum_{i = 1}^\infty \mu(E_i) = \sum_{i = 1}^\infty 0 = 0
    ,\]
    so countable additivity holds for this case as well.

</div>
</details>

## The Hausdorff Measure

Now that we've established what a measure is and some of its general
properties, we can hone in closer on the Hausdorff measure, a particular
measure that gives us a way to quantifying dimensions and volume. To get to
volumes, we'll first start from something that we are very familiar with in
higher dimensions: distance.

**Definition.** We shall the say the **diameter** of a set \( S \subset
\mathbb{R}^n \) is defined as
\[
    |S| := \sup_{x, y \in S} |x - y|
.\]

In other words, the longest possible length across all segments in the set is
the diameter. The absolute value signs denote the usual Euclidean norm in \( n
\) dimensions. Combining this diameter with set unions allows us to create a
controllably precise covering of any set.

**Definition.** We call a **\( \delta \)-cover** of a set \( S \subset
\mathbb{R}^n \) for \( \delta > 0 \) to be a collection of sets \( \{ U_i \}_i
\) such that

1. \( F \subset \bigcup_i U_i \). In other words, the collection of sets must
   cover \( F \) (and it can cover points outside of \( F \)).
2. \( |U_i| < \delta \) for each \( i \). Indeed, \( \delta \) is the parameter
   of the delta covers and allows one to control how big each covering set is
   inside the \( \delta \)-cover.

To check understanding, consider the following problem:

<div class="black-box" id="problem212">
**Problem 2.1.2.** Which of the following are \( \delta \)-covers of \( [0, 1]
\) for \( \delta = \frac{1}{2} \)?

1. \( \{ (-\frac{1}{3}, \frac{1}{3}), (\frac{1}{3}, \frac{2}{3}), (\frac{2}{3}, \frac{4}{3}) \} \)
2. \( \{ [0, \frac{1}{n}] : n \in \mathbb{N} \} \)
3. \( \{ [0, \frac{1}{2}], [\frac{1}{2}, 1] \} \)
</div>

<details class="solution">
<summary>Solution 2.1.2.</summary>
<div class="solution-contents">

1. No; \( |(-\frac{1}{3}, \frac{1}{3})| = \frac{2}{3} > \frac{1}{2} = \delta \).
2. No; \( U_1 = [0, 1] \), and \( |[0, 1]| = 1 > \frac{1}{2} = \delta \).
3. No; \( |[\frac{1}{2},1]| = \frac{1}{2} \not< \delta \).

</div>
</details>

With this, we can finally define the Hausdorff measure.

**Definition.** We define the **outer \( s \)-dimensional Hausdorff measure**
of a set \( S \) as
\[
    \mathcal{H}^s_\delta (S) := \inf \left\{ \sum_{i = 1}^\infty |U_i|^s :
    \{U_i \}_i \text{ is a } \delta \text{-cover of } S \right\}
,\]
where the infimum is taken over all \( \delta \)-covers of \( S \).

Before we fully dive into what this is exactly saying, we'll go through some
problems to glean important characteristics of the Hausdorff measure. We will
briefly mention, though, that intuitively this should be close to a notion of
\( s \)-dimensional volume. Thinking in terms of units, a set with dimension \(
s \) should have volume with units of length to the \( s \) power. In addition,
the infima across \( \delta \)-covers makes it so that we are measuring the
volume of the most accurate, refined covering of the set.

Using the below problem, we can refine this further to only consider all \(
\delta \)-covers where each element is open and convex.

<div class="black-box" id="problem211">
**Problem 2.1.1.** For any set \( E \) and any \( \varepsilon > 0 \), show that
there exists a convex, open set \( U \supset E \) such that \( |U| \le |E| +
\varepsilon \).
</div>

<details class="solution">
<summary>Solution 2.1.1.</summary>
<div class="solution-contents">

We shall firstly prove the following very useful lemma:

**Lemma.** Fix points \( x, y, z \in \mathbb{R}^n \) and let \( p(t) = tx + (1 - t)y\), where \( p : [0,1] \to \mathbb{R}^n \). Then,
\[
    |z - p(t)| \le \max \{ |z - x|, |z - y| \}
.\]

*Proof.* There exists a unique plane passing through \( x, y, z \). Thus, we have an analogous problem in geometry that, given a segment \( AB \) and a point \( P \), we must show that for any point \( C \) on segment \( AB \), \( PC \le \max\{ PA, PB \} \), but this is immediately obvious, as either \( A \) or \( B \) is farther away than \( C \) from the altitude (the segment with the shortest length). \( \blacksquare \)

Next, let's construct the convex hull of \( E \). Namely, let
\[
    H := \{ tx + (1 - t) y \mid t \in [0, 1], x, y \in E \}
.\]
With this, we have the following claim:

**Claim.** \( |H| = |E| \).

*Proof.* From the definition of diameter, we can split the supremum into three cases as follows:
\begin{align*}
    |H| &= \sup_{x, y \in H} |x - y| \\
    &= \max \{ \sup_{x, y \in E} |x - y|, \sup_{x \in E, y \in H \setminus E} |x - y|, \sup_{x, y \in H \setminus E} |x - y| \}
.\end{align*}
It suffices to prove that the last two suprema are bounded above by the first (which is \( |E| \)) to show that \( |H| = |E| \).

Case \( x \in E, y \in H \setminus E \): Because \( y \in H \setminus E \), there must exist points \( a, b \in E \) such that for some \( t \in [0, 1] \), \( y = ta + (1-t) b \). By our above lemma, \( |x - y| \le \max\{ |x - a|, |x - b| \} \), so if we take WLOG \( a \) to be the furthest endpoint then we have that \( |x-y| \le |x - a| \). Because we can find such an \( a \in E \) for all \( x \in E, y \in H \setminus E \), we must have that
\[
    \sup_{x \in E, y \in H \setminus E} |x - y| \le \sup_{x, y \in E} |x - y|
.\]

Case \( x, y \in H \setminus E \): We proceed similarly. There must exist points \( a, b, c, d \in E \) where for some \( s, t \in [0, 1] \) we have \( x = cs + (1 - s)d, y = at + (1 - t)b\). Applying the above lemma, we can say WLOG that \( |x - y| \le |x - a| \) and again WLOG \( |x - a| \le |c - a| \). Since, we can always find such \( a, c \in E \), we must have
\[
    \sup_{x, y \in H \setminus E} |x - y| \le \sup_{x, y \in E} |x - y|
.\]

Thus,
\[
    |H| = \sup_{x, y \in E} |x - y| = |E|
,\]
which concludes our proof. \( \blacksquare \)

From here, define \( U \) as
\[
    U := \bigcup_{x \in H} B_x (r)
,\]
where \( r \) is some fixed radius we shall determine later. Clearly, as \( U \) is the union of an arbitrary number of open balls, \( U \) is ensured to be open and convex.

Now, notice that
\[
    |U| = \sup_{x, y \in H, |z_1| = |z_2| = r} | x - y + z_1 + z_2 |
,\]
and by the triangle inequality
\begin{align*}
    \sup_{x, y \in H, |z_1| = |z_2| = r} | x - y + z_1 + z_2 | &\le \sup_{x, y \in H} |x - y| + |z_1| + |z_2| \\
    &= |H| + 2r \\
    & = |E| + 2r
.\end{align*}
Thus, if we're given any fixed \( \varepsilon > 0 \), we can choose \( r = \varepsilon / 4 \) and obtain an open, convex set \( U \) of sufficiently small diameter.

</div>
</details>

Of course, this measure is dependent on the parameter \( \delta \) controlling
the covers of \( S \). We mentioned earlier that we want to refine our covers,
so what happens to the measure when we are varying \( \delta \)? This leads to
the following problem:

<div class="black-box" id="problem213">
**Problem 2.1.3.** Let \( 0 < \delta_1 < \delta_2 \). Show that
\[
    \mathcal{H}^s_{\delta_1} (F) \ge \mathcal{H}^s_{\delta_2} (F)
.\]
</div>

<details class="solution">
<summary>Solution 2.1.3.</summary>
<div class="solution-contents">

For convenience, denote
\[
    C_\delta := \left\{ \sum_{i  = 1}^\infty |U_i|^s : \{ U_i \}_i \textrm{ is a } \delta \textrm{-cover of } F \right\}
,\]
so that we wish to prove
\[
    \inf C_{\delta_1} \ge \inf C_{\delta_2}
.\]
In addition, notice that any \( \delta_1 \)-cover of \( F \) is also a \( \delta_2 \)-cover of \( F \); both assuredly union to a superset of \( F \) and each \( U_i \) has \( |U_i| < \delta_1 < \delta_2 \).

Following this line of reason, we must have that \( C_{\delta_1} \subset C_{\delta_2} \), implying \( \inf C_{\delta_1} \ge \inf C_{\delta_2} \), which is what we wished to prove.

</div>
</details>

In other words, as we take \( \delta \) closer to \( 0 \), the measure
monotonically increases. This leads to a well defined, but not necessary finite
limit.

**Definition.** We define the **\( s \)-dimensional Hausdorff measure** of a
set \( S \) to be
\[
    \mathcal{H}^s (S) = \lim_{\delta \to 0^+} \mathcal{H}^s_\delta (S)
.\]

Of course, we should probably show that this is an actual measure. Note in
the below problem that we are only asked to prove subadditivity (as
defined in [Problem 2.0.4](#problem204)) as opposed to
addivity. Proving full addivitity is harder and outside the scope of the
contest (but it is possible).

<div class="black-box" id="problem214">
**Problem 2.1.4.** Prove the following:

1. \( \mathcal{H}^s (E) \ge 0 \) for all \( E \subset \mathbb{R}^n \).
2. \( \mathcal{H}^s (\emptyset) = 0 \).
3. Countable subaddivity (see [Problem 2.0.4](#problem204)) for \(
   \mathcal{H}^s \).
</div>

<details class="solution">
<summary>Solution 2.1.4.</summary>
<div class="solution-contents">

1. The diameter of a set is strictly nonnegative. Since the Hausdorff measure is a sum of powers of diameters, it also must be strictly nonnegative.
2. Observe that \( \emptyset \) is always a \( \delta \)-cover for \( \emptyset \), independent of \( \delta \). The value for the measure using this \( \delta \)-cover is \( 0 \), but since the measure is strictly nonnegative, this must be the infimum value, so \( \mathcal{H}^s_{\delta} (\emptyset) = 0 \). Taking \( \delta \to 0^+\), we get that \( \mathcal{H}^s (\emptyset) = 0 \).
3. We wish to show that for any fixed \( \delta > 0 \),
\[
    \mathcal{H}^s_\delta \left( \bigcup_{i = 1}^\infty E_i \right) \le \sum_{i = 1}^\infty \mathcal{H}^s _\delta (E_i)
.\]
Suppose the infima \( \delta \)-covers for each \( E_i \) are given by \( \{ U_{ij} \}_{j = 1}^\infty \), so that
\[
    \sum_{i = 1}^\infty \mathcal{H}^s_\delta (E_i) = \sum_{i = 1}^\infty \sum_{j = 1}^\infty |U_{ij}|^s
.\]
Observe, however, that \( \{ U_{ij} \}_{i,j = 1}^\infty \) is also a \( \delta \)-cover for \( \bigcup_i E_i\), since
\[
    \bigcup_{i = 1}^\infty E_i \subset \bigcup_{i = 1}^\infty \bigcup_{j = 1}^\infty U_{ij}
,\]
and each \( |U_{ij}| < \delta \). Because it is a valid \( \delta \)-cover,
\[
    \mathcal{H}^s_\delta \left( \bigcup_{i = 1}^\infty E_i \right) \le \sum_{i = 1}^\infty \sum_{j = 1}^\infty |U_{ij}|^s = \sum_{i = 1}^\infty \mathcal{H}^s_\delta(E_i)
,\]
and taking \( \delta \to 0^+ \) gives
\[
   \mathcal{H}^s \left( \bigcup_{i = 1}^\infty E_i \right) \le \sum_{i = 1}^\infty \mathcal{H}^s (E_i)
,\]
which is what we wished to show.
</div>
</details>

There are also some very intuitive volume-like properties to the Hausdorff
measure:

<div class="black-box" id="problem215">
**Problem 2.1.5.** Let \( E \subset \mathbb{R}^n \) and \( 0 < c \in \mathbb{R}
\). Then, let \( E' \) be \( E \) scaled by \( c \), that is, \( E' := \{ cx
: x \in E \} \). Show that for all \( s \),
\[
    \mathcal{H}^s (E') = c^s \mathcal{H}^s(E)
.\]

</div>

<details class="solution">
<summary>Solution 2.1.5.</summary>
<div class="solution-contents">

Observe that there is a bijection between the \( \delta \)-covers of \( E \) and
the \( c\delta \)-covers of \( E' \). For every \( \delta \)-cover \( \{ U_i
\}_i \) of \( E \), we recover a unique, valid \( c\delta \)-cover \( \{ U'_i
\}_i \), where
\[
    U'_i = \{ cu : u \in U_i \}
.\]
We also have an inverse mapping (take \( U'_i \) to \( U_i \) by scaling down by
\( c \)), so this is bijective. We can prove that the diameter of each \( U'_i
\) is valid, as
\begin{align*}
    |U'_i| &= \sup_{a, b \in U'_i} |a - b| \\
    &= \sup_{a, b \in U_i} |ca - cb| \\
    &= c\sup_{a, b \in U_i} |a - b| \\
    &= c|U_i| < c \delta
.\end{align*}
Mapping each \( U_i \) to \( U'_i \) gives us that \( \mathcal{H}^s_{c \delta}
(E') \le c^s \mathcal{H}^s_\delta (E) \), and the inverse mapping gives \(
\mathcal{H}^s_\delta (E) \le c^{-s} \mathcal{H}^s_{c \delta} (E') \). Combining
these gives \( \mathcal{H}^s_{c \delta} (E') = c^s \mathcal{H}^s_\delta (E) \),
and taking the limit as \( \delta \to 0^+ \) gives \( \mathcal{H}^s (E') = c^s
\mathcal{H}^s(E) \).

</div>
</details>

<div class="black-box" id="problem216">
**Problem 2.1.6.** Let \( E \subset \mathbb{R}^n \) and \( x \in \mathbb{R}^n \). Let \( E' = E + x = \{ e + x : e \in E \} \). Show that for all \( s \), \( \mathcal{H}^s (E) = \mathcal{H}^s (E') \).
</div>

<details class="solution">
<summary>Solution 2.1.6.</summary>
<div class="solution-contents">

Observe that there is a bijection between the \( \delta \)-covers of \( E \) and \( E' \). Namely, if one is given a \( \delta \)-cover \( \{ U_i \}_i \) of \( E \), we recover a unique, valid \( \delta \)-cover \( \{ U'_i \}_i \), where
\[
    U'_i = \{ u + x : u \in U_i \}
.\]
Clearly this mapping is invertible (switch the plus for a minus), so it's also bijective. It is also trivial to show that the diameter of each \( U'_i \) remains the same under shifting, as
\begin{align*}
    |U'_i| &= \sup_{a, b \in U'_i} |a - b| \\
    &= \sup_{a, b \in U_i} |(a + x) - (b + x)| \\
    &= \sup_{a, b \in U_i} |a - b| \\
    &= |U_i|
.\end{align*}
Because there is a mapping from each \( \delta \)-cover of \( E \) to \( E' \), we can tell that \( \mathcal{H}^s_\delta (E') \le \mathcal{H}^s_\delta (E) \), but since map goes the other way as well, we have \( \mathcal{H}^s_\delta (E) \le \mathcal{H}^s_\delta (E') \). This implies that \( \mathcal{H}^s_\delta(E) = \mathcal{H}^s_\delta (E') \), and taking \( \delta \to 0^+ \) gives \( \mathcal{H}^s (E) = \mathcal{H}^s (E') \).

</div>
</details>

Earlier, we explored how the outer measure varied with respect to \( \delta
\), and now we shall explore the \( s \) parameter that has sort of just been
hanging out until now.

<div class="black-box" id="problem217">
**Problem 2.1.7.** For \( 0 < r < s \) and \( E \subset \mathbb{R}^n \), prove the following:

1. \( \mathcal{H}^r (E) \ge \mathcal{H}^s (E) \).
2. If \( \mathcal{H}^r (E) < \infty \), then \( \mathcal{H}^s (E) = 0 \).
</div>

<details class="solution">
<summary>Solution 2.1.7.</summary>
<div class="solution-contents">

1. Take \( 0 < \delta < 1 \) and consider any \( \delta \)-cover of \( E \). Because \( 0 \le |U_i| < \delta \), concavity tells us that \( |U_i|^s \le |U_i|^r \), and thus
    \[
        \sum_{i = 1}^\infty |U_i|^s \le \sum_{i = 1}^\infty |U_i|^r
    \]
    for all \( \delta \)-covers. Thus, \( \mathcal{H}^r_\delta (E) \ge
    \mathcal{H}^s_\delta  (E)\) and taking \( \delta \to 0^+ \) yields \(
    \mathcal{H}^r (E) \ge \mathcal{H}^s (E) \).
2. Suppose \( \{ U_i \}_i \) denotes the infima \( \delta \)-cover (where once
   again \( 0 < \delta < 1 \)) for \( \mathcal{H}^r_\delta (E)\). From Problem
   2.1.3, we know that \( \mathcal{H}^r_\delta(E) \le \mathcal{H}^r(E) \), so \(
   \mathcal{H}^r_\delta(E) \) must be finite.

    Let's now inspect \( \mathcal{H}^s_\delta (E) \) with the same \( \delta
    \)-cover. Observe that
    \begin{align*}
        0 \le \mathcal{H}^s_\delta(E) &= \sum_i |U_i|^s \\
        &\le \delta^{s - r} \sum_i |U_i|^r \\
        &= \delta^{s - r} \mathcal{H}^r_\delta (E)
    .\end{align*}
    Taking the limit on both sides returns
    \[
        0 \le \lim_{\delta \to 0^+} \mathcal{H}^s_\delta(E) \le \lim_{\delta \to 0^+} \delta^{s - r} \mathcal{H}^r_\delta(E) = 0
    ,\]
    so we see that finiteness and \( s - r > 0 \) imply \( \mathcal{H}^s(E) = 0 \).

</div>
</details>

This property tells us that there is a critical value for which the Hausdorff
measure jumps from an infinite value to a finite (potentially nonzero value). In
particular, if we were to fix a set \( U \) and graph \( \mathcal{H}^s (U) \)
while varying \( s \), we would obtain the graph below:

<img src="./diagrams/hausdorffmeasure.svg" />

This leads to the all-important definition:

**Definition.** The value of \( s \) for which \( \mathcal{H}^s (U) \) jumps from infinity to
a finite value is called the **Hausdorff dimension** of \( U \). Formally,
\begin{align*}
    \dim U &:= \sup \{ s : \mathcal{H}^s (U) = \infty \} \\
    &= \inf \{ s : \mathcal{H}^s (U) = 0 \}
.\end{align*}

## Understanding the Hausdorff Measure

Now that we've showed the Hausdorff is well-defined and has some particular
properties, including the very appealing ability to uniquely attribute a
dimension to any subset of \( \mathbb{R}^n \), we're in great shape to start
applying it to fractals. Before we do that, however, we should consider some
examples and work with the measure outside of how the problems guide us to give
us a better intuition of what we've proved and why.

Let's first consider the following: **it is trivial to get upper bounds on the
Hausdorff measure but very hard to get lower bounds**. Indeed, if I give you
any \( \delta \)-cover of a set \( E \), compute the sum of \( s \) powers of
each element, and take \( \delta \to 0^+ \), we cannot say that the Hausdorff
measure is what I've computed. The Hausdorff measure takes the infimum over all
\( \delta \)-covers, meaning that at most I can say the measure is less than or
equal to what I've computed. This tells us an upper bound, but not a lower
bound.

There is one exception to this case, however. If we can prove that \(
\mathcal{H}^s(E) \le 0 \), nonnegativity tells us that \( \mathcal{H}^s(E) \)
must be identically \( 0 \).

Another thing that I found hard to understand during the contest before doing
any concrete examples was how the Hausdorff dimension and the behavior around it
actually arose. So, let's take a concrete example of trying to compute the
Hausdorff measure of \( [0, 1] \).

Consider the \( \delta \)-covering where we
take intervals of length \( \delta / 2 \), resulting in \( 2 / \delta \) total
intervals. Thus,
\[
    \mathcal{H}^s_{\delta} ([0, 1]) \approx \sum_{i = 1}^\infty |U_i|^s = \left( \frac{\delta}{2} \right)^s \cdot \frac{2}{\delta} = C \delta^{s - 1}
,\]
for some constant \( C \). Taking \( \delta \) to be very small, we see that the
measure is infinite for \( s < 1 \) (because then the exponent is negative),
finite for \( s = 1 \), and \( 0 \) for \( s > 1 \). Thus, as we would expect,
the dimension of the interval is \( 1 \). Of course, this isn't rigorous at all
since we haven't proven that our \( \delta \)-cover is the most optimal one, but
the intuition still holds.

Further, we actually can glean something from this argument. Remember when I
said that if we can show an upper bound of \( 0 \), we have a definite value for
the Hausdorff measure? If we take \( s > 1 \), we get exactly this. So, we can
say rigorously that \( \mathcal{H}^s([0, 1]) = 0 \) for \( s > 1 \). This alone
doesn't tell us that \( \dim [0, 1] = 1 \), but it does tell us that \( \dim[0,
1] \le 1 \), which is very useful.

<div class="black-box" id="problem218">
**Problem 2.1.8.** Prove that if \( E \subset \mathbb{R}^n \), then \( \dim E
\le n \).
</div>

<details class="solution">
<summary>Solution 2.1.8.</summary>
<div class="solution-contents">

By [Problem 2.0.3](#problem203), \( E \subset \mathbb{R}^n \) gives us \( \mathcal{H}^s (E) \le \mathcal{H}^s (\mathbb{R}^n) \). We then have the following claim:

**Claim.** For \( s > n \), \( \mathcal{H}^s (\mathbb{R}^n) = 0 \).

Let's first consider \( \mathcal{H}^s_\delta ([-R, R]^n) \) and tile it using \( n \)-dimensional cubes of side length \( \delta / 2 \). By the Pythagorean identity, the cubes have a diameter of \( \delta \sqrt{n} / 2\), computing the measure then yields
\begin{align*}
    \mathcal{H}^s_\delta ([-R, R]^n) &\le \sum_i |U_i|^s \\
    &= \left(\frac{2 R}{\delta / 2} \right)^n \cdot (\delta \sqrt{n} / 2)^s \\
    &= C \delta^{s - n}
,\end{align*}
where \( C \) is constant with respect to \( \delta \).

If we then take the limit as \( \delta \to 0^+ \), we see that
\begin{align*}
    \mathcal{H}^s ([-R, R]^n) &= \lim_{\delta \to 0^+} \mathcal{H}^s_\delta ([-R, R]^n) \\
    &\le \lim_{\delta \to 0^+} C \delta^{s - n} = 0
,\end{align*}
but since measures are nonnegative, \( \mathcal{H}^s ([-R, R]^n) = 0 \). Taking the limit as \( R \to \infty \), we recover that \( \mathcal{H}^s (\mathbb{R}^n) = 0 \). \( \blacksquare \)

Now, denote
\[
    N_A := \{ d \mid \mathcal{H}^d(A) = 0 \}
.\]
Using the above inequality and nonnegativity of measures yields \( 0 \le \mathcal{H}^s (E) \le \mathcal{H}^s (\mathbb{R}^n) \), which tells us that \( \mathcal{H}^s (\mathbb{R}^n) = 0 \implies \mathcal{H}^s (E) = 0 \). Thus, \( N_{\mathbb{R}^n} \subset N_E\). This implies that
\[
    \dim E = \inf N_E \le \inf N_{\mathbb{R}^n} \le n
.\]

</div>
</details>

We remark that the above problem is a special case of \( A \subset B \implies
\dim A \le \dim B \), which should be intuitive.

<div class="black-box" id="problem219">
**Problem 2.1.9.** Prove that \( \mathcal{H}^0 \) is simply the [counting
measure](#problem202).
</div>

<details class="solution">
<summary>Solution 2.1.9.</summary>
<div class="solution-contents">

In other words, we must show that \( \mathcal{H}^0 (E) = \#E \) if \( E \) is finite and \( \mathcal{H}^0 (E) \) is infinite if \( E \) is infinite.

First, let's consider the case when \( E \) is finite. Since \( E \) does not depend on \( \delta \), we can see that each \( U_i \) in our limiting \( \delta \)-cover must be singleton (otherwise we could always choose a small enough \( \delta \) such that the diameter of \( U_i \) would be too large). Thus, if \( E = \{ e_1, e_2, \ldots, e_k \} \), we can take \( U_i = \{ e_i \} \) to obtain a measure of \( \mathcal{H}^0 (E) = k = \# E \).

For the case when \( E \) is infinite, consider that
\[
    \sum_{i} |U_i|^0 \ge \frac{|E|}{\delta}
,\]
so if we take \( \delta \to 0^+ \), the measure \( \mathcal{H}^0 (E) \to \infty \).

</div>
</details>

With this, we're ready to tackle fractals.

## Fractals

The fractals we consider in this section are the [Cantor
set](https://en.wikipedia.org/wiki/Cantor_set), the [Sierpinksi
carpet](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_carpet), the [Minkowski sausage](https://en.wikipedia.org/wiki/Minkowski_sausage) (many a jokes were made about this one), the [Koch
curve](https://en.wikipedia.org/wiki/Koch_snowflake), and the [Sierpinksi triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle).

What exactly do we mean when we talk of a fractal? Intuitively, a fractal is a
set of points that is self-similar when we take copies, scale the copies down,
translate them, and glue them together in some way. We make this intuition
concrete with the idea of contractions and iterated function systems (IFSs).

**Definition.** A function \( f : \mathbb{R}^n \to \mathbb{R}^n \) is called a
**contraction** if there exists some constant \( 0 < c < 1 \) such that for
every \( x, y \in \mathbb{R}^n \), \( |f(x) - f(y)| = c|x - y| \). The value \( c \) is called the **contraction ratio** for \( f \).

Contractions take any set and make lengths between points less, shifting the
points closer to eachother. This definition takes care of the scaling and
translating part of fractals. The next definition handles the multiple copies
part:

**Definition.** An **iterated function system** (**IFS**) is a finite set of
contractions \( (f_1, f_2, \ldots, f_m) \), where \( m \ge 2 \).

Each function has the same domain and codomain, but they can have differing
contraction ratios.

<div class="black-box" id="problem401">
**Problem 4.0.1.** Let \( f \) be a contraction in \( \mathbb{R}^n \). Denote \( f^{(k)} \) to be \( f \) composed with itself \( k \) times.

1. Show that for any \( x, y \in \mathbb{R}^n \) and any \( \varepsilon > 0 \),
   there exists some \( k \) such that \( |f^{(k)}(x) - f^{(k)}(y)| <
   \varepsilon \).
2. Show that if one replaces the contraction assumption with the weaker \( |f(x)
   - f(y)| < |x - y| \) for \( x \ne y \), then there exists such functions with
   no fixed points (that is, no \( x \) such that \( f(x) = x \)).
</div>

<details class="solution">
<summary>Solution 4.0.1.</summary>
<div class="solution-contents">

1. First, we have the following claim:

    **Claim.** \( |f^{(k)} (x) - f^{(k)} (y) | = c^k |x - y|\).

    *Proof.* We will proceed by using induction. Obviously, the base case for when \( k = 1 \) is equivalent to the contraction condition on \( f(x) \).

    Now, by our induction hypothesis, suppose that \( |f^{(m - 1)} (x) - f^{(m - 1)} (y) | = c^{m - 1} |x - y| \). Notice that, by contraction,
    \begin{align*}
        |f^{(m)} (x) - f^{(m)} (y) | &= |f(f^{(m - 1)} (x)) - f(f^{(m - 1)} (y))| \\
        &= c |f^{(m - 1)} (x) - f^{(m - 1)} (y) |
    .\end{align*}
    But because of our induction hypothesis, we have
    \begin{align*}
        c |f^{(m - 1)} (x) - f^{(m - 1)} (y) | &= c \cdot c^{m - 1} |x - y| \\
        &= c^m |x - y|
    .\end{align*}
    Thus, induction holds. \( \blacksquare \)

    Now, for any fixed \( x, y \in \mathbb{R}^n \) and \( \varepsilon > 0 \), it suffices to choose a \( k \) such that (if \( x = y \) then the statement is trivially true, so we shall ignore this case)
    \[
        c^k < \frac{\varepsilon}{|x -y|}
    ,\]
    which is equivalent to \( k > \log \left( \frac{\varepsilon}{|x - y|} \right) / \log{c}\), which is valid because \( 0 < c < 1 \).
        
2. We claim that an example of such a function is \( f(x) = \sqrt{x^2 + 1} \), where \( f : \mathbb{R} \to \mathbb{R} \). First, we shall verify that this function satisfies weak contraction.

    **Claim.** For \( x \ne y \),
    \[
        |\sqrt{x^2 + 1} - \sqrt{y^2 + 1}| < |x - y|
    .\]

    *Proof.* Squaring both sides, doing some algebra, and squaring again yields
    \begin{align*}
        x^2 + 1 + y^2 + 1 - 2\sqrt{(x^2 + 1)(y^2 + 1)} &< x^2 + y^2 - 2xy \\
        2 - 2 \sqrt{(x^2 + 1)(y^2 + 1)} &< -2xy \\
        (x^2 + 1)(y^2 + 1) &> (xy + 1)^2
    .\end{align*}
    But, \( (x^2 + 1)(y^2 + 1) - (xy + 1)^2 = (x - y)^2 \), which is strictly greater than \( 0 \) for \( x \ne y \), so our function satisfies the weak contraction condition. \( \blacksquare \)

    Now, we must prove that \( f(x) \) has no fixed point. This is equivalent to the \( f(x) - x = 0 \) having no real solution. Clearly \( f(x) > 0 \) for \( x < 0 \) (and thus \( f(x) - x > 0 \)), so we are left to consider when \( x > 0 \). Observe, however, in this case that \( \sqrt{x^2 + 1} > \sqrt{x^2} = x \), so there cannot be a solution when \( x > 0 \). Thus, \( f(x) \) has no fixed point.

</div>
</details>

The below problem deals with showing that contractions preserve compactness,
which is rather useful theoretically for verifying certain properties, although
I won't go into it here because it's not really important for understanding, and
I don't believe I could do the topology proper justice.

<div class="black-box" id="problem402">
**Problem 4.0.2.** If \( f \) is a contraction and \( K \) is compact, show that
\( f(K) \) is compact.
</div>

<details class="solution">
<summary>Solution 4.0.2.</summary>
<div class="solution-contents">

By the definition of compactness, we shall show that \( f(K) \) is (1) bounded and (2) closed.

1. We're given that \( K \) is bounded, so there equivalently must exist a radius \( R > 0 \) such that \( |x| \le R \) for all \( x \in K \). It then suffices to find a new radius \( R' \) such that \( |f(x)| \le R' \) for \( x \in K \).

    Observe by the triangle inequality and the contraction condition that \( |f(x)| \le |f(x) - f(0)| + |f(0)| = c|x| + |f(0)| \). Since \( |x| \le R \), we can choose \( R' = cR + |f(0)| < \infty \) to see that \( f(x) \le R' \) for all \( x \in K \). Thus, \( f(K) \) is bounded.
2. Equivalently, we shall show that \( f(K)^c \) is open. To bridge across the proof, we have the following claim:

    **Claim.** \( f(K^c) = f(K)^c \).

    *Proof.* In other words, we must have that \( f(x) \in f(K) \implies x \in K \). This would be true if \( f \) were injective, so we shall prove as such.

    Observe that \( f(x) = f(y) \) implies by contraction \( |f(x) - f(y)| = 0 = c|x - y| \), which is equivalent to \( x = y \). Thus, \( f \) is injective, so \( f(K^c) = f(K)^c \). \( \blacksquare \)

    Because \( K \) is closed, \( K^c \) must be open. Because \( K^c \) is open, we can write it as the union of open balls, so
    \begin{align*}
        f(K^c) &= f \left( \bigcup_{\alpha \in K^c}  B_\alpha (r(\alpha)) \right) \\
        &= \bigcup_{\alpha \in K^c} f(B_\alpha (r(\alpha))) \\
        &= \bigcup_{\alpha \in K^c} B_{f(\alpha)} (c r(\alpha))
    ,\end{align*}
    where \( c \) is the ratio of \( f \), and \( r \) is some function of \( \alpha \) for the radius of each ball. Clearly, then \( f(K^c) = f(K)^c \) is open, being the union of an arbitrary number of open balls, which means that \( f(K) \) is closed.

</div>
</details>

IFSs are important because they allow us to uniquely characterize the set of
points in a fractal without having to explicitly define such set. In particular:

**Definition.** We denote an **attractor** of an IFS \( (f_1, f_2, \ldots, f_m) \) to be a set such that
\[
    D = \bigcup_{i = 1}^m f_i(D)
,\]
where each \( f_i(D) \) is not necessarily pairwise disjoint under intersection.

Notice the wording: "*an*" attractor. The following theorem given to us,
however, allows us to change this wording.

**Theorem.** Every IFS \( (f_1, f_2, \ldots, f_m) \) corresponds to unique,
non-empty, compact attractor set \( F \).

<div class="black-box" id="problem403">
**Problem 4.0.3.** Prove the uniqueness of the above theorem. That is, prove
that if \( F_1 \) and \( F_2 \) are attractors of \( (f_1, f_2, \ldots, f_m) \),
then \( F_1 = F_2 \)
</div>

<details class="solution">
<summary>Solution 4.0.3. (TODO)</summary>
<div class="solution-contents">

Unfortunately, we didn't actually get a good proof of this in contest.

</div>
</details>

We may go between the IFS and the attractor governed by the IFS as we see fit;
they correspond uniquely to one another and each exist. It should be no surprise
that this attractor is precisely the formalization of the fractal that we're
looking for.

The example IFS given for the Cantor set is perhaps illuminating to look at. The
Cantor set is precisely the attractor of \( (f_1, f_2) \), where
\begin{align*}
    f_1(x) &= \frac{1}{3} x \\
    f_2(x) &= \frac{1}{3} x + \frac{2}{3}
.\end{align*}

<div class="black-box" id="problem404">
**Problem 4.0.4.** For each of the following fractals, find an IFS whose
attractor is that fractal and explain why it is the attractor.

1. The Sierpinski carpet
2. The Koch curve
3. The Minkowski sausage
</div>

<details class="solution">
<summary>Solution 4.0.4.</summary>
<div class="solution-contents">

\[
    \gdef\ScaleMatrix#1{
    \begin{bmatrix}
        #1 & 0 \\
        0 & #1 \\
    \end{bmatrix}
    }
    \gdef\RotationMatrix#1{
        \begin{bmatrix}
            \cos(#1^\circ) & -\sin(#1^\circ) \\
            \sin(#1^\circ) & \cos(#1^\circ) \\
        \end{bmatrix}
    }
\]

1. **The Sierpinski Carpet.** Let \( a_1, a_2, \ldots, a_8 = (0, 0) \), \( (\frac{1}{9}, 0) \), \( (\frac{2}{9}, 0) \), \( (\frac{2}{9}, \frac{1}{9}) \), \( (\frac{2}{9}, \frac{2}{9}) \), \( (\frac{1}{9}, \frac{2}{9}) \), \( (0, \frac{2}{9}) \), \( (0, \frac{1}{9}) \). We claim that the IFS is given by
    \[
        f_i (x) = \frac{1}{3}x + a_i
    .\]
    We claim as such because these functions scale down the attractor set (a square with a hollow center) and place square copies in eight squares bordering the center, exactly the geometric shape of the Sierpinski Carpet.

2. **The Koch curve.** We claim that the IFS is given by
    \begin{align*}
        f_1 (x) &= \ScaleMatrix{\frac{1}{3}} x, \\
        f_2(x) &= \ScaleMatrix{\frac{1}{3}} \RotationMatrix{60} x + \left(\frac{1}{3}, 0 \right), \\
        f_3(x) &= \ScaleMatrix{\frac{1}{3}} \RotationMatrix{-60} x + \left( \frac{1}{2}, \frac{\sqrt{3}}{6} \right), \\
        f_4(x) &= \ScaleMatrix{\frac{1}{3}} x + \left( \frac{2}{3}, 0 \right)
    .\end{align*}
    There are four segments to the pattern of the Koch curve, and each segment is a third of the length of the original segment (hence the scaling matrix). In addition, \( f_2 \) and \( f_3 \) feature \( 60^\circ \) counterclockwise and clockwise rotations for the rotated segments.

    We also make a small note that each \( f_i \) is indeed a contraction as they satisfy
    \[
        |f_i(x) - f_i(y)| = \sqrt{\left| \det \ScaleMatrix{\frac{1}{3}} \right|} |x - y| = \frac{1}{3} |x - y|
    .\]

3. **The Minkowski sausage.** We claim that the IFS is given by
    \begin{align*}
        f_1(x) &= \ScaleMatrix{\frac{1}{4}} x, \\
        f_2(x) &= \ScaleMatrix{\frac{1}{4}} \RotationMatrix{90} x + \left( \frac{1}{4}, 0 \right), \\
        f_3(x) &= \ScaleMatrix{\frac{1}{4}} x + \left( \frac{1}{4}, \frac{1}{4} \right), \\
        f_4(x) &= \ScaleMatrix{\frac{1}{4}} \RotationMatrix{-90} x + \left( \frac{1}{2}, \frac{1}{4} \right), \\
        f_5(x) &= \ScaleMatrix{\frac{1}{4}} \RotationMatrix{-90} x + \left(\frac{1}{2}, 0 \right), \\
        f_6(x) &= \ScaleMatrix{\frac{1}{4}} x + \left( \frac{1}{2}, -\frac{1}{4} \right), \\
        f_7(x) &= \ScaleMatrix{\frac{1}{4}} \RotationMatrix{90} x + \left( \frac{3}{4}, - \frac{1}{4} \right), \\
        f_8(x) &= \ScaleMatrix{\frac{1}{4}} + \left( \frac{3}{4}, 0 \right)
    \end{align*}
    This follows directly from the diagram given in Figure 2. We also note that each \( f_i \) is a contraction, as we have
    \[
        |f_i(x) - f_i(y)| = \sqrt{\left| \det \ScaleMatrix{\frac{1}{4}} \right|} |x - y| = \frac{1}{4} |x - y|
    .\]

</div>
</details>

Now that we've found a way to formalize our fractals, we can actually use the
tools we've developed before to get a better understanding of them.
Specifically, the contest gives us a very useful tool for computing the
dimension of the fractals. Firstly, consider the following definition:

**Definition.** An IFS \( (f_1, f_2, \ldots, f_m) \) satisfies the **open set
condition** (**OSC**) if there exists a bounded, non-empty open set \( U \subset
\mathbb{R}^n \) such that for each \( i \ne j \),
\[
    f_i(U) \cap f_j(U) = \emptyset
\]
and
\[
    U \supset \bigcup_{i = 1}^m f_i(U)
.\]

We are then given the following theorem:

**Theorem.** Let \( (f_1, f_2, \ldots, f_m) \) be an IFS satisfying the OSC, and
let each \( c_i  \) denote the contraction ratio of each \( f_i \). Then the
unique real number \( s \) such that
\[
    \sum_{i = 1}^{m} c_i^s = 1
\]
is the Hausdorff dimension of the attractor for the IFS.

Intuitively, this makes sense when viewed from a sort of conservation of
Hausdorff measure. We can split the fractal \( U \) into each \( f_i(U) \)
component, of which the set is scaled by \( c_i^s \). Invoking [Problem
2.1.5](#problem215) and asserting that measures of each component must add up to
their whole, we get this condition. Although not every IFS satisfies the OSC,
this is extremely useful for finding the Hausdorff dimensions of attractors
whose IFSs do satisfy the OSC.

<div class="black-box" id="problem411">
**Problem 4.1.1.** Let \( f_1, f_2, f_3 : \mathbb{R}^2 \to \mathbb{R}^2 \) be
defined as
\begin{align*}
    f_1(x) &= \frac{1}{2} x \\
    f_2(x) &= \frac{1}{2} x + \left( \frac{1}{2}, 0 \right) \\
    f_3(x) &= \frac{1}{2} x + \left( \frac{1}{4}, \frac{\sqrt{3}}{4} \right)
.\end{align*}
Show that this IFS satisfies the open set condition, and calculate its Hausdorff
dimension with proof.
</div>

<details class="solution">
<summary>Solution 4.1.1.</summary>
<div class="solution-contents">

We claim that the set \( U \) of all points contained within (but not on the boundary) of the equilateral triangle of side length \( 1 \) with vertices \( (0, 0), (\frac{1}{2}, \frac{\sqrt{3}}{2}), (1, 0) \) is a set for which this IFS satisfies the open set condition.

Note that \( U \) is trivially non-empty and is open by construction due to not containing the boundary. In addition, \( U \) is bounded, which one can show by taking a ball of radius \( 1 \) or more.

We shall now verify that \( f_1 (U) \cap f_2(U) = f_1(U) \cap f_3(U) = f_2(U) \cap f_3(U) = \emptyset \). Notice that, in order for \( f_i(U) \cap f_j(U) \) to be nonempty for \( i \ne j \), there must exist points \( a, b \in U \) such that \( f_i(a) = f_j(b) \). We shall show no such points exist over all pairs:

- \( f_1 (U) \cap f_2(U) \ne \emptyset \) is equivalent to there being \( a, b \in U \) such that \( a - b = (1, 0) \), but clearly \( 0 < a_x, b_x < 1 \) (note the strict inequalities as \( U \) is open), so this cannot be the case.
- \( f_1 (U) \cap f_3(U) \ne \emptyset \) is equivalent to \( a - b = (\frac{1}{2}, \frac{\sqrt{3}}{2}) \), but this again cannot be the case because \( 0 < a_y, b_y < \frac{\sqrt{3}}{2} \).
- \( f_2(U) \cap f_3(U) \ne \emptyset \) is equivalent to \( a - b = (-\frac{1}{2}, \frac{\sqrt{3}}{2} ) \), but this cannot hold because \( 0 < a_y, b_y < \frac{\sqrt{3}}{2} \) once again.


The fact that \( U \supset f_1(U) \cup f_2(U) \cup f_3(U) \) is also trivial to see geometrically. Since the desired \( U \) exists, the IFS \( (f_1, f_2, f_3) \) satisfies the open set condition.
    
Calculating the Hausdorff dimension is now trivial, as \( |f_i(x) - f_i(y)| = \frac{1}{2} |x - y | \) for \( i = 1, 2, 3 \), so \( c_i = \frac{1}{2} \). Thus by Theorem 4.1.2,
\[
    \frac{3}{2^s} = 1 \implies s = \log(3) / \log(2)
.\]

</div>
</details>

<div class="black-box" id="problem412">
**Problem 4.1.2.** Verify that the Hausdorff dimension of the Cantor set is \( \frac{\log 2}{\log 3} \), and find the Hausdorff dimension of the Koch curve.
</div>

<details class="solution">
<summary>Solution 4.1.2.</summary>
<div class="solution-contents">

To start, we have the following obvious claim:

**Claim.**The Cantor set IFS and Koch curve IFS satisfy the open set condition.

*Proof.* For completeness, we copy the IFS for the Cantor set given and the IFS
for the Koch curve from [Problem 4.0.4](#problem404) here:

1. **Cantor set IFS:**
    \begin{align*}
        f_1 (x) &= \frac{1}{3} x, \\
        f_2 (x) &= \frac{1}{3} x + \frac{2}{3}
    .\end{align*}
2. **Koch curve IFS:**
    \begin{align*}
        f_1 (x) &= \ScaleMatrix{\frac{1}{3}} x, \\
        f_2(x) &= \ScaleMatrix{\frac{1}{3}} \RotationMatrix{60} x + \left(\frac{1}{3}, 0 \right), \\
        f_3(x) &= \ScaleMatrix{\frac{1}{3}} \RotationMatrix{-60} x + \left( \frac{1}{2}, \frac{\sqrt{3}}{6} \right), \\
        f_4(x) &= \ScaleMatrix{\frac{1}{3}} x + \left( \frac{2}{3}, 0 \right)
    .\end{align*}

For both fractals, we shall take \( U \) to be the open unit interval \(
(0, 1) \). It is trivial to verify that this set is bounded, and the
image of \( U \) under each \( f_i \) is disjoint (a consequence of the
interval being open). It is also trivial to see that for each fractal,
\( U \) contains the union of each image under \( f_i \). Thus, we are
free to utilize Theorem 4.1.2, noting that \( c_i = 1 / 3 \) for each \(
i \) for both fractals. \( \blacksquare \)

The Hausdorff dimension of the Cantor set is thus given by
\[
    \sum_{i = 1}^2 \frac{1}{3^s} = 1 \implies s = \frac{\log 2}{\log 3}
,\]
and similarly the Hausdorff dimension of the Koch curve is
\[
    \sum_{i = 1}^4 \frac{1}{3^s} = 1 \implies s = \frac{\log 4}{\log 3}
.\]

</div>
</details>

<div class="black-box" id="problem413">
**Problem 4.1.3.** Use [Problem 4.1.2](#problem412) to give a proof that the
Cantor set is uncountable.
</div>


<details class="solution">
<summary>Solution 4.1.3.</summary>
<div class="solution-contents">

We claim the following:

**Claim.** Consider a finite or countable set \( P \subset \mathbb{R}^n \). Then for \( s > 0 \),
\[
\mathcal{H}^s (P) = 0
.\]

*Proof.* We shall first show that the Hausdorff measure of a singleton set vanishes. That is,
\[
\mathcal{H}^s (\{ a \}) = 0
.\]
Obviously, observe that the \( \delta \)-cover \( \{ \{a \} \}\) suffices to show that \( \mathcal{H}^s_\delta (\{ a \})  = 0\) and thus \( \mathcal{H}^s (\{ a \} ) = 0 \) by taking \( \delta \to 0^+\).

Now, since \( P \) is countable, suppose \( P = \{ p_1, p_2, \ldots \} \). By nonnegativity and countable additivity from Theorem 2.1.1, we have
\[
\mathcal{H}^s (P) = \mathcal{H}^s\left( \bigcup_{i = 1}^\infty \{ p_i \} \right) = \sum_{i = 1}^\infty \mathcal{H}^s (\{ p_i \}) = 0
,\]
which is what we wished to show. \( \blacksquare \)

We now trivially remark that since \( \mathcal{H}^s (P) = 0 \) for \( s > 0 \) for any finite or countable set \( P \), the set's Hausdorff dimension must be \( 0 \). However, the dimension of the Cantor Set is nonzero, so it must be uncountable.

</div>
</details>

<div class="black-box" id="problem414">
**Problem 4.1.4.** Let \( n, m \in \mathbb{N} \). Show that there is a \( k \)
and a set \( E \subset \mathbb{R}^k \) such that the Hausdorff dimension of \( E \) is \( \frac{n}{m} \). Conclude that for any \( 0 \le r \in \mathbb{R} \), there exists sets with Hausdorff dimension arbitrarily close to \( r \).
</div>


<details class="solution">
<summary>Solution 4.1.4.</summary>
<div class="solution-contents">

In other words, we must prove that for any nonnegative rational number \( q \), there exists a set \( E \subset \mathbb{R}^k \) with dimension \( q \). Consider the following construction. Denote
\[
    P := \left \{ \left( \frac{i_1}{2^m}, \frac{i_2}{2^m}, \ldots, \frac{i_k}{2^m} \right) : \, 0 \le i_1, i_2, \ldots, i_k < 2^m, i_1, i_2, \ldots, i_k \in \mathbb{Z}  \right \}
,\]
and choose \( k \) such that \( mk > n \).
Choose \( 2^n \) points \( p_1, p_2, \ldots, p_{2^n} \in P \) and construct the following IFS:
\[
    f_i(x) = \frac{1}{2^m} x + p_i
.\]
Take \( U := [0, 1]^k \) so that, by the definition of the points in \( P \), the images of \( U \) under each \( f_i \) are disjoint. In addition, clearly
\[
    U \supset \bigcup_i f_i (U)
,\]
as \( U \) can contain \( 2^{mk} \) cubes of dimension \( k \) and side length \( 2^{-m} \), and since we've chosen \( mk > n \), we can fit \( 2^n \) of these cubes in \( U \). Taking these together, \( (f_1, f_2, \ldots, f_{2^n}) \) is an IFS that, equipped with the open set \( U \), satisfies the open set condition. Thus, the Hausdorff dimension of the attractor of the IFS can be calculated as
\[
    \sum_{i = 1}^{2^n} \frac{1}{2^{ms}} = 1 \iff \frac{2^n}{2^{ms}} = 1 \iff s = \frac{n}{m}
,\]
and this holds for any \( n, m \in \mathbb{N} \).

Now that we assuredly have sets with any rational dimension, we can claim the following:

**Claim.** Let \( 0 \le r \in \mathbb{R} \). For any \( \varepsilon > 0 \), there exists a set with Hausdorff dimension \( q \), where \( |r - q| < \varepsilon \).

*Proof.* Decompose \( r \)  as \( r = \lfloor r \rfloor + \{ r \} \), where \( \{ r \} \) denotes the fractional part of \( r \). Suppose that the decimal expansion of \( \{ r \} \) is given to be
\[
    \{ r \} = \overline{0.a_1 a_2 \cdots}
.\]
Define the sequence \( q_i \) as
\[
    q_i = \lfloor r \rfloor + \overline{0.a_1a_2 \cdots a_i}
,\]
where we truncate the fractional part of \( \{ r \} \) to \( i \) digits. Observe that each \( q_i \) is necessarily rational and
\[
    |r - q_i| < 10^{-i}
.\]
It now suffices to choose an \( i \) such that \( 10^{-i} < \varepsilon \), which is possible if \( i > - \log{\varepsilon} / \log 10 \). Since \( q_i \) is rational, we can conclude that a set of Hausdorff dimension \( q_i \) must exist. Thus, there exists a set with Hausdorff dimension arbitrarily close to \( r \). \( \blacksquare \)

</div>
</details>

<div class="black-box" id="problem415">
**Problem 4.1.5.** Construct an example of an IFS which does not satisfy the
OSC, and where no two functions in the IFS are equal.
</div>


<details class="solution">
<summary>Solution 4.1.5.</summary>
<div class="solution-contents">

Denote \( F = (f_1, f_2) \), where \( f_1, f_2 : \mathbb{R} \to \mathbb{R} \) and
\begin{align*}
    f_1(x) &= \frac{2}{3} x \\
    f_2(x) &= \frac{2}{3} x + \frac{1}{3}
.\end{align*}
    
**Claim.** \( F \) is an IFS which does not satisfy the OSC.

*Proof.* BWOC, suppose that the IFS did satisfy the OSC. Then there would exist
a non-empty, bounded, open set \( U \subset \mathbb{R} \) for which \( f_1(U)
\cap f_2(U) = \emptyset \) and \( U \supset f_1(U) \cup f_2(U)\). Observe that by [Problem 2.1.8](#problem218), \( \dim U \le 1 \). However, for \( 0 \le s \le 1 \),
\[
    \frac{4}{3} \le 2 \left( \frac{2}{3} \right)^s \le 2
,\]
so by contrapositive, this IFS clearly cannot satisfy the OSC.
</div>
</details>

This is roughly how far we got into the contest before we ran out of time and
ideas. Perhaps in the future, I'll work through more of the mass distribution
and Sierpinkski triangle sections, but that's a function of how much time and
energy I have. I hope you enjoyed the window into our contest experience; I
enjoyed writing up the solutions quite a bit.

Merry thanksgiving, everybody >:)
