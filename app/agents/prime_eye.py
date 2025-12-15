import hashlib
import json
from pathlib import Path


class PrimeEye:
    """
    Read-only oversight agent.
    Scans artifacts and ledger events for integrity, drift, and violations.
    """

    def __init__(self, ledger_path: str = "ledger/ledger.jsonl"):
        self.ledger_path = Path(ledger_path)

    def _hash_payload(self, payload: dict) -> str:
        data = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(data).hexdigest()

    def scan_artifact(self, artifact_path: str, expected_hash: str) -> bool:
        """
        Verifies artifact integrity against expected hash.
        """
        path = Path(artifact_path)
        if not path.exists():
            raise FileNotFoundError(f"Artifact not found: {artifact_path}")

        content = path.read_bytes()
        actual_hash = hashlib.sha256(content).hexdigest()
        return actual_hash == expected_hash

    def scan_ledger(self) -> list:
        """
        Returns all ledger events for inspection.
        """
        if not self.ledger_path.exists():
            return []

        events = []
        with self.ledger_path.open("r", encoding="utf-8") as f:
            for line in f:
                events.append(json.loads(line))
        return events

    def detect_drift(self, event: dict) -> bool:
        """
        Detects hash mismatches or missing lineage pointers.
        """
        expected = event.get("event_hash")
        recalculated = self._hash_payload({
            "task_id": event.get("task_id"),
            "event_type": event.get("event_type"),
            "actor": event.get("actor"),
            "timestamp": event.get("timestamp"),
            "payload": event.get("payload"),
            "previous_hash": event.get("previous_hash"),
        })
        return expected != recalculated
