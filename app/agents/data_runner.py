import shutil
from pathlib import Path
from datetime import datetime


class DataRunner:
    """
    Responsible for moving artifacts between system folders.
    Acts as the courier with full traceability.
    """

    def __init__(self, base_path: str = "artifacts"):
        self.base_path = Path(base_path)

        # Standard system paths
        self.pending = self.base_path / "pending_review"
        self.vault = self.base_path / "vault"
        self.archive = self.base_path / "archive"
        self.carbon = self.base_path / "carbon_copies"

        for path in [self.pending, self.vault, self.archive, self.carbon]:
            path.mkdir(parents=True, exist_ok=True)

    def _timestamp(self) -> str:
        return datetime.utcnow().strftime("%Y%m%d%H%M%S")

    def deliver(self, src: str, dest: str, task_id: str) -> Path:
        """
        Moves an artifact and creates a carbon copy.
        """
        src_path = Path(src)
        if not src_path.exists():
            raise FileNotFoundError(f"Source not found: {src}")

        dest_dir = getattr(self, dest)
        dest_path = dest_dir / f"{task_id}_{self._timestamp()}_{src_path.name}"

        # Move primary artifact
        shutil.copy2(src_path, dest_path)

        # Create carbon copy
        carbon_path = self.carbon / dest_path.name
        shutil.copy2(dest_path, carbon_path)

        return dest_path

    def recycle(self, src: str, task_id: str, reason: str) -> Path:
        """
        Archives an artifact with recycle reason embedded in filename.
        """
        src_path = Path(src)
        if not src_path.exists():
            raise FileNotFoundError(f"Source not found: {src}")

        recycled_name = f"{task_id}_RECYCLE_{self._timestamp()}_{src_path.name}"
        dest_path = self.archive / recycled_name

        shutil.copy2(src_path, dest_path)
        shutil.copy2(dest_path, self.carbon / recycled_name)

        return dest_path
