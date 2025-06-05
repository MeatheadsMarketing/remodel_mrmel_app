# PHASE_5_FILE: Streamlit tab for blueprint confirmation + feedback
# Origin: Blueprint Phase 5 — USER CONFIRMATION GATE 1
# Role: Allows user to confirm 2D blueprint validity and leave feedback

import streamlit as st
import os
import json
from datetime import datetime

st.set_page_config(page_title="✅ Confirm 2D Blueprint", layout="centered")
st.title("✅ Step 5: Confirm Your Blueprint")
st.write("Review the layout below and confirm if it matches what you described in your walkthrough.")

svg_path = "layout_test/blueprint/2d_blueprint.svg"
feedback_path = "layout_test/feedback/blueprint_confirm_log.jsonl"
notes_path = "layout_test/feedback/feedback_notes.txt"

if os.path.exists(svg_path):
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_content = f.read()
    st.components.v1.html(svg_content, height=600, scrolling=True)
else:
    st.warning("⚠️ No blueprint SVG found. Please generate it first.")

st.markdown("## 🧠 Confirmation")
confirm = st.radio("Is this layout correct?", ["Yes", "No"])

comments = st.text_area("Optional: Add feedback, corrections, or suggestions")

if st.button("Submit Confirmation"):
    os.makedirs("layout_test/feedback", exist_ok=True)
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "confirmed": confirm,
        "comments": comments
    }
    with open(feedback_path, "a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

    if comments.strip():
        with open(notes_path, "a", encoding="utf-8") as note_file:
            note_file.write(f"{datetime.now().isoformat()} — {comments}\n")

    st.success("✅ Confirmation recorded.")
