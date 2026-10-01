# Coding Practice Patterns from ex1.h and ex2_skel.c

There is no separate lab-material set available. These files are the current evidence for likely coding practice.

## ex1.h — bitwise C patterns

Be able to write and debug:

- Test the LSB and MSB
- Extract bit `i`
- Set, clear, and flip bit `i`
- Count leading and trailing zeros
- Test even/odd values
- Multiply by 16 with unsigned-overflow protection
- Compute modulo 128 using bit operations
- Produce a 32-bit binary string

### Patterns to know

```c
n & 1u
n & (1u << i)
n | (1u << i)
n & ~(1u << i)
n ^ (1u << i)
n >> 31
n & 127u
n << 4
```

Always check bit ranges when required. Remember that shifting by 32 or more is invalid/undefined for a 32-bit value.

## ex2_skel.c — C, memory, arrays, and debugging patterns

Be able to understand and debug:

- `typedef float point3d[3]`
- Arrays of fixed-size records
- Pointer-to-array parameters
- Dynamic allocation with `malloc`
- Correct `sizeof` expressions
- Nested loops
- Signed floating-point comparisons
- Counters indexed by octant/sign pattern
- `rand`, `RAND_MAX`, and timing with `clock`
- Correct use of `free`

### Debugging checklist

- Is every allocation checked and freed?
- Is `sizeof` applied to the correct type?
- Are array indices within bounds?
- Are loop limits correct?
- Are all branches mutually exclusive and complete?
- Are counters initialized before use?
- Are integer, unsigned, float, and double types being mixed safely?
- Does the code classify zero consistently with the specification?
- Is the output destination correct?
- Can the code be simplified without changing behavior?

## Lab-test preparation

Practice by taking a short function and doing three things:

1. Explain its intended behavior.
2. Find a bug or missing statement.
3. Test boundary cases: zero, maximum bit, negative values, empty input, and last valid index.
