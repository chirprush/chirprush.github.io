## Background

\[
    \gdef\vvec#1{\mathbf{#1}}
\]

A little bit ago I was creating a 3D renderer from scratch for CS class, and I thought it would be a fun idea to try deriving the rendering and projection techniques myself mathematically. I don't quite know if this is how it's usually done in general (perhaps I could have overcomplicated some things?), but this is what I came up with.

We shall first describe the following variables that we have to work with:

- \( \vvec{c} \), the vector containing the camera position,
- \( \vvec{\hat n} \), the unit vector relative to the camera position that contains the direction of the camera,
- \( \vvec{q} \), the center of the projection plane,
- \( \textsf{dist} \), the distance from the camera to the projection plane,
- \( \textsf{width} \), the width of the projection plane,
- \( \textsf{height} \), the height of the projection plane,

The projection plane is the plane with center \( \vvec{q} = \vvec{c} + \textsf{dist} \cdot \vvec{\hat n} \) and is oriented to be orthogonal to \( \vvec{\hat n} \).

The desired outcome of the perspective projection algorithm is, given a point \( \vvec{p} \), to determine where \( \vvec{p} \) lies when projected on the plane, whether or not it should be rendered (i.e. does it lie in the width and height bounds and it is in front of the camera?), and where on the screen it should be rendered.

## Derivation

The first order of business is to project the point onto the plane. Note that the perspective projection of \( \vvec{p} \) lies on the ray \( \vvec{r} (t) = t\vvec{c} + (1 - t) \vvec{p} = \vvec{c} + t (\vvec{p} - \vvec{c}) \), so we must determine where this ray intersects with the plane.

Observe that the projection plane is the set of vectors \( \vvec{x} \) such that \( \vvec{\hat n} \cdot (\vvec{x} - \vvec{q}) = 0 \). With this, we may substitute \( \vvec{r}(t) \) in for \( \vvec{x} \) to determine the intersection:
\[
    \vvec{\hat n} \cdot (\vvec{r}(t) - \vvec{q}) = \vvec{\hat n} \cdot (\vvec{c} - \vvec{q} + t(\vvec{p} - \vvec{c})) = 0
.\]
From this, we obtain
\[
    t_p = \frac{\vvec{\hat n} \cdot (\vvec{q} - \vvec{c})}{\vvec{\hat n} \cdot (\vvec{p} - \vvec{c})} = \frac{\textsf{dist}}{\vvec{\hat n} \cdot (\vvec{p} - \vvec{c})}
.\]
With this construction, values of \( t_p \) that are negative correspond to points behind the camera, so these can be thrown out.

Now that we have the projected point onto the plane \( \vvec{r} (t_p) \), we must figure out where on the plane this value falls to render it onto the screen. To do so, we shall construct an orthogonal basis for the plane, with the origin at the center of the plane, and then solve for the corresponding position of the points mapped in terms of the plane basis.

Through \( 90^\circ \) rotations of the camera direction vector about respective axes (converting to spherical coordinates and then simply adding angles makes this a whole lot easier), we can obtain vectors \( \vvec{r} \) and \( \vvec{d} \), which represent the right and down orthonormal basis vectors of the projection plane. Our goal then is to solve the following matrix equation:
\[
    A \vvec{v} = \vvec{p} - \vvec{q}
,\]
where \( A = \begin{bmatrix} \vvec{r} & \vvec{d} \end{bmatrix} \). Although \( A \) is not square, we may multiply by its left psuedoinverse on both sides to see that
\[
    \vvec{v} = \begin{bmatrix} x \\ y \end{bmatrix} = (A^T A)^{-1} A^T (\vvec{p} - \vvec{q})
.\]
From this, we can map the coordinates onto our rendering canvas and cull any points that potentially lie out of our view.
