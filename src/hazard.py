class HazardDetectionUnit:
    def __init__(self):
        self.stall = False

    def detect_hazard(self, decode_stage, execute_stage, mem_stage):
        """
        Detects data hazards and determines if a stall is needed.
        """
        if execute_stage and "rd" in execute_stage and decode_stage:
            if execute_stage["rd"] != 0 and (
                execute_stage["rd"] == decode_stage.get("rs1", -1) or execute_stage["rd"] == decode_stage.get("rs2", -1)
            ):
                self.stall = True
                return True  # Stall needed

        if mem_stage and "rd" in mem_stage and decode_stage:
            if mem_stage["rd"] != 0 and (
                mem_stage["rd"] == decode_stage.get("rs1", -1) or mem_stage["rd"] == decode_stage.get("rs2", -1)
            ):
                self.stall = True
                return True  # Stall needed

        self.stall = False
        return False  # No stall needed

    def should_stall(self):
        """
        Returns whether the pipeline should stall.
        """
        return self.stall
