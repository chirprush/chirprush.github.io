## Theoretical Groundwork

\[
    \gdef\vvec#1{\mathbf{#1}}
\]

This is a small little description of how I would try to draw equipotential curves, specifically for *two dimensional* vector fields. We shall first start by laying the groundwork of vector fields and potentials.

<div class="side-box">
**Definition.** Let \( \vvec{F} \colon \mathbb{R}^n \to \mathbb{R}^n \) be a vector field. We call the field's potential function \( P \colon \mathbb{R}^n \to \mathbb{R} \) the unique function such that:
\[
\vvec{F} = - \nabla P
.\]
</div>

It is from this definition that the usual physics properties of the potential arise, and it also gives one a nice geometric intuition (field lines follow the potential downhill). In particular, we have that
\[
    \int_{\vvec{a}}^{\vvec{b}} \vvec{F} \cdot d\vvec{l} = \int_{\vvec{b}}^{\vvec{a}} \nabla P \cdot d\vvec{l} = P(\vvec{a}) - P(\vvec{b})
,\]
which follows from the Gradient Theorem.

It is also from this definition that another key property of potentials arises, one that is very useful in attempting to draw them.

<div class="side-box">
**Claim.** At all points across an equipotential surface, the field lines are orthogonal to the surface.
</div>

*Proof.* Suppose we have a potential function \( P \) and we are looking in the neighborhood of some point \( \vvec{r} \). Any point on the equipotential surface in the neighborhood of this point is by definition a point for which the potential does not differ from \( P(\vvec{r}) \). In other words, we are looking for any point \( \vvec{x} = (x_1, x_2, \ldots, x_n) \) such that
\[
    x_1 \frac{\partial P(\vvec{r})}{\partial x_1} + x_2 \frac{\partial P(\vvec{r})}{\partial x_2} + \cdots + x_n \frac{\partial P(\vvec{r})}{\partial x_n} = \vvec{x} \cdot \nabla P(\vvec{r}) = 0
.\]
Observe that \( \nabla P = - \vvec{F} \), so this reduces to any point \( \vvec{x} \) on the equipotential surface in the neighborhood of \( \vvec{r} \) having the property that
\[
    \vvec{F} \cdot \vvec{x} = 0
,\]
which means that the vector tangent to the equipotential surface is orthogonal to the field lines.

## The Algorithm

Realizing this, we can use this to find and draw points along equipotential curves in two dimensions. Note that, for higher dimensions, this strategy fails to work given a greater number of points needed to define a valid surface as well as having a greater number of directions. That being said, this algorithm could be adapted to higher dimensions if given enough thought.

Suppose we start at some point \( \vvec{r} \) and we wish to find some further point \( \vvec{r}'' \) on the equipotential surface. We may first move along the vector orthogonal to the field line at the point by some amount. That is to say,
\[
    \vvec{r}' \leftarrow \vvec{r} + dt \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \frac{\vvec{F}(\vvec{r})}{\| \vvec{F} (\vvec{r}) \|}
,\]
where the matrix represents a clockwise \( 90^\circ \) rotation and \( dt \) represents some step size.

Practically, however, this also changes the potential we are at, so we must normalize the vector in a sense. We shall choose to normalize the vector along the field vector \( \vvec{F} (\vvec{r}') \), as going along the surface does not change the potential value. We can measure the potential value at \( \vvec{r}' \) and then compare this to the value of \( P(\vvec{r}) \) we wish to stay at in order to determine how far to step. In particular, using the shorthand that \( \vvec{F} = \vvec{F} (\vvec{r}') \), let
\[
    \Delta P = \left. \frac{\partial}{\partial t} \, P(\vvec{r}' + t \vvec{F}) \right\vert_{t = 0}
\]
so that \( (\Delta P) t = P(\vvec{r}) - P(\vvec{r}') \). Then our final approximation for the next point along the equipotential surface is given by
\[
    \vvec{r}'' \leftarrow \vvec{r}' + t \vvec{F}
.\]
Note that for several steps along the equipotential surface, the value of \( P(\vvec{r}) \) should be stored and held constant in order to not diverge from the equipotential.

### A Specific Case

As a final remark, we shall calculate the value of \( \Delta P \) for an electrostatic system of \( n \) particles with respective charges \( q_1, q_2, \ldots, q_n \) and positions \( \vvec{r}_1, \vvec{r}_2, \ldots, \vvec{r}_n \). We have that
\[
    P(\vvec{r}) = \sum_{i = 1}^{n} \frac{kq_i}{\| \vvec{r} - \vvec{r}_i \|}
.\]
This then tells us that
\[
\begin{align*}
    \left. \frac{\partial}{\partial t} P(\vvec{r}' + t \vvec{F}) \right\vert_{t = 0} &= -\left. \sum_{i = 1}^{n} \frac{k q_i}{\| \vvec{r}' + t \vvec{F} - \vvec{r}_i \|^3} \, (\vvec{r}' + t \vvec{F} - \vvec{r}_i) \cdot \vvec{F} \, \right\vert_{t = 0} \\
    &= - \vvec{F} \cdot \sum_{i = 1}^{n} \frac{k q_i (\vvec{r}' - \vvec{r}_i)}{\| \vvec{r}' - \vvec{r}_i \|^3}.
\end{align*}
\]
