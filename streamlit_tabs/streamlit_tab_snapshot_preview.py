# PHASE_3_FILE: Displays captured snapshot frames and associated zone/command metadata
# Origin: Blueprint Phase 3 — FRAME SNAPSHOT GENERATION
# Role: Streamlit UI tab for reviewing captured frames alongside inferred zone logic

import streamlit as st
import os
import json
from PIL import Image

st.set_page_config(page_title="📸 Snapshot Preview", layout="wide")

st.title("📸 Step 3: Snapshot Preview")
st.write("Browse the frames captured from your walkthrough video and check how they align with zones or rooms.")

snapshot_dir = "layout_test/snapshots"
command_path = "layout_test/parsed_commands/commands.json"

# Load snapshots
snapshot_files = sorted([f for f in os.listdir(snapshot_dir) if f.endswith(".jpg")])

if snapshot_files:
    selected_frame = st.selectbox("Select a snapshot to view:", snapshot_files)
    image_path = os.path.join(snapshot_dir, selected_frame)
    image = Image.open(image_path)
    st.image(image, caption=f"Snapshot: {selected_frame}", use_column_width=True)
else:
    st.warning("⚠️ No snapshots found. Make sure to run the snapshot generator first.")

# Load zone commands
try:
    with open(command_path, "r", encoding="utf-8") as f:
        commands = json.load(f)
    st.subheader("🧠 Inferred Commands / Zone Info")
    st.json(commands)
except:
    st.info("No commands found yet.")
