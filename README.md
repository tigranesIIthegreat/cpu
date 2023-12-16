# Project Title: 8-bit CPU Implementation

## Description
This project aims to implement an 8-bit CPU utilizing a simple Instruction Set Architecture (ISA) consisting of 16 instructions. The CPU architecture is designed to handle basic operations and computations using minimal instructions.

## Features
- **8-bit CPU**: Designed to operate with 8-bit data and instructions.
- **Simple ISA**: Consists of 16 fundamental instructions to perform basic aarithmetic, logic and control-flow operations.

## Instructions planned to be implemented
The ISA includes the following set of instructions:
1. `ADD reg reg`: Add two values and store the result.
2. `SUB reg reg`: Subtract two values and store the result.
3. `INC reg`: Increment a value by one.
4. `DEC reg`: Decrement a value by one.
5. `AND reg reg`: Bitwise AND operation.
6. `OR reg reg`: Bitwise OR operation.
7. `XOR reg reg`: Bitwise XOR operation.
8. `SHL reg`: Shift left the bits of a register by one.
9. `SHR reg`: Shift right the bits of a register by one.
10. `CMP reg reg`: Compare the bits of two registers, 
set zero_flag to one if the values are equal
11. `MOV reg reg`: Copy the contents of one register into another.
12. `LOAD reg mem`: Load a value from memory to a register.
13. `LOADI reg imm`: Load an immediate value to a register.
14. `STORE reg mem`: Store a value from a register to memory.
15. `JMP mem`: Unconditional jump to a specified memory address.
16. `JZ mem`: Jump if the zero flag is set.

## Usage
To simulate and test the CPU:
1. Clone the repository: `git clone https://github.com/tigranesIIthegreat/cpu`
2. Have icarus verilog and python3 installed on the machine.
3. Navigate to the project directory.
4. Run `scripts/main.py` to compile, simulate and check.

## Current state
Only ALU, memory, program counter, instruction decoder modules are designed and checked for now.