import json
import hashlib
from datetime import datetime
from pathlib import Path


class LedgerLogger:
    """
    Immutable ledger logger.
    Appends every system event with hash, timestamp, and lineage.
    """

    def __init__(self, ledger_path: str = "ledger/ledger.jsonl"):
        self.ledger_path = Path(ledger_path)
        self.ledger_path.parent.mkdir(parents=True, exist_ok=True)

    def _hash_event(self, event: dict) -> str:
        payload = json.dumps(event, sort_keys=True).encode("utf-8")
        return hashlib.sha256(payload).hexdigest()

    def log_event(
        self,
        task_id: str,
        event_type: str,
        actor: str,
        payload: dict,
        previous_hash: str | None = None,
    ) -> dict:
        """
        Logs an immutable ledger event.
        """

        event = {
            "task_id": task_id,
            "event_type": event_type,
            "actor": actor,
            "timestamp": datetime.utcnow().isoformat(),
            "payload": payload,
            "previous_hash": previous_hash,
        }

        event["event_hash"] = self._hash_event(event)

        with self.ledger_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")

        return event
