# PHASE_3_FILE: Maps each captured frame to the closest matching command/zone
# Origin: Blueprint Phase 3 — FRAME SNAPSHOT GENERATION
# Role: Aligns each frame's timestamp with inferred zone based on commands.json

import os
import json

def map_frames_to_zones(commands_path, snapshot_dir, frame_interval=3):
    with open(commands_path, "r", encoding="utf-8") as f:
        commands = json.load(f)

    frame_mappings = []
    snapshot_files = sorted([f for f in os.listdir(snapshot_dir) if f.endswith(".jpg")])

    for i, frame_name in enumerate(snapshot_files):
        frame_time = i * frame_interval
        assigned_zone = "unknown"

        for command in commands:
            if command["start"] <= frame_time <= command["end"]:
                assigned_zone = command["zone"]
                break

        frame_mappings.append({
            "frame": frame_name,
            "timestamp": frame_time,
            "zone": assigned_zone
        })

    output_path = os.path.join(snapshot_dir, "frame_zone_map.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(frame_mappings, f, indent=2)

    return output_path
