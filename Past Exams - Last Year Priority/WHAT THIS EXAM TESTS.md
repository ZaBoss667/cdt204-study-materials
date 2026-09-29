# Final Exam Analysis — CDT204 TEN1 260611

## Format

- Total: 65 points
- Grade 3: 33 points
- Grade 4: 46 points
- Grade 5: 59 points
- Full calculations, assumptions, approximations, explanations, and diagrams are expected.

## What the exam actually emphasizes

| Question | Points | Topic | Lesson connection |
|---|---:|---|---|
| 1 | 6 | Flynn taxonomy and parallel architectures | Lesson 1 / later multiprocessing |
| 2 | 9 | Cache organization calculations | Later memory lessons |
| 3 | 8 | Branch prediction | Lesson 3 / later pipelining |
| 4 | 7 | Direct-mapped cache calculations and tracing | Later memory lessons |
| 5 | 6 | MIPS loop tracing and C translation | Lesson 2 |
| 6 | 10 | Multicore execution time and power | Lesson 1 / later multiprocessing |
| 7 | 7 | Cache mapping and misses | Later memory lessons |
| 8 | 12 | Datapath control for new instructions | Lesson 3 |

## Priority order

1. Datapath and control — 12 points
2. Cache calculations and tracing — 23 points
3. Multicore performance and power — 10 points
4. Branch prediction — 8 points
5. MIPS tracing and C translation — 6 points
6. Flynn taxonomy — 6 points

## Lesson 1 material tested

- Parallelism and Flynn taxonomy
- Execution time: `IC × CPI × Cycle Time`
- Multicore speedup when CPI changes with core count
- Power as a function of frequency and voltage
- Power/performance tradeoffs

For the exam's power model, use the formula given in the question. In last year's exam:

`Power = C × f × V²`

`Voltage = frequency/5 + 0.4`, with frequency in GHz.

Do not automatically substitute the textbook's `½CV²f` formula when the exam provides a different model.

## Lesson 2 material tested

Question 5 tests:

- Register initialization
- Integer division in a loop
- Loop termination
- Counting iterations
- Translating MIPS control flow into C

The exam program gives:

```c
int s0 = 0;
int s1 = 1;
int s2 = 256;
while (s2 != s1) {
    s2 = s2 / 2;
    s0++;
}
```

The final value is `s0 = 8`.

## Lesson 3 material tested

Question 8 tests whether you can derive control signals for unfamiliar instructions. Do not only memorize the standard `lw`, `sw`, and R-type table.

For every custom instruction:

1. Identify register inputs.
2. Identify immediate inputs.
3. Identify whether memory is read or written.
4. Identify the ALU operation.
5. Identify whether a register is written.
6. Identify the destination register.
7. Mark unused controls as `X` only when their outputs are irrelevant.

Question 3 tests:

- Always-taken and always-not-taken accuracy
- Two-bit saturating predictors
- Repeating branch patterns
- Designing a predictor using history or a finite-state cycle

## Cache formulas to learn next

- `Block bytes = 2^(offset bits)`
- `Number of sets = 2^(index bits)`
- `Cache size = sets × ways × block bytes`
- `Tag bits = address bits − index bits − offset bits`
- `Address block number = address / block bytes`
- `Set index = block number mod number of sets`
- A direct-mapped cache has one possible line for each block.
- A miss occurs when the valid bit is zero or the stored tag differs.

For implementation-bit ratios, include:

- Data bits
- Tag bits
- Valid bits
- Any replacement/metadata bits specified in the question

## One-month implication

Do not wait until Lesson 1 feels perfect before moving forward. Use a spiral schedule:

- Daily: 30–45 minutes repairing Lesson 1 fundamentals
- Main study block: current later lesson
- Daily practice: one MIPS/C debugging or code-completion task
- Weekly: one timed exam section

The final exam shows that caches and datapath/control deserve the largest later study blocks.
