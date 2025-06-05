# PHASE_4_FILE: Displays the static 2D blueprint generated from snapshots and zone logic
# Origin: Blueprint Phase 4 — STATIC 2D BLUEPRINT GENERATION
# Role: Streamlit UI tab to preview SVG layout and text annotations for zone visualization

import streamlit as st
import os
import json


st.title("🗺️ Step 4: Blueprint Viewer")
st.write("Preview the generated 2D layout based on voice transcript and snapshot alignment.")

svg_path = "layout_test/blueprint/2d_blueprint.svg"
labels_path = "layout_test/blueprint/blueprint_labels.json"

# Load SVG layout
if os.path.exists(svg_path):
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_content = f.read()
    st.components.v1.html(svg_content, height=600, scrolling=True)
else:
    st.warning("⚠️ Blueprint SVG not found.")

# Load label annotations
try:
    with open(labels_path, "r", encoding="utf-8") as f:
        labels = json.load(f)
    st.subheader("🏷️ Labels & Room Tags")
    st.json(labels)
except:
    st.info("No label metadata found.")
