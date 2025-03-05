from cpu import CPU

def main():
    print("Starting RISC-V 1-10 Counter Test...")
    
    # Machine code for a 1-10 counter program
    counter_program = [
        b'\x01\x00\x01\x13',  # ADDI x1, x0, 1  (x1 = 1)
        b'\x0A\x00\x02\x13',  # ADDI x2, x0, 10 (x2 = 10)
        b'\x01\x10\x11\x13',  # ADDI x1, x1, 1  (x1 += 1)
        b'\xFE\x11\x02\x63'   # BNE x1, x2, loop (if x1 != x2, loop)
    ]
    
    # Initialize CPU
    cpu = CPU()
    
    # Load the program into memory
    for i, instruction in enumerate(counter_program):
        cpu.memory.store_word(i * 4, int.from_bytes(instruction, 'little'))
    
    # Run the program
    cpu.run()
    
    print("Counter program finished execution.")
    print(f"Final value of x1: {cpu.registers[1]}")  # Should be 10

if __name__ == "__main__":
    main()
