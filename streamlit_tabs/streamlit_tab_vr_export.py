# PHASE_8_FILE: Streamlit tab to export VR-ready bundle
# Origin: Blueprint Phase 8 — VR EXPORT + IMMERSIVE FILE GENERATION
# Role: Packages GLB, metadata, and manifest for VR viewing or Sketchfab deployment

import streamlit as st
import os
import zipfile

st.set_page_config(page_title="📦 Export VR Bundle", layout="centered")
st.title("📦 Step 8: Export VR Bundle")

vr_ready_path = "layout_test/feedback/vr_ready_flag.json"
export_dir = "layout_test/vr_export"
glb_path = "layout_test/layout_3d/layout_model.glb"
meta_path = "layout_test/layout_3d/layout_metadata.json"

if os.path.exists(vr_ready_path):
    st.success("✅ Layout is VR-ready!")
else:
    st.warning("⚠️ Layout is not confirmed for VR export yet.")

os.makedirs(export_dir, exist_ok=True)
zip_path = os.path.join(export_dir, "vr_render_bundle.zip")

if st.button("📦 Generate VR Export ZIP"):
    with zipfile.ZipFile(zip_path, "w") as zipf:
        if os.path.exists(glb_path):
            zipf.write(glb_path, arcname="layout_model.glb")
        if os.path.exists(meta_path):
            zipf.write(meta_path, arcname="layout_metadata.json")
        if os.path.exists(vr_ready_path):
            zipf.write(vr_ready_path, arcname="vr_ready_flag.json")

    st.success("✅ VR bundle created.")
    st.download_button("⬇️ Download VR Bundle", zip_path, file_name="vr_render_bundle.zip")
