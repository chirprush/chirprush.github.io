## Problem

<div class="side-box">
**Problem.** We call a permutation *bitonic* if all the elements increase until a certain index \( k \), where \( 2 \le k \le n - 1 \), and then decrease until the end.

Count modulo \( 10^9 + 7 \) the number of bitonic permutations of length \( n \) such that \( B_i = x \) and \( B_j = y \), where \( i < j \) and \( x \ne y \).
</div>

## Solution

Given the definition of a bitonic permutation, we are motivated to go casewise on \( k \) when counting. Notice that since the elements increase up to \( k \) and decrease afterwards, \( B_k \) must be equal to the maximum value, \( n \).

**Observation.** Without the \( B_i \) and \( B_j \) conditions, the number of total bitonic permutations \( A \) on \( n \) numbers is given by
\[
    A = \sum_{k = 2}^{n - 1} \binom{n - 1}{k - 1} = 2^{n - 1} - 2
.\]
This works because we must set \( B_k = n \), giving us \( n - 1 \) elements left to choose from. We can then choose any \( k - 1 \) of the remaining elements because there is only one way to increasingly sort each choice, and the choice of \( k - 1 \) elements uniquely determines the decreasing elements.

With this idea in mind, we can start looking at the constrained problem. There are two main cases that we have to consider:

- Either \( B_i = x = n \) or \( B_j = y = n \). Having this condition forces \( k \) to be either \( i \) or \( j \). This case is actually easier, however, as we only have to consider one value. Consulting the following diagram,

    <img src="/articles/codeforces-problem-1763D/figures/edgecase1.png" />

    we see that the answers for each case respectively should be
    \[
        \binom{n - y - 1}{j - i - 1} \binom{y - 1}{n - j}, \text{ and } \binom{n - x - 1}{j - i - 1} \binom{x - 1}{i - 1} 
    ,\]
    since we must handle the sorting condition and since choosing two of the sections uniquely determines the choice of the third.
- Otherwise we must go casewise on all possible values of \( k \). In particular, though, we can group these cases of \( k \) into three further cases: \( k < i \), \( i < k < j \), and \( k > j \).

We shall now tackle these cases:

- Case \( k < i \). We must have that \( x > y \), and we have the following diagram:

    <img src="/articles/codeforces-problem-1763D/figures/maincase1.png" />

    For this case, it's clear to see that the answer is
    \[
        \binom{n - x - 1}{i - k - 1} \binom{x - y - 1}{j - i - 1}  \binom{y - 1}{n - j}  
    .\]
- Case \( i < k < j \). We have the following diagram:

    <img src="/articles/codeforces-problem-1763D/figures/maincase2.png" />

    This case is slightly more complicated, as there is an overlap of elements in the inner two sections. With a bit of thinking, we see that the condition \( n - \min\{x, y\} - 1 \ge j - i - 2 \) must hold (otherwise there is no possible permutation). For convenience, we shall say that WLOG \( x < y \), simplifying the condition to \( n - x - 1 \ge j - i - 2 \).

    We shall first place the elements in range \( y + 1 \) to \( n - 1 \). We must choose \( j - k - 1 \) of them to place in the third interval, leaving the others to be uniquely placed in the second interval. We shall then choose the remaining \( k - i - 1 - (n - y - 1 - (j - k - 1)) = j - i - 1 + y - n \) numbers out of the \( y - x - 1 \) we have. All that is left is to choose the first interval out of simplicity, which then uniquely determines the fourth.

    Thus, if \( x < y \), the answer is
    \[
        \binom{n - y - 1}{j - k - 1}  \binom{y - x - 1}{j - i - 1 + y - n}  \binom{x - 1}{i - 1} 
    ,\]
    and if \( x > y \), the answer is
    \[
        \binom{n - x - 1}{k - i - 1} \binom{x - y - 1}{j - i - 1 + x - n} \binom{y - 1}{n - j} 
    .\]
- Case \( k > j \). We must have that \( x < y \), and we have the following diagram:

    <img src="/articles/codeforces-problem-1763D/figures/maincase3.png" />

    It is also apparent for this case that the answer is
    \[
        \binom{n - y - 1}{k - j - 1} \binom{y - x - 1}{j - i - 1} \binom{x - 1}{i - 1} 
    .\]
