Measurment of Code Speed

Create an array F[0...n]
F[0] <-- 0
F[1] <-- 1

for i from 2 to n:
    F[i] <-- F[i-1] + F[i-2]

return F[n]


The lines of code: 2n + 2

Breakdown the code lines:

1- Create an array F[0...n]
Based on memory managent system to allocate memory and keep 0 on memory

2- F[0] <-- 0  Assignment (Find memory location and then assignment)
3- F[1] <-- 1  Assignment

4- for i from 2 to n (increment i, comparision i to n to break loop, branch move to another instruction after loop)

5- F[i] <-- F[i-1] + F[i-2] (lookup, assignment, addition of big integers)

6- return F[n] (lookup, return)


Some additional Factors:
1- Speed of the Computer
2- The System Archiecture of Computer
3- The compiler being used (High-level language or Low-level language, optimization of code)
4- Memory Hierarchy (Lookup speed, Exactly how memory storge and capacity)

So it's tough to calculate the exact computing runtime

In practice, you might not even know some of factors (Your program wiil run on variety of computers)

Our Goal:
1- Measure Runtime without knowing these details
2- Get results that work for large inputs, so we sshould calculate runtime based on the size of input


Asymptotic Notation
Need some less precise but its too good

Assume all of missed details can describe as a constant, so if you use faster computer, this constant decresaed
So measure runtime in a way that ignore constant multiples (We ignore details)

So by change constant we can achieve 1 Year, 1 hour or 1 minute of runtime.

Asymptotic runtime measure based on the input size, so if the input size increase, runtime increase too. Runtime proportional to input size (We want to find this relationship)

We Approximate Runtimes
We assume our computer run on Gigahertz (GHz) (10^8 Hz)
Consider runtime proportion to n
So:
if n = 20 --> runtime = 1 sec
then n = 50 --> runtime = 1 sec
then n = 10^6 --> runtime = 1 sec
then n = 10^9 --> runtime = 1
Max n --> 10^(9)

Consider runtime proportion to (n)log(n):
if n = 20 --> runtime = 1 sec
then n = 50 --> runtime = 1 sec
then n = 10^6 --> runtime = 1 sec
then n = 10^9 --> runtime = 30 Sec
Max n --> 10^(7.5)

Consider runtime proportion to n^2:
if n = 20 (4 * 10^2 actions)  --> runtime = 1 sec
then n = 50 (25 * 10^2 actions) --> runtime = 1 sec
then n = 10^2 (10^4 actions) --> runtime = 1 sec
then n = 10^6 (10^12 actions) --> runtime = 17 min
then n = 10^9 (10^18 actions) --> runtime = 30 year
Max n --> 10^(4.5)


Consider runtime proportion to 2^n:
if n = 20 --> runtime = 1 sec
then n = 50 --> runtime = 13 day
then n = 10^2 --> runtime = 4.10^13 Year
Max n --> 30




So:

log n << (n) ^ (0.5) << n << (n)log(n) << n^2 << 2^n

Big-O Notation

f(n) = O(g(n)) 
(f is Big-O of g) or f <= g
if there exist constants N and c so that for all n >= N, f(n) <= c.g(n)

(f is bounded above by some constants multiple of g)

e.g.:
3n^2 + 5n + 2 = O(n^2) since if n >= 1
3n^2 + 5n + 2 <= 3n^2 + 5n^2 + 2n^2 = 10n^2
so n^2 multiples 10 can bounded this function
O(n^2)

our function are the same frowth rate by n^2

Use big-O notation to report algorithm runtimes.

Advantage:
1- clarify growth rate based on input size (how big we can handle) and compare algorithms based on input
2- Clean up Notation (O(n^2) is easier than 3n^2 + 5n + 2) or (log2(n), log3(n), logx(n) differ by constant multiples, and don't need to specify which
3- Make easier to Algebra on different algorithm runtimes speed
4- Can ignore comlicated details (all factors considered in constant)

Disadvantages:
1- loses important information about constant multiples and loses various details
2- Big-O is only asymptotic (in some sense we want to talk about when we use very very very big input and when we want to run in specifc input it is not useful enough)(sometime we cannot store these very very very big on computer or our hardware)


Using Big-O Notation

Common Rules:
1- (constants can be omitted) 7n^3 = O(n^3); n^2/3 = O(n^2)
2- n^a < n^b for 0 < a < b --> so we can assume n = O(n^2) or (n^0.5) = O(n) (why? because O(n^2) upper bounded of n and O(n) is bounded above n^0.5)
3- n^a < b^n (a > 0, b > 1) --> n^5 = O((2^0.5)^n), n^100 = O(1.1^n)
4- (log n) ^ a < n^b (a, b > 0) --> (log n)^3 = O(n^0.5), nlogn = O(n2)
5- (sum of term can asuume based on max) --> n^2 + n = O(n^2) or 2^n + n^9 = O(2^n)
6- n < (n)log(n)
## Common rules

Before proceeding with visualizations, let's review the common rules of comparing the order of growth of functions arising frequently in algorithm analysis.

1. Multiplicative constants can be omitted: $c \cdot f \preceq f$. Examples: $5n^2 \preceq n^2$, $\frac{n^2}{3} \preceq n^2$.
2. Out of two polynomials, the one with larger degree grows faster: $n^a \preceq n^b$ for $0 \le a \le b$. Examples: $n \prec n^2$, $\sqrt{n} \prec n^{2/3}$, $n^2 \prec n^3$, $n^0 \prec \sqrt{n}$.
3. Any polynomial grows slower than any exponential: $n^a \prec b^n$ for $a \ge 0, b>1$. Examples: $n^3 \prec 2^n$, $n^{10} \prec 1.1^n$.
4. Any polylogarithm grows slower than any polynomial: $(\log n)^a \prec n^b$ for $a, b>0$. Examples: $(\log n)^3 \prec \sqrt{n}$, $n\log n \prec n^2$.
5. Smaller terms can be ommited: if $f \prec g$, then $f+g\preceq g$. Examples: $n^2+n \preceq n^2$, $2^n+n^9 \preceq 2^n$.


Measurment of Code Speed in terms of Big-O Notation

Create an array F[0...n]
F[0] <-- 0
F[1] <-- 1

for i from 2 to n:
    F[i] <-- F[i-1] + F[i-2]

return F[n]


Breakdown the code lines:

1- Create an array F[0...n] --> O(n)
2- F[0] <-- 0   --> O(1)
3- F[1] <-- 1   --> O(1)
4- for i from 2 to n --> O(n)
5- F[i] <-- F[i-1] + F[i-2] --> O(n)
6- return F[n] --> O(1)

Sum of works: O(n) + O(1) + O(1) + O(n).O(n) + O(1) = O(n^2)
The runtime speed: O(n^2)


We have a different notation:
f(n) = Omega(g(n)) --> bounded below


logx(n) < n^(0.1) < n ^ (0.5) < n < (n) logx(n) < n ^ (1.1) < n ^(1.1) < n ^ 2 < n ^ 3 < 1.1^n < 2 ^ n

