# PHASE_5_FILE: Feedback capture utility for blueprint confirmation system
# Origin: Blueprint Phase 5 — USER CONFIRMATION GATE 1
# Role: Modular handler to log user approval/rejection and archive traceable feedback

import os
import json
from datetime import datetime

def record_feedback(confirm_value, comments, log_path, notes_path):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "confirmed": confirm_value,
        "comments": comments
    }

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

    if comments.strip():
        with open(notes_path, "a", encoding="utf-8") as note_file:
            note_file.write(f"{datetime.now().isoformat()} — {comments}\n")

    return True
