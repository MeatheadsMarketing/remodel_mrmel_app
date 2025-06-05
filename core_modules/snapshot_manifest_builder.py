# PHASE_3_FILE: Builds manifest to summarize all captured snapshots and zone mappings
# Origin: Blueprint Phase 3 — FRAME SNAPSHOT GENERATION
# Role: Creates manifest index for downstream blueprint or model alignment

import os
import json

def build_manifest(snapshot_dir):
    snapshots = sorted([f for f in os.listdir(snapshot_dir) if f.endswith(".jpg")])
    zone_map_path = os.path.join(snapshot_dir, "frame_zone_map.json")

    manifest = {
        "snapshot_count": len(snapshots),
        "frames": [],
        "zone_index": {}
    }

    if os.path.exists(zone_map_path):
        with open(zone_map_path, "r", encoding="utf-8") as f:
            zone_map = json.load(f)
        manifest["frames"] = zone_map

        for entry in zone_map:
            zone = entry["zone"]
            manifest["zone_index"].setdefault(zone, []).append(entry["frame"])
    else:
        for i, f in enumerate(snapshots):
            manifest["frames"].append({"frame": f, "timestamp": i * 3, "zone": "unknown"})

    output_path = os.path.join(snapshot_dir, "snapshot_manifest.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return output_path
