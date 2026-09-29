# CDT204 — Lesson 1 Practice Exam

## Scope

Lecture 1: Introduction and Performance.

Use only Lesson 1 material. Do not use notes while answering. Show every calculation, unit, assumption, and comparison clearly.

**Total: 31 points + 2 bonus points**

---

## Question 1 — Core concepts (5 points)

### a. (3 points)
Recite the seven great ideas in computer architecture and explain each in one or two sentences.

### b. (1 point)
Explain the difference between response time and throughput. Give one example where improving throughput does not directly reduce the execution time of one task.

### c. (1 point)
Explain two reasons why MIPS is a flawed metric for comparing computers.

---

## Question 2 — CPU time and speedup (6 points)

A program executes `1.2 × 10^9` instructions.

| Computer | Clock rate | CPI |
|---|---:|---:|
| P1 | 2.5 GHz | 1.6 |
| P2 | 3.2 GHz | 2.0 |

### a. (4 points)
Calculate the CPU execution time on P1 and P2.

### b. (1 point)
Which computer is faster?

### c. (1 point)
Calculate the speedup of the faster computer over the slower computer.

---

## Question 3 — Instruction mix and average CPI (5 points)

A program executes `4 × 10^9` instructions on a processor with a clock rate of 2.5 GHz.

| Instruction class | Fraction of instructions | CPI |
|---|---:|---:|
| Arithmetic | 50% | 1 |
| Load/store | 30% | 2 |
| Branch | 20% | 5 |

### a. (3 points)
Calculate the average CPI.

### b. (2 points)
Calculate the CPU execution time.

---

## Question 4 — Amdahl’s law (5 points)

A program spends 75% of its original execution time performing multiplication.

### a. (2 points)
If multiplication is made four times faster, calculate the overall speedup.

### b. (1 point)
Calculate the new execution time if the original execution time was 20 seconds.

### c. (2 points)
What is the maximum possible speedup if multiplication becomes infinitely fast? Explain why the speedup is limited.

---

## Question 5 — Parallel execution with overhead (5 points)

A program takes 120 seconds on one processor. With `p` processors, the execution time is:

```text
T(p) = 120/p + 3 seconds
```

Calculate the following for `p = 2, 4, 8, 16, 32`:

### a. (3 points)
The execution time for each processor count.

### b. (1 point)
The speedup relative to one processor.

### c. (1 point)
The ratio of actual speedup to ideal speedup. State what happens as the number of processors increases.

---

## Question 6 — Dynamic power and the Power Wall (5 points)

Use the power model:

```text
Power = C × f × V²
```

where `C = 5 mA/MHz`.

Voltage is calculated by:

```text
V = frequency/5 + 0.4
```

with frequency measured in GHz.

### a. (2 points)
For one core operating at 3 GHz, calculate the voltage and power consumption.

### b. (2 points)
For one core operating at 500 MHz, calculate the voltage and power consumption.

### c. (1 point)
Explain why reducing frequency and voltage can greatly reduce power, and explain how the Power Wall influenced the move toward multicore processors.

---

## Bonus — Combined performance change (2 points)

A new compiler reduces instruction count to 60% of its original value but increases CPI by 10%. Clock rate is unchanged.

Calculate the ratio:

```text
New execution time / Old execution time
```

State whether execution becomes faster or slower, and by what percentage.

---

## Submission checklist

Before sending your answers:

- [ ] Write the formula before substituting values.
- [ ] Include units.
- [ ] Show intermediate calculations.
- [ ] State which computer is faster and why.
- [ ] Explain conceptual answers in your own words.

