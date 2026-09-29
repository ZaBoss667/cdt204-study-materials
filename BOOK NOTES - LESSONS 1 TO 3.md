# Textbook Notes for Lessons 1–3

Source: *Computer Organization and Design: The Hardware/Software Interface*, MIPS Edition, Sixth Edition.

These notes map the supplied fifth-edition reading guide to the sixth-edition textbook by topic. They cover only the material supporting Lectures 1–3.

## Reading map

| Lesson | Sixth-edition sections |
|---|---|
| Lesson 1 — Introduction and Performance | §§1.1–1.4, 1.6, 1.8–1.12 |
| Lesson 2 — ISA | §§2.1–2.10, 2.12, 2.21–2.22 |
| Lesson 3 — Datapath and Pipelining | §§4.1–4.4 and §4.6 |
| Supporting arithmetic | Chapter 3, especially §3.2 |

Sixth-edition §4.5 is the multicycle implementation. The pipeline overview covered by Lecture 3 is §4.6.

---

# Lesson 1 — Introduction and Performance

## Seven great ideas

1. **Use abstraction to simplify design:** hide lower-level details behind simpler interfaces.
2. **Make the common case fast:** improving frequent operations normally matters more than optimizing rare ones.
3. **Performance via parallelism:** perform multiple operations simultaneously.
4. **Performance via pipelining:** overlap stages of different operations.
5. **Performance via prediction:** guess likely outcomes and recover when the guess is wrong.
6. **Hierarchy of memories:** combine small fast memories with larger slower memories.
7. **Dependability via redundancy:** use additional components or information to detect and survive failures.

## Hardware/software abstraction

- The ISA is the interface between hardware and low-level software.
- The ABI combines the user-visible ISA with operating-system conventions.
- Different processor implementations can execute the same ISA while having different performance and cost.
- The five classic computer components are input, output, memory, datapath, and control.

## Performance definitions

- **Response time / execution time:** total time required to complete one task.
- **Throughput:** tasks completed per unit time.
- **Elapsed time:** wall-clock time, including I/O and operating-system delays.
- **CPU time:** time the processor spends working on the task.

For a fixed task:

```text
Performance = 1 / Execution Time
Speedup of X over Y = Execution Time Y / Execution Time X
```

## CPU performance equation

```text
CPU Time = IC × CPI × Cycle Time
CPU Time = (IC × CPI) / Clock Rate
Clock Cycles = IC × CPI
Cycle Time = 1 / Clock Rate
```

- IC is the dynamic instruction count.
- CPI is the average number of cycles per executed instruction.
- Clock rate alone does not determine performance.

For instruction classes:

```text
Average CPI = Σ(Fraction_i × CPI_i)
```

## Complete comparison rule

```text
New Time / Old Time
= (New IC / Old IC)
× (New CPI / Old CPI)
× (Old Clock Rate / New Clock Rate)
```

## MIPS metric

```text
MIPS = IC / (Execution Time × 10^6)
MIPS = Clock Rate / (CPI × 10^6)
```

MIPS is unreliable because:

- Different ISAs perform different amounts of work per instruction.
- CPI and MIPS vary by program and instruction mix.
- A higher instruction-execution rate can accompany a longer total execution time.

## Amdahl’s law

If fraction `p` of the original execution time is improved by factor `s`:

```text
Overall Speedup = 1 / ((1 − p) + p/s)
Maximum Speedup = 1 / (1 − p)
```

The portion that is not improved limits total speedup.

## Benchmarks

```text
SPECratio = Reference Time / Measured Time
```

Use the geometric mean to summarize normalized performance ratios. Benchmarks are useful only when they represent the relevant workload.

## Power wall

A common dynamic-power model is:

```text
Pdynamic = 1/2 × C × V^2 × f
```

Some exam questions provide a model without the `1/2`; always use the model stated in the question.

- Frequency and switching activity increase power.
- Voltage has a squared effect on dynamic power.
- Voltage could not continue falling enough to offset higher frequencies and transistor counts.
- Heat removal and energy consumption constrained further frequency growth.
- Industry shifted toward multicore processors and parallel execution.

---

# Lesson 2 — ISA and MIPS

## Core design principles

1. Simplicity favors regularity.
2. Smaller is faster.
3. Make the common case fast.
4. Good design demands good compromises.

MIPS is a load/store architecture: arithmetic operates on registers; explicit load and store instructions access memory.

## Registers and memory

- 32 general-purpose registers, each 32 bits wide.
- Register selectors require 5 bits.
- `$zero` always reads as zero.
- `$t` registers are temporary/caller-saved.
- `$s` registers are preserved by a callee when used.
- `$a0–$a3` carry arguments; `$v0–$v1` carry results.
- `$sp` is the stack pointer and `$ra` is the return address.

For a 32-bit integer array:

```text
Address(A[i]) = Base(A) + 4i
```

MIPS memory is byte-addressed. A word contains four bytes and normally begins at an address divisible by four.

## Binary representation

Unsigned n-bit range:

```text
0 to 2^n − 1
```

Two’s-complement n-bit range:

```text
−2^(n−1) to 2^(n−1) − 1
```

To negate a fixed-width two’s-complement number, invert every bit and add one.

- Zero extension inserts leading zeros.
- Sign extension repeats the original sign bit.
- Logical immediates such as `andi` and `ori` are zero-extended.
- Arithmetic and address immediates are normally sign-extended.

## Instruction formats

```text
R: op(6) rs(5) rt(5) rd(5) shamt(5) funct(6)
I: op(6) rs(5) rt(5) immediate(16)
J: op(6) target(26)
```

Branch target:

```text
Target = PC + 4 + (SignExtend(immediate) << 2)
immediate = (Target − (PC + 4)) / 4
```

Jump target:

```text
Target = {(PC + 4)[31:28], target_field, 00}
```

## Program translation

```text
Source → Compiler → Assembly → Assembler → Object file
→ Linker → Executable → Loader → Running program
```

Pseudoinstructions are assembler conveniences expanded into real machine instructions.

---

# Lesson 3 — Datapath and Pipelining

## Logic foundations

- Combinational logic depends only on current inputs.
- Sequential logic contains state.
- Multiplexers choose one input according to a control signal.
- Edge-triggered state elements update on a clock edge.
- Half adder: `Sum = A XOR B`, `Carry = A AND B`.

## Datapath components

- Program counter
- Instruction memory
- Register file
- ALU
- Data memory
- Sign extender
- Adders
- Multiplexers
- Control unit

## Instruction behavior

| Instruction | ALU purpose | Memory | Register write |
|---|---|---|---|
| R-type | Arithmetic/logical operation | None | ALU result to `rd` |
| `lw` | Base plus offset | Read | Memory value to `rt` |
| `sw` | Base plus offset | Write | None |
| `beq` | Subtract operands for equality | None | None |

Important control signals include `RegDst`, `ALUSrc`, `MemtoReg`, `RegWrite`, `MemRead`, `MemWrite`, `Branch`, and `ALUOp`.

```text
PCSrc = Branch AND Zero
```

## Single-cycle implementation

- Every instruction takes one long clock cycle.
- The longest path determines the period.
- A load usually determines the critical path: instruction memory, register file, ALU, data memory, register write.
- CPI = 1 does not guarantee good performance when the clock period is long.

## Five-stage pipeline

1. IF — instruction fetch
2. ID — decode and register read
3. EX — execute or calculate address
4. MEM — data-memory access
5. WB — register write-back

For `n` instructions and `k` stages without stalls:

```text
Cycles = n + k − 1
```

With `B` additional stall or flush cycles:

```text
Total Time = (n + k − 1 + B) × Pipeline Cycle Time
```

Pipelining improves instruction throughput, not the latency of one instruction.

## Hazards

- **Structural hazard:** two operations require the same unavailable resource.
- **Data hazard:** a consumer needs a result that is not yet available.
- **Control hazard:** the correct next instruction is unknown after a branch.

Forwarding can send an ALU result directly to a dependent instruction. A load-use dependence normally still needs one stall because loaded data becomes available too late for the following instruction’s EX stage.

Branch prediction avoids waiting for every branch. A misprediction requires discarding wrong-path work and fetching from the correct address.

---

# Supporting Chapter 3 facts

- Signed overflow is not the same as carry-out.
- Addition overflows when equal-sign operands produce a result with the opposite sign.
- A full n-bit by n-bit product may require 2n bits.
- IEEE 754 single precision uses 1 sign bit, 8 exponent bits, and 23 fraction bits.
- Floating-point values have limited precision, so addition is not always associative.
