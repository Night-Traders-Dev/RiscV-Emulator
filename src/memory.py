class Memory:
    def __init__(self, size=1024):
        """
        Initialize memory with the given size.
        """
        self.memory = bytearray(size)

    def load(self, address, size=4):
        """
        Load a word (default 4 bytes) from memory at the specified address.
        """
        return int.from_bytes(self.memory[address:address + size], 'little')

    def store(self, address, value, size=4):
        """
        Store a word (default 4 bytes) into memory at the specified address.
        """
        self.memory[address:address + size] = value.to_bytes(size, 'little')
