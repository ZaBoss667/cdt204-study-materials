# Lesson 3 — What You Need to Learn

## Textbook

Sixth edition: §§4.1–4.4 and §4.6. Review §4.5 for the multicycle implementation. Chapter 3 is supporting background, especially §3.2.

## Checklist

- [ ] Distinguish combinational logic from sequential/state logic.
- [ ] Know the truth tables and uses of AND, OR, XOR, and NOT.
- [ ] Explain a half adder:
  - [ ] `Sum = A XOR B`
  - [ ] `Carry = A AND B`
- [ ] Explain multiplexers and control selection.
- [ ] Explain D flip-flops/registers and edge-triggered clocking.
- [ ] Identify the datapath components: PC, instruction memory, register file, ALU, data memory, sign extender, adders, multiplexers, and control.
- [ ] Trace an R-type instruction through the datapath.
- [ ] Trace `lw` and `sw` through the datapath.
- [ ] Trace `beq` through the datapath.
- [ ] Explain how `Zero` and `Branch` select the next PC.
- [ ] Explain the control signals `RegDst`, `ALUSrc`, `MemtoReg`, `RegWrite`, `MemRead`, `MemWrite`, `Branch`, and `ALUOp`.
- [ ] Reconstruct the single-cycle control table.
- [ ] Explain why the load instruction determines the single-cycle critical path.
- [ ] Explain why single-cycle designs need separate instruction and data memories.
- [ ] Explain why a single-cycle CPI of 1 does not guarantee good performance.
- [ ] Define pipelining, stage, throughput, latency, fill time, and drain time.
- [ ] Know the five MIPS pipeline stages: IF, ID, EX, MEM, and WB.
- [ ] Calculate pipeline clock period and total execution time.
- [ ] Explain why pipeline speedup approaches the number of balanced stages only for long instruction streams.
- [ ] Identify structural, data, and control hazards.
- [ ] Explain forwarding/bypassing.
- [ ] Identify the load-use hazard and insert the required stall.
- [ ] Explain instruction scheduling to avoid stalls.
- [ ] Explain branch stalls, branch prediction, and misprediction recovery.
- [ ] Explain why pipelining improves throughput rather than individual instruction latency.

## Minimum practice

- [ ] Fill in the control table for R-type, `lw`, `sw`, and `beq`.
- [ ] Draw the datapath path for each of those four instructions.
- [ ] Calculate a single-cycle critical path.
- [ ] Calculate the completion time for a finite instruction sequence in a five-stage pipeline.
- [ ] Draw an ALU-to-ALU forwarding path.
- [ ] Draw a load-use hazard with one bubble.
- [ ] Reorder instructions to remove avoidable stalls.
- [ ] Calculate the effect of branch stalls or mispredictions on CPI.
