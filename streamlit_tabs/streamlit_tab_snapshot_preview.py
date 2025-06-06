import streamlit as st
import os

def main():
    st.subheader("📸 Step 3: Snapshot Preview")

    snapshot_dir = "layout_test/snapshots"
    snapshot_files = []

    if os.path.exists(snapshot_dir):
        snapshot_files = sorted([f for f in os.listdir(snapshot_dir) if f.endswith(".jpg")])
    else:
        st.warning("⚠️ Snapshot folder not found. Run the generator or create the folder manually.")

    if not snapshot_files:
        st.info("No snapshot images to display.")
    else:
        for snapshot in snapshot_files:
            st.image(os.path.join(snapshot_dir, snapshot), caption=snapshot, use_column_width=True)