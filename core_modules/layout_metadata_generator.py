# PHASE_6_FILE: Generates layout_metadata.json to describe rooms and zones in 3D model
# Origin: Blueprint Phase 6 — 3D BASIC RENDER FROM 2D BLUEPRINT
# Role: Captures zone names, bounding boxes, and labels for viewer tools and VR engines

import json
import os

def generate_layout_metadata(commands_path, output_path):
    with open(commands_path, "r", encoding="utf-8") as f:
        commands = json.load(f)

    metadata = []
    for cmd in commands:
        metadata.append({
            "zone": cmd.get("zone", "unknown"),
            "label": cmd.get("description", ""),
            "start": cmd.get("start"),
            "end": cmd.get("end")
        })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    return output_path
