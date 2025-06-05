# PHASE_2_FILE: Builds structured spatial layout commands from transcript and zone tag data
# Origin: Blueprint Phase 2 — GPT VOICE INTELLIGENCE
# Role: Consolidates transcript and zone_tags into formalized commands.json used by later rendering

import os
import json

def build_commands(transcript_path, zone_tags_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript = json.load(f)

    with open(zone_tags_path, "r", encoding="utf-8") as f:
        zones = json.load(f)

    commands = []

    for zone in zones:
        commands.append({
            "zone": zone.get("zone", "unknown"),
            "start": zone.get("start", 0),
            "end": zone.get("end", 0),
            "description": f"Inferred zone '{zone.get('zone', '')}' from timestamp {zone.get('start')}s to {zone.get('end')}s"
        })

    output_dir = "layout_test/parsed_commands"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "commands.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(commands, f, indent=2)

    return output_path
