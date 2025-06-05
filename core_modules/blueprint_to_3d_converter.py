# PHASE_6_FILE: Converts layout outline JSON into 3D geometry
# Origin: Blueprint Phase 6 — 3D BASIC RENDER FROM 2D BLUEPRINT
# Role: Generates .glb or .gltf file with layout volume and room mapping

import os
import trimesh
import json

def convert_to_3d(layout_outline_path, output_glb_path):
    with open(layout_outline_path, "r", encoding="utf-8") as f:
        layout = json.load(f)

    scene = trimesh.Scene()

    for i, zone in enumerate(layout.get("zones", [])):
        center = zone.get("center", [0, 0])
        width = zone.get("width", 4)
        height = zone.get("height", 4)

        mesh = trimesh.creation.box(extents=(width, 2, height))
        mesh.apply_translation((center[0], 1, center[1]))
        scene.add_geometry(mesh)

    os.makedirs(os.path.dirname(output_glb_path), exist_ok=True)
    scene.export(output_glb_path)
    return output_glb_path
