class Decoder:
    def decode(self, instruction):
        """
        Decode a 32-bit RISC-V instruction.
        """
        opcode = instruction & 0x7F
        rd = (instruction >> 7) & 0x1F
        funct3 = (instruction >> 12) & 0x7
        rs1 = (instruction >> 15) & 0x1F
        rs2 = (instruction >> 20) & 0x1F
        funct7 = (instruction >> 25) & 0x7F
        imm_i = (instruction >> 20) & 0xFFF
        imm_s = ((instruction >> 25) << 5) | ((instruction >> 7) & 0x1F)
        imm_b = ((instruction >> 31) << 12) | (((instruction >> 7) & 1) << 11) | (((instruction >> 25) & 0x3F) << 5) | (((instruction >> 8) & 0xF) << 1)
        imm_u = instruction & 0xFFFFF000
        imm_j = ((instruction >> 31) << 20) | (((instruction >> 12) & 0xFF) << 12) | (((instruction >> 20) & 1) << 11) | (((instruction >> 21) & 0x3FF) << 1)

        return {
            "opcode": opcode,
            "rd": rd,
            "funct3": funct3,
            "rs1": rs1,
            "rs2": rs2,
            "funct7": funct7,
            "imm_i": imm_i,
            "imm_s": imm_s,
            "imm_b": imm_b,
            "imm_u": imm_u,
            "imm_j": imm_j,
        }
