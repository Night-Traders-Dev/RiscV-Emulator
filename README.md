# RISC-V Emulator in Python

This project is a RISC-V RV32I emulator written in Python 3. It aims to provide an educational tool for understanding how a RISC-V CPU processes instructions, handles memory, and manages a pipeline architecture.

## Features
- Implements the RV32I instruction set.
- Includes a pipeline with instruction fetch, decode, execute, memory, and write-back stages.
- Supports a basic hazard detection mechanism.
- Memory system with load and store functionality.
- Modular structure for CPU, Decoder, Executor, Memory, Pipeline, and Registers.

## Files and Structure
- `main.py` - Entry point for running the emulator.
- `cpu.py` - Manages the CPU components and execution loop.
- `decoder.py` - Decodes RISC-V instructions.
- `execute.py` - Handles the execution of instructions.
- `memory.py` - Manages memory operations including load and store.
- `pipeline.py` - Implements a basic pipeline with forwarding and hazard detection.
- `registers.py` - Implements the register file.
- `hazard.py` - Detects and manages pipeline hazards.

## Running the Emulator
1. Ensure you have Python 3 installed.
2. Run the emulator with:
   ```sh
   python3 main.py
   ```
3. Modify `main.py` to load different test programs.

## Example Test Program
A simple test program that increments a register from 1 to 10:
```python
program = [
    b'\x93\x05\x00\x0A',  # addi x11, x0, 10 (Set x11 to 10)
    b'\x93\x05\x00\x01',  # addi x11, x11, 1 (Increment x11)
]
```

## Future Improvements
- Implement additional RISC-V extensions.
- Improve pipeline hazard handling.
- Add support for more instruction formats.

## License
This project is open-source under the MIT License.

# RiscV-Emulator
