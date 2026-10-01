# Lesson 2 — What You Need to Learn

## Textbook

Sixth edition: §§2.1–2.10 and §2.22. Review §2.12 for compiler/assembler/linker/loader concepts. Sixth-edition §2.20 is additional matrix-multiply material.

## Checklist

- [ ] Define ISA, microarchitecture, and hardware implementation.
- [ ] Compare stack, accumulator, register-memory, and register-register ISAs.
- [ ] Compare RISC and CISC design tendencies.
- [ ] Explain MIPS design principles: regularity, smaller is faster, common-case optimization, and compromise.
- [ ] Memorize the MIPS register conventions: `$zero`, `$a`, `$v`, `$t`, `$s`, `$sp`, `$fp`, `$gp`, and `$ra`.
- [ ] Translate simple C arithmetic into MIPS.
- [ ] Explain why MIPS arithmetic uses registers rather than memory operands.
- [ ] Translate array accesses into byte offsets.
- [ ] Explain alignment and big-endian versus little-endian storage.
- [ ] Convert binary, decimal, and hexadecimal values.
- [ ] Convert signed values using two’s complement.
- [ ] Know unsigned and signed n-bit ranges.
- [ ] Perform zero extension and sign extension.
- [ ] Perform AND, OR, XOR, NOT, logical shifts, and arithmetic right shifts.
- [ ] Explain immediate-extension rules for arithmetic, memory, and logical instructions.
- [ ] Translate if-statements and loops into MIPS using `beq`, `bne`, `slt`, `slti`, and `j`.
- [ ] Explain `jal`, `jr`, `$ra`, `$sp`, caller-saved registers, and callee-saved registers.
- [ ] Explain pseudoinstructions and how the assembler expands them.
- [ ] Memorize R-, I-, and J-format fields.
- [ ] Encode assembly instructions into 32-bit machine code.
- [ ] Decode 32-bit machine code into assembly.
- [ ] Calculate branch targets using `PC + 4 + (sign-extended immediate << 2)`.
- [ ] Calculate jump targets using the upper four bits of `PC + 4`, the 26-bit index, and two zero bits.
- [ ] Load a 32-bit constant using `lui` and `ori`.
- [ ] Explain the compiler–assembler–linker–loader sequence.

## Minimum practice

- [ ] Encode `add $t0,$s1,$s2`.
- [ ] Encode an `lw` instruction with a decimal offset.
- [ ] Decode an R-format instruction.
- [ ] Convert positive and negative 8-bit values.
- [ ] Convert binary to hexadecimal by grouping four bits.
- [ ] Translate an array expression into MIPS.
- [ ] Translate a loop into MIPS and count its instructions.
- [ ] Calculate a branch offset.
- [ ] Trace a procedure call and return.
