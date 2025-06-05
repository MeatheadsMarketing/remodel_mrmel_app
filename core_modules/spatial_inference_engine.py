# PHASE_2_FILE: Infers spatial logic from command + transcript data
# Origin: Blueprint Phase 2 — GPT VOICE INTELLIGENCE
# Role: Establishes spatial relationships (adjacency, entry points, sequence) from transcript zones

import os
import json

def infer_spatial_map(commands_path):
    with open(commands_path, "r", encoding="utf-8") as f:
        commands = json.load(f)

    spatial_map = {
        "sequence": [],
        "adjacency_matrix": {},
        "entry_point": None
    }

    last_zone = None
    for cmd in commands:
        zone = cmd["zone"]
        spatial_map["sequence"].append(zone)

        if last_zone:
            spatial_map["adjacency_matrix"].setdefault(last_zone, set()).add(zone)
            spatial_map["adjacency_matrix"].setdefault(zone, set()).add(last_zone)

        last_zone = zone

    if spatial_map["sequence"]:
        spatial_map["entry_point"] = spatial_map["sequence"][0]

    # convert sets to lists
    for k in spatial_map["adjacency_matrix"]:
        spatial_map["adjacency_matrix"][k] = list(spatial_map["adjacency_matrix"][k])

    output_dir = "layout_test/parsed_commands"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "spatial_map.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(spatial_map, f, indent=2)

    return output_path
