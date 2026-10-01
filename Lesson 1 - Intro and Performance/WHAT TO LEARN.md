# Lesson 1 — What You Need to Learn

## Textbook

Sixth edition: §§1.1–1.4, 1.6, 1.8, 1.11–1.12. Also understand the performance material in §1.9. Review §1.2 carefully.

## Checklist

- [ ] Recite and explain the 7 Great Ideas:
  - [ ] Abstraction
  - [ ] Make the common case fast
  - [ ] Performance via parallelism
  - [ ] Performance via pipelining
  - [ ] Performance via prediction
  - [ ] Hierarchy of memories
  - [ ] Dependability via redundancy
- [ ] Explain the ISA as the hardware/software interface.
- [ ] Identify the five classic computer components: input, output, memory, datapath, and control.
- [ ] Explain the path from high-level code to a running program.
- [ ] Distinguish response time, elapsed time, CPU time, and throughput.
- [ ] Write from memory:
  - [ ] `CPU Time = IC × CPI × Cycle Time`
  - [ ] `CPU Time = (IC × CPI) / Clock Rate`
- [ ] Given IC, CPI, and clock rate, calculate CPU execution time.
- [ ] Convert between clock rate and cycle time.
- [ ] Compare two machines and calculate speedup:
  - [ ] `Speedup = slower execution time / faster execution time`
- [ ] Given instruction classes and their frequencies, calculate average CPI:
  - [ ] `Average CPI = Σ(fractionᵢ × CPIᵢ)`
- [ ] Explain why execution time is the reliable performance measure.
- [ ] Explain why IC, CPI, clock rate, and MIPS alone can be misleading.
- [ ] State and explain:
  - [ ] `MIPS = IC / (Execution Time × 10⁶)`
  - [ ] Why MIPS is unreliable across different ISAs and programs.
- [ ] Explain benchmark ratios and why geometric mean is used for normalized ratios.
- [ ] Apply Amdahl’s law:
  - [ ] `Speedup = 1 / ((1 − p) + p/s)`
- [ ] State dynamic power:
  - [ ] `Pdynamic = ½CV²f`
- [ ] Explain the Power Wall: frequency, switching activity, voltage, heat, and the shift toward multicore processors.
- [ ] Explain the difference between parallelism, pipelining, and prediction.

## Minimum practice

- [ ] Solve the Lecture 1 CPI example.
- [ ] Solve the Lecture 1 machine-time exercise.
- [ ] Solve weighted-CPI comparisons.
- [ ] Solve one speedup problem.
- [ ] Solve one Amdahl’s-law problem.
- [ ] Solve one MIPS-versus-execution-time problem.
- [ ] Explain the Power Wall without notes.
