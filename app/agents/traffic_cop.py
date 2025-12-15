from enum import Enum

class TaskState(Enum):
    NEW = "NEW"
    SR1_PENDING = "SR1_PENDING"
    SR2_PENDING = "SR2_PENDING"
    SR3_PENDING = "SR3_PENDING"
    SPS_READY = "SPS_READY"
    CUFFED = "CUFFED"
    RELEASED = "RELEASED"
    RECYCLE = "RECYCLE"  # Added per governance validation


class TrafficCop:
    """
    Enforces all legal task state transitions.
    Returns (True, message) if transition is allowed.
    Returns (False, reason) if blocked.
    """

    def check_transition(self, current_state: str, target_state: str, context: dict = None):
        context = context or {}

        # 0. Rotation Lock (prevents seat capture)
        if context.get("rotation_lock", False):
            return False, "BLOCK: Seat is locked for cool-down."

        # 1. NEW -> SR1
        if current_state == TaskState.NEW.value and target_state == TaskState.SR1_PENDING.value:
            return True, "Task accepted into SR1 cycle."

        # 2. SR1 -> SR2 (requires 3 SR1 artifacts)
        if current_state == TaskState.SR1_PENDING.value and target_state == TaskState.SR2_PENDING.value:
            if context.get("sr1_count", 0) < 3:
                return False, "BLOCK: Waiting for 3 SR1 responses."
            return True, "SR1 complete. Rotating to SR2."

        # 3. SR2 -> SR3 (requires 3 SR2 artifacts)
        if current_state == TaskState.SR2_PENDING.value and target_state == TaskState.SR3_PENDING.value:
            if context.get("sr2_count", 0) < 3:
                return False, "BLOCK: Waiting for 3 SR2 responses."
            return True, "SR2 complete. Rotating to SR3."

        # 4. SR3 -> CUFFED
        if current_state == TaskState.SR3_PENDING.value and target_state == TaskState.CUFFED.value:
            return True, "SR3 complete. Task cuffed for human review."

        # 5. CUFFED -> RELEASED (Human approval + explicit cuff flag)
        if current_state == TaskState.CUFFED.value and target_state == TaskState.RELEASED.value:
            if not context.get("human_approval", False):
                return False, "BLOCK: Human approval required."
            if context.get("cuff_status") != "released":
                return False, "BLOCK: cuff_status must be 'released'."
            return True, "UNLOCK: Vault release authorized."

        # 6. Any -> RECYCLE (requires rejection reason)
        if target_state == TaskState.RECYCLE.value:
            if not context.get("rejection_reason"):
                return False, "BLOCK: Recycle requires a logged rejection reason."
            return True, "RECYCLE: Task returned to queue."

        # Default deny
        return False, f"BLOCK: Illegal transition from {current_state} to {target_state}."
