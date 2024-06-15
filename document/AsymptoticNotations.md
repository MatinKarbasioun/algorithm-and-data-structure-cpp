
# Measurement of Code Speed

## Fibonacci Sequence Algorithm

### Pseudocode:
```cpp
Create an array F[0...n]
F[0] <-- 0
F[1] <-- 1

for i from 2 to n:
    F[i] <-- F[i-1] + F[i-2]

return F[n]
```

### Breakdown of Code Lines:
1. **Create an array F[0...n]**: Allocation of memory and initialization.
2. **F[0] <-- 0**: Assignment operation.
3. **F[1] <-- 1**: Assignment operation.
4. **for i from 2 to n**: Loop with increment, comparison, and branching.
5. **F[i] <-- F[i-1] + F[i-2]**: Lookup, addition, and assignment.
6. **return F[n]**: Lookup and return.

### Lines of Code:
Total: `2n + 2`

## Factors Affecting Code Speed:
1. Speed of the computer.
2. System architecture.
3. Compiler optimizations.
4. Memory hierarchy.

Due to these factors, it's difficult to calculate the exact runtime of a program. The goal is to measure runtime based on the size of the input, ignoring constant factors.

## Asymptotic Notation:
Asymptotic notation helps measure runtime based on input size while ignoring constant factors. This way, we can approximate runtimes for large inputs, which gives us a clearer understanding of how the algorithm scales.

### Example Runtime Proportions:
1. **Proportional to n**:
    - `n = 20` --> `runtime = 1 sec`
    - `n = 50` --> `runtime = 1 sec`
    - `n = 10^6` --> `runtime = 1 sec`
    - `n = 10^9` --> `runtime = 1 sec`
    - Max `n` --> `10^9`

2. **Proportional to n log(n)**:
    - `n = 20` --> `runtime = 1 sec`
    - `n = 50` --> `runtime = 1 sec`
    - `n = 10^6` --> `runtime = 1 sec`
    - `n = 10^9` --> `runtime = 30 sec`
    - Max `n` --> `10^7.5`

3. **Proportional to n^2**:
    - `n = 20` (400 actions) --> `runtime = 1 sec`
    - `n = 50` (2500 actions) --> `runtime = 1 sec`
    - `n = 10^2` (10^4 actions) --> `runtime = 1 sec`
    - `n = 10^6` (10^12 actions) --> `runtime = 17 min`
    - `n = 10^9` (10^18 actions) --> `runtime = 30 years`
    - Max `n` --> `10^4.5`

4. **Proportional to 2^n**:
    - `n = 20` --> `runtime = 1 sec`
    - `n = 50` --> `runtime = 13 days`
    - `n = 10^2` --> `runtime = 4 x 10^13 years`
    - Max `n` --> `30`

### Order of Growth:
`log n << n^(0.5) << n << n log(n) << n^2 << 2^n`

## Big-O Notation:
Big-O notation expresses the upper bound of the runtime of an algorithm in terms of the size of the input.

### Definition:
`f(n) = O(g(n))` means `f` is Big-O of `g`, or `f` <= `g` if there exist constants `N` and `c` such that for all `n >= N`, `f(n) <= c.g(n)`.

### Example:
`3n^2 + 5n + 2 = O(n^2)` since for `n >= 1`, `3n^2 + 5n + 2 <= 10n^2`.

### Advantages:
1. Clarifies growth rate based on input size.
2. Cleans up notation.
3. Facilitates algebraic manipulation of runtimes.
4. Ignores complicated details by considering constants.

### Disadvantages:
1. Loses information about constant multiples and various details.
2. Only useful for asymptotic analysis, not for specific small inputs.

### Using Big-O Notation:

#### Common Rules:
1. Constants can be omitted: `7n^3 = O(n^3)`, `n^2/3 = O(n^2)`.
2. Larger degree polynomials grow faster: `n^a < n^b` for `0 < a < b`.
3. Any polynomial grows slower than any exponential: `n^a < b^n` for `a > 0, b > 1`.
4. Any polylogarithm grows slower than any polynomial: `(log n)^a < n^b` for `a, b > 0`.
5. The sum of terms can be assumed based on the maximum: `n^2 + n = O(n^2)`, `2^n + n^9 = O(2^n)`.

## Measuring Code Speed in Terms of Big-O Notation:
### Fibonacci Sequence Algorithm:
```cpp
Create an array F[0...n]
F[0] <-- 0
F[1] <-- 1

for i from 2 to n:
    F[i] <-- F[i-1] + F[i-2]

return F[n]
```

### Breakdown:
1. **Create an array F[0...n]**: `O(n)`
2. **F[0] <-- 0**: `O(1)`
3. **F[1] <-- 1**: `O(1)`
4. **for i from 2 to n**: `O(n)`
5. **F[i] <-- F[i-1] + F[i-2]**: `O(n)`
6. **return F[n]**: `O(1)`

### Total Work:
`O(n) + O(1) + O(1) + O(n) + O(n) + O(1) = O(n^2)`

### Different Notations:
`f(n) = Omega(g(n))` is bounded below.

### Order of Growth:
`logx(n) < n^(0.1) < n^(0.5) < n < n logx(n) < n^(1.1) < n^2 < n^3 < 1.1^n < 2^n`
