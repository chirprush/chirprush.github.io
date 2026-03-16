> *Spelunking: "the hobby or practice of exploring games"*
>
> *from [Merriam-Webster](https://www.merriam-webster.com/dictionary/spelunking)*

Welcome back everyone! I've definitely been writing far less frequently what
with the CMU workload, but it's finally the start of a new semester! This means
that I finally have some time to put towards other projects, like this blog and
perhaps some larger projects.

Indeed, over winter break whilst I was battling the warm, inviting sirens (my
bed), I made it my goal to complete at least one sizeable project of interest.
After some brainstorming (and some preconceived ideas of what I wanted to do), I
landed on a fun topic: formalizing Markov chains in Lean. There were two main
reasons for this:

1. I knew I wanted to build *something* in Lean. I had read [Theorem Proving in
   Lean4](https://leanprover.github.io/theorem_proving_in_lean4/) before, so I
   knew some basics about how to work in the language, but having actual
   experience and playing around would be fun. Further, having a demonstrable
   project in Lean is good to refer back to (ex. "Oh I remember this one
   pattern; let me look it up in my project"), and it's also good to show to
   others. Most importantly though, it's cool to nerd out :)
2. Markov chains have recently appeared to me in a very new light. This is
   mostly due to my professor (from the fall semester 2025),
   [Wesley Pegden](https://www.cmu.edu/math/people/faculty/pegden.html), who
   taught 21-242 (linear algebra with proofs). Pegden cares a lot about
   pedagogy and is very articulate with his explanations, which is nice to see.
   Pegden's main specialty is not linear algebra, however, but combinatorics,
   probability, the [Abelian
   sandpile](https://en.wikipedia.org/wiki/Abelian_sandpile_model) (I had no
   clue this existed until I read Pegden's bio), and
   their applications (this is also striking, as Pegden is a pure mathematics
   professor).

A third subreason soon emerged in that proofs surrounding Markov chains (some of
which Pegden showed us 21-242!) are rather amenable to Lean. Most of the proofs,
as it turns out, are based algebraic manipulations and inequalities. Only a
small handful of theorems use results from analysis, number theory, or spectral
theory.
