# PHASE_7_FILE: Streamlit tab to confirm 3D render validity before VR export
# Origin: Blueprint Phase 7 — VR CONFIRMATION GATE
# Role: UI for user approval of 3D layout and logs readiness for VR generation

import streamlit as st
import os
import json
from datetime import datetime

st.title("🎮 Step 7: Confirm 3D Layout")
st.write("This is your last step before generating your full VR export.")

glb_path = "layout_test/layout_3d/layout_model.glb"
meta_path = "layout_test/layout_3d/layout_metadata.json"
confirm_path = "layout_test/feedback/render_confirm_log.jsonl"
flag_path = "layout_test/feedback/vr_ready_flag.json"

if os.path.exists(glb_path):
    st.download_button("⬇️ Download Final 3D Layout", glb_path, file_name="layout_model.glb")
else:
    st.warning("⚠️ layout_model.glb not found.")

st.subheader("💬 VR Readiness Confirmation")
confirm = st.radio("Is this layout ready for VR export?", ["Yes", "No"])
comments = st.text_area("Optional: Feedback or change requests")

if st.button("✅ Finalize Layout"):
    os.makedirs("layout_test/feedback", exist_ok=True)
    with open(confirm_path, "a", encoding="utf-8") as log_file:
        log_file.write(json.dumps({
            "timestamp": datetime.now().isoformat(),
            "confirmed": confirm,
            "comments": comments
        }) + "\n")

    if confirm == "Yes":
        with open(flag_path, "w", encoding="utf-8") as flag_file:
            json.dump({"vr_ready": True, "timestamp": datetime.now().isoformat()}, flag_file)

    st.success("✅ Response recorded. Layout status updated.")
