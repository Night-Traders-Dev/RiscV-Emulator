from cpu import CPU

def main():
    print("Starting CPU execution with pipeline...")
    
    # Define test programs
    test_programs = [
        b'\x0A\x00\x05\x13',  # Test 1: ADDI x10, x0, 10
        b'\x0A\x00\x05\x13' b'\x14\x00\x06\x13' b'\x00\xA6\x06\x33' b'\x40\xA6\x06\x33',  # Test 2: ADD/SUB
        b'\xFF\x0F\x07\x13' b'\xAA\xAA\x07\x13' b'\x55\x55\x07\x13',  # Test 3: ANDI, ORI, XORI
        b'\x0A\x00\x05\x13' b'\x00\x00\xA2\x23' b'\x00\x00\x25\x03',  # Test 4: LW, SW
        b'\x0A\x00\x05\x13' b'\x0A\x00\x06\x13' b'\x00\xA5\x63\x63' b'\xFF\xFF\xE0\xEF'  # Test 5: BEQ, JAL
    ]

    for i, program in enumerate(test_programs):
        print(f"Running Test Program {i + 1}...")
        cpu = CPU()
        cpu.load_program(program)
        cpu.run()
        print(f"Test Program {i + 1} completed.\n")
        print(f"CPU Counter: {cpu.pc}\n")


if __name__ == "__main__":
    main()
