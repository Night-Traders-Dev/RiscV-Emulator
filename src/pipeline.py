class Pipeline:
    def __init__(self):
        """
        Initialize the pipeline stages.
        """
        self.if_stage = None  # Instruction Fetch
        self.id_stage = None  # Instruction Decode
        self.ex_stage = None  # Execute
        self.mem_stage = None  # Memory Access
        self.wb_stage = None  # Write Back


    def step(self, instruction, decoder, executor, memory, registers):
        """
        Simulates one step of the pipeline, moving instructions through stages.
        """
        # Write-back stage
        if self.wb_stage is not None:
            registers[int(self.wb_stage["rd"])] = self.wb_stage["value"]

        # Memory stage
        self.wb_stage = self.mem_stage

        # Execute stage
        if self.ex_stage is not None:
            self.mem_stage = executor.execute(self.ex_stage)

        # Decode stage
        if self.id_stage is not None:
            self.ex_stage = decoder.decode(self.id_stage)

        # Fetch stage
        self.id_stage = instruction  # Pass the instruction to decode


    def fetch(self, instruction):
        """
        Fetch stage: Retrieves the instruction.
        """
        self.if_stage = instruction

    def decode(self, decoder):
        """
        Decode stage: Decodes the instruction.
        """
        if self.if_stage is not None:
            self.id_stage = decoder.decode(self.if_stage)

    def execute(self, executor):
        """
        Execute stage: Executes the decoded instruction.
        """
        if self.id_stage is not None:
            self.ex_stage = executor.execute(self.id_stage)

    def memory_access(self, memory):
        """
        Memory stage: Handles memory-related instructions.
        """
        if self.ex_stage is not None:
            self.mem_stage = self.ex_stage  # Placeholder for memory operations


def write_back(self, registers):
    """
    Write-back stage: Writes results back to registers.
    """
    if self.mem_stage is not None:
        rd = int(self.mem_stage["rd"])  # Ensure rd is an integer
        registers[rd] = self.mem_stage["value"]


