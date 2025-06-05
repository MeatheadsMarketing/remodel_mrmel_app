# PHASE_4_FILE: Builds inferred room layout and determines room sequence for blueprint rendering
# Origin: Blueprint Phase 4 — STATIC 2D BLUEPRINT GENERATION
# Role: Refines entry-to-exit sequence and guides layout engine with directional hints

import json

def build_path_sequence(commands_path):
    with open(commands_path, "r", encoding="utf-8") as f:
        commands = json.load(f)

    sequence = []
    zone_seen = set()

    for cmd in commands:
        zone = cmd.get("zone", "unknown")
        if zone not in zone_seen:
            sequence.append(zone)
            zone_seen.add(zone)

    return {
        "entry_point": sequence[0] if sequence else "unknown",
        "zone_sequence": sequence
    }
