class Registers:
    def __init__(self):
        """
        Initialize 32 registers (x0 to x31) with all values set to 0.
        """
        self.registers = [0] * 32

    def read(self, reg_num):
        """
        Read the value from a register.
        x0 is hardwired to 0 and always returns 0.
        """
        if reg_num == 0:
            return 0
        return self.registers[reg_num]

    def write(self, reg_num, value):
        """
        Write a value to a register. x0 cannot be modified.
        """
        if reg_num != 0:
            self.registers[reg_num] = value

    def dump(self):
        """
        Print the register values for debugging.
        """
        for i in range(0, 32, 4):
            print(
                f"x{i}: {self.registers[i]:08x}  x{i+1}: {self.registers[i+1]:08x}  "
                f"x{i+2}: {self.registers[i+2]:08x}  x{i+3}: {self.registers[i+3]:08x}"
            )
