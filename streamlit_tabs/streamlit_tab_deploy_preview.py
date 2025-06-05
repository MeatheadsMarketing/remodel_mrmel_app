# PHASE_FINAL_FILE: Streamlit tab for deployment preview and validation
# Origin: Deployment Sanity Check
# Role: Visually confirms all phase files, folders, and outputs are ready before launch

import streamlit as st
import os

st.title("🧪 Final Deployment Preview — Remodel_MrMel")

folders_to_check = [
    "layout_test/transcript",
    "layout_test/parsed_commands",
    "layout_test/snapshots",
    "layout_test/blueprint",
    "layout_test/layout_3d",
    "layout_test/feedback",
    "layout_test/vr_export"
]

files_to_flag = [
    "layout_test/transcript/transcript.json",
    "layout_test/parsed_commands/commands.json",
    "layout_test/parsed_commands/spatial_map.json",
    "layout_test/snapshots/frame_0000.jpg",
    "layout_test/snapshots/frame_zone_map.json",
    "layout_test/blueprint/2d_blueprint.svg",
    "layout_test/layout_3d/layout_model.glb",
    "layout_test/layout_3d/layout_metadata.json",
    "layout_test/feedback/blueprint_confirm_log.jsonl",
    "layout_test/feedback/vr_ready_flag.json",
    "layout_test/vr_export/vr_render_bundle.zip"
]

st.subheader("📁 Folder Sanity Check")
for folder in folders_to_check:
    if os.path.exists(folder):
        st.success(f"✅ {folder}")
    else:
        st.error(f"❌ {folder} MISSING")

st.subheader("📄 File Trace Check")
for file in files_to_flag:
    if os.path.exists(file):
        st.success(f"🟢 {file}")
    else:
        st.warning(f"🟡 {file} not found (optional or pending)")

st.info("📦 You can now deploy with full confidence if all folders and key files are GREEN.")
