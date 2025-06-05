# PHASE_4_FILE: Adds room labels and object annotations to 2D blueprint
# Origin: Blueprint Phase 4 — STATIC 2D BLUEPRINT GENERATION
# Role: Annotates layout zones with detected furniture, labels, and instructions

import os
import json

def label_zones(commands_path, output_path):
    with open(commands_path, "r", encoding="utf-8") as f:
        commands = json.load(f)

    labels = []
    for cmd in commands:
        zone = cmd.get("zone", "unknown")
        start = cmd.get("start", 0)
        end = cmd.get("end", 0)
        description = cmd.get("description", "")

        labels.append({
            "zone": zone,
            "time_window": f"{start}s - {end}s",
            "label": description
        })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(labels, f, indent=2)

    return output_path
