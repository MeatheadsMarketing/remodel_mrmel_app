# PHASE_8_FILE: Programmatic bundler for GLB, metadata, and VR flag
# Origin: Blueprint Phase 8 — VR EXPORT + IMMERSIVE FILE GENERATION
# Role: Creates zip bundle for export-ready 3D layout with all metadata

import os
import zipfile

def package_vr_bundle(glb_path, metadata_path, flag_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with zipfile.ZipFile(output_path, "w") as zipf:
        if os.path.exists(glb_path):
            zipf.write(glb_path, arcname="layout_model.glb")
        if os.path.exists(metadata_path):
            zipf.write(metadata_path, arcname="layout_metadata.json")
        if os.path.exists(flag_path):
            zipf.write(flag_path, arcname="vr_ready_flag.json")

    return output_path
