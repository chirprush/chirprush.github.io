In comparison to fields like high school/undergraduate calculus and linear
algebra, tensor calculus is a subject that feels rather _out there_. The first
time when one might hear about tensor calculus is in general relativity to model
the curvature of spacetime, and it even has it's own embedded language of sorts
for how to manage indices. The concept of a tensor itself is rather esoteric, a
common joke being that a tensor is defined seemingly tautologically as anything that
transforms like a tensor (although this is more of a nod to the mathematical
view of a tensor as an abstract multilinear map).

But tensor calculus itself is a rather beautiful and geometric extension of
regular calculus, and it comes as a consequence of differing coordinate systems.
The main tenant of tensor calculus (specifically the transformation rules of
tensors) is actually rather natural: **objects are physically the same
regardless of how we view them**. At the moment, this statement might not be
very impactful (we will revisit after some actual math), but we do already have
some inuitive notion of what this is getting at. In physics, we have different
systems of measurement: the SI system, the CGS system, the goofy imperial
system, and so on. One can say a certain length is \( 2.54 \text{ cm} \) or \( 1
\text{ in} \), and while both the numbers and units are different, the physical
lengths both represent are the same. Tensor calculus takes this idea,
generalizes it much further, and makes it systematic.

[comments]: I like making things conversational, but I feel like this is a lot
[comments]: of exposition idk I want to revise it quite a bit.
[comments]: tie this into units maybe
[comments]: Maybe give a preview of attractions to come with a simulation
[comments]: Also maybe it's because the font isn't loading rn but the paragraphs
[comments]: look far too long
[comments]: Also mention how I'm definitely not going to go into manifolds right
[comments]: here for those who know

## Coordinate Systems

Early we looked at the adage (? is this the right word) that objects are
physically the same regardless of how they are viewed. In order to make this
statement concrete, we must make concrete what we mean by viewing something
physical. In particular, we do so by constructing the notion of a coordinate
system.

[outline]: Consider we have two coordinate systems for the same plane (we only
[outline]: treat coordinate systems and we don't really go into the rigour of manifolds and
[outline]: such because idk topology bro like) (so we're
[outline]: assuming 2D because it's the easiest to visualize). Both coordinate
[outline]: systems look the same in terms of themselves of course, but it's the
[outline]: between them that we care about
[look this up]: Must the number of coordinates always be the same? I feel
[look this up]: like differentiability should preserve the dimension of the
[look this up]: manifold perhaps and like we're going to assume that the entire space is filled
[look this up]: (i.e. bijective).

[outline]: It'd be good to have like a nice diagram showing the basis is just
[outline]: derivatives and then we can just write them as linear combinations

[outline]: Then we go into the transformation rules -> covariant and
[outline]: contravariant vectors (called vectors and covectors in math) are
[outline]: really wacky but ultimately a consequence of the chain rule right
[outline]: Mathematically the vector space is isomoporhic to the dual space so
[outline]: while you could always just use normal vectors, they don't transform the way
[outline]: that we want because if the basis transforms one way, the components have to
[outline]: transform the other way (think about this in terms of units and such)

[outline]: Now we move onto the metric tensor for lengths

[outline]: Tensor products? I have to look more into them
[outline]: Maybe the abstract view of tensors? And like combining it with
[outline]: physics?

[outline]: Eventually I wish to derive the geodesic equations but idk
[outline]: Probably a look at curvature would be nice I still have to figure it
[outline]: out but it's a fairly good example of something that is helped a lot by
[outline]: tensor calculus
[outline]: Small note somewhere to clarify tensor vs tensor field

## A Tangible Example
