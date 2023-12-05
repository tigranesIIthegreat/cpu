# Project Title: 8-bit CPU Implementation

## Description
This project aims to implement an 8-bit CPU utilizing a simple Instruction Set Architecture (ISA) consisting of 16 instructions. The CPU architecture is designed to handle basic operations and computations using minimal instructions.

## Features
- **8-bit CPU**: Designed to operate with 8-bit data and instructions.
- **Simple ISA**: Consists of 16 fundamental instructions to perform basic aarithmetic, logic and control-flow operations.

## Instructions planned to be implemented
The ISA includes the following set of instructions:
1. `LOAD reg mem`: Load a value from memory to a register.
2. `LOADI reg imm`: Load an immediate value to a register.
3. `STORE reg mem`: Store a value from a register to memory.
4. `JMP mem`: Unconditional jump to a specified memory address.
5. `JZ mem`: Jump if the zero flag is set.
6. `MOV reg reg`: Copy the contents of one register into another.
7. `ADD reg reg`: Add two values and store the result.
8. `SUB reg reg`: Subtract two values and store the result.
9. `AND reg reg`: Bitwise AND operation.
10. `INC reg`: Increment a value by one.
11. `DEC reg`: Decrement a value by one.
12. `OR reg reg`: Bitwise OR operation.
13. `XOR reg reg`: Bitwise XOR operation.
14. `SHL reg`: Shift left the bits of a register by one.
15. `SHR reg`: Shift right the bits of a register by one.
16. `CMP reg reg`: Compare the bits of two registers, 
set zero_flag to one if the values are equal

## Usage
To simulate and test the CPU:
1. Clone the repository: `git clone https://github.com/tigranesIIthegreat/cpu`
2. Have icarus verilog and python3 installed on the machine.
3. Navigate to the project directory.
4. Run `scripts/main.py` to compile, simulate and check.

## Current state
Only ALU and memory modules are designed and checked for now.