# PHASE_6_FILE: Streamlit tab to preview 3D layout render
# Origin: Blueprint Phase 6 — 3D BASIC RENDER FROM 2D BLUEPRINT
# Role: Displays GLB model of layout for inspection before VR generation

import streamlit as st
import os

st.set_page_config(page_title="🔲 3D Layout Preview", layout="wide")
st.title("🔲 Step 6: Preview 3D Layout")
st.write("Review the basic 3D layout generated from your 2D blueprint.")

glb_path = "layout_test/layout_3d/layout_model.glb"
meta_path = "layout_test/layout_3d/layout_metadata.json"

# Show GLB preview if available
if os.path.exists(glb_path):
    st.download_button("⬇️ Download 3D Model", glb_path, file_name="layout_model.glb")
    st.markdown("To preview interactively, open with a GLB viewer like Sketchfab or Babylonsandbox.")
else:
    st.warning("⚠️ No 3D model found. Please run the render generator.")

# Show metadata if present
try:
    with open(meta_path, "r", encoding="utf-8") as f:
        import json
        metadata = json.load(f)
    st.subheader("📄 Layout Metadata")
    st.json(metadata)
except:
    st.info("ℹ️ No metadata file found.")
