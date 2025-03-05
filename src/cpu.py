from decoder import Decoder
from execute import Executor
from memory import Memory
from pipeline import Pipeline

class CPU:
    def __init__(self, memory_size=1024):
        """
        Initialize the RISC-V CPU with registers, memory, and pipeline.
        """
        self.registers = [0] * 32  # 32 general-purpose registers
        self.pc = 0  # Program Counter (PC)
        self.memory = Memory(memory_size)  # Memory management
        self.decoder = Decoder()  # Initialize the instruction decoder
        self.executor = Executor(self.registers)  # Initialize the instruction executor
        self.pipeline = Pipeline()  # Initialize the pipeline

    def load_program(self, program, start_address=0):
        """
        Load a program (byte array) into memory at the specified address.
        """
        for i, byte in enumerate(program):
            self.memory.store(start_address + i, byte, size=1)
        self.pc = start_address

    def fetch(self):
        """
        Fetch the next instruction from memory.
        """
        instruction = self.memory.load(self.pc)
        self.pc += 4  # Advance the program counter
        return instruction

    def run(self, max_instructions=100):
        """
        Run the CPU, executing instructions through the pipeline.
        """
        for _ in range(max_instructions):
            instruction = self.fetch()
            if instruction == 0:  # Stop on a zero instruction (NOP or halt)
                break
            self.pipeline.step(instruction, self.decoder, self.executor, self.memory, self.registers)

