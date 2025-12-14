import os
import json
from datetime import datetime
from typing import Dict

ARTIFACT_DIR = os.path.join("data", "artifacts")

def write_artifact(task_id: str, content: Dict) -> Dict:
    os.makedirs(ARTIFACT_DIR, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = f"{task_id}_{timestamp}.json"
    path = os.path.join(ARTIFACT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(content, f, indent=2, ensure_ascii=False)

    return {
        "artifact_path": path,
        "artifact_filename": filename
                  }
