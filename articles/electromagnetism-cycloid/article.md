Hello again, everyone! This will be a short and sweet mini-article (with bigger
articles coming up) on a physics problem taken from a textbook in our physics
class. For the reader's (slight) entertainment, I'll set the scene exactly:

I was bored during our second period of Physics C, and we had just gotten the
packets on magnetism, so I took a scroll through the book. Aside from the
interestingly detailed right hand rule diagrams (props to the artists), one
problem found in the bottom right of a random page caught my eye. A particle was
placed in a specific configuration of an electric and magnetic field so as to
have the path of a [cycloid](https://en.wikipedia.org/wiki/Cycloid). The
problem was just to nonrigorously explain this behavior, but the textbook noted
that the explicit, mathematical derivation and description of the path was something for more advanced textbooks.

So of course, I spent the period thinking about it. In the process, I also kinda
missed what our teacher was lecturing on. Oops.

<div class="black-box">
**Problem.** Consider a particle of charge \( +q \) and mass \( m \) placed at
rest at the origin in a constant magnetic field \( \mathbf{B} \) directed in the negative \( z
\)-direction and a constant electric field \( \mathbf{E} \) directed upward in the
positive \( y \)-direction.

Determine the trajectory of the particle at time \( t \).
</div>

## The Workings

The diagram from the textbook indicates that the particle always stays in the \(
xy \)-plane. Indeed, the particle's trajectory is determined entirely by the
Lorentz force
\[
    \mathbf{F} = q (\mathbf{E} + \mathbf{v} \times \mathbf{B})
,\]
and since the electric field has no \( z \)-component while the magnetic field
is only in the \( z \)-axis, this indeed makes sense.

Thus, we can model the position of the particle \( \mathbf{x}(t) \) at a time \(
t \) as a vector in \( \mathbf{R}^2 \) and consider the individual components of
the force by Newton's second law:
\begin{align*}
    m \ddot{\mathbf{x}}_x (t) &= qB \dot{\mathbf{x}}_y(t), \\
    m \ddot{\mathbf{x}}_y (t) &= -qB \dot{\mathbf{x}}_x (t) + qE
.\end{align*}
This is actually a very interesting system of differential equations, because
they're coupled! They are not individually solvable, so we need some cool
methods. Since this system is linear, we can set up a matrix differential equation! One can
verify that the system is equivalent to
\[
    \frac{d}{dt} \dot{\mathbf{x}} (t) = \begin{bmatrix}
        0 & qB / m \\
        -qB / m & 0
    \end{bmatrix} \dot{\mathbf{x}}(t) + \begin{bmatrix}
        0 \\
        qE / m
    \end{bmatrix}
.\]
But, this is actually a very simple form. We have a constant (in \( t \)) matrix
(let's call it \( A \)) times the function plus a constant, which lets us reasonably
ansatz an exponential function of the form
\[
    \dot{\mathbf{x}}(t) = \exp(A t) \mathbf{u} + \begin{bmatrix}
        E / B \\
        0
    \end{bmatrix}
.\]
And our initial condition \( \dot{\mathbf{x}} (0) = \mathbf{0} \) give \( \mathbf{u} \) so that
\[
    \dot{\mathbf{x}}(t) = (I - \exp(A t)) \begin{bmatrix}
        E/B \\
        0
    \end{bmatrix}
.\]
In order to simplify this now, we actually need to evaluate the matrix
exponential. Luckily \( A \) is of the form
\[
    A = \frac{qB}{m} t \begin{bmatrix}
        0 & 1 \\
        -1 & 0
    \end{bmatrix}
.\]
Ignoring the constant factor, this matrix would have order two, so the even powered
terms are the identity, and the odd powered terms are just \( A \) (ignoring the
constant again). Putting the constants back in, we get a rotation-like matrix in the solution:
\[
    \dot{\mathbf{x}}(t) = \begin{bmatrix}
        1 - \cos{\left( \frac{qB}{m} t \right)} & -\sin{\left( \frac{qB}{m} t \right)} \\
        \sin{\left( \frac{qB}{m} t \right)} & 1 - \cos{\left( \frac{qB}{m}t \right)}
    \end{bmatrix} \begin{bmatrix}
        E / B \\
        0
    \end{bmatrix}
    =
    \frac{E}{B}
    \begin{bmatrix}
        1 - \cos{\left( \frac{qB}{m} t \right)} \\
        \sin{\left( \frac{qB}{m} t \right)}
    \end{bmatrix}
.\]
We can then integrate this vector element-wise and apply the initial condition \(
\mathbf{x} (0) = \mathbf{0} \) to get
\[
    \mathbf{x}(t) = \frac{E}{B} \begin{bmatrix}
        t - \frac{m}{qB} \sin{\left( \frac{qB}{m} t \right)} \\
        \frac{m}{qB} - \frac{m}{qB} \cos{\left( \frac{qB}{m} t \right)}
    \end{bmatrix}
.\]
There's our cycloid!

## An Isomorphism

If one likes matrix exponentials and coupled differential equations less, we can
take an
[isomorphism](https://en.wikipedia.org/wiki/Complex_number#Matrix_representation_of_complex_numbers)
to the complex numbers! In particular, we can treat \(
\mathbf{x}(t) \) to represent the particle's position in \( \mathbf{C} \), where
the real component is the \( x \)-component and the imaginary component is the
\( y \)-component. With this, our matrix \( A \) just gets mapped to \( -i qB / m \).
Working through everything, this yields the highly analogous solution
\[
    \mathbf{x}(t) = \frac{E}{B} \left( t + i \frac{m}{qB} - i \frac{m}{qB} \exp{\left( -i \frac{qB}{m} t\right)} \right)
.\]
