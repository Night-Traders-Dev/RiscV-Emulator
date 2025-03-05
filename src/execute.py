class Executor:
    def __init__(self, registers):
        """
        Initialize the executor with CPU registers.
        """
        self.registers = registers

    def execute(self, decoded):
        """
        Execute a decoded RISC-V instruction.
        """
        opcode = decoded["opcode"]
        funct3 = decoded["funct3"]
        funct7 = decoded["funct7"]
        rd = decoded["rd"]
        rs1 = decoded["rs1"]
        rs2 = decoded["rs2"]
        imm_i = decoded["imm_i"]

        if opcode == 0x13:  # I-type (ADDI, ANDI, ORI, etc.)
            if funct3 == 0x0:  # ADDI
                self.registers[rd] = self.registers[rs1] + imm_i
            elif funct3 == 0x7:  # ANDI
                self.registers[rd] = self.registers[rs1] & imm_i
            elif funct3 == 0x6:  # ORI
                self.registers[rd] = self.registers[rs1] | imm_i

        elif opcode == 0x33:  # R-type (ADD, SUB, AND, OR)
            if funct3 == 0x0:
                if funct7 == 0x00:  # ADD
                    self.registers[rd] = self.registers[rs1] + self.registers[rs2]
                elif funct7 == 0x20:  # SUB
                    self.registers[rd] = self.registers[rs1] - self.registers[rs2]
            elif funct3 == 0x7:  # AND
                self.registers[rd] = self.registers[rs1] & self.registers[rs2]
            elif funct3 == 0x6:  # OR
                self.registers[rd] = self.registers[rs1] | self.registers[rs2]

        print(f"Executed: opcode={opcode}, rd={rd}, value={self.registers[rd]}")
        return self.registers
