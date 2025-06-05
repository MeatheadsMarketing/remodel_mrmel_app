# PHASE_7_FILE: Logs confirmation of 3D layout and toggles VR-ready flag
# Origin: Blueprint Phase 7 — VR CONFIRMATION GATE
# Role: Backend logic for logging user 3D layout approvals and updating vr_ready_flag.json

import os
import json
from datetime import datetime

def flag_render_approval(confirm_value, comments, confirm_log_path, flag_file_path):
    os.makedirs(os.path.dirname(confirm_log_path), exist_ok=True)

    with open(confirm_log_path, "a", encoding="utf-8") as log_file:
        log_file.write(json.dumps({
            "timestamp": datetime.now().isoformat(),
            "confirmed": confirm_value,
            "comments": comments
        }) + "\n")

    if confirm_value == "Yes":
        with open(flag_file_path, "w", encoding="utf-8") as flag_file:
            json.dump({
                "vr_ready": True,
                "timestamp": datetime.now().isoformat()
            }, flag_file)

    return True
