# PHASE_2_FILE: Streamlit tab to display and review Whisper transcript with GPT-enriched zone tags
# Origin: Blueprint Phase 2 — GPT VOICE INTELLIGENCE
# Role: Visual interface to review raw + tagged transcript JSON and zone classification

import streamlit as st
import json
import os

st.set_page_config(page_title="🧠 Transcript Inspector", layout="wide")

st.title("📝 Step 2: Review Transcription + Zone Tags")
st.markdown("Use this tab to view the raw transcription and inspect the GPT-detected layout zones.")

transcript_path = "layout_test/transcript"
commands_path = "layout_test/parsed_commands"

# Load transcript
try:
    transcript_file = [f for f in os.listdir(transcript_path) if f.endswith("_transcript.json")][0]
    with open(os.path.join(transcript_path, transcript_file), "r", encoding="utf-8") as f:
        transcript = json.load(f)
    st.success(f"Loaded: {transcript_file}")
    st.subheader("📄 Raw Transcript")
    st.json(transcript)
except:
    st.warning("❌ No transcript found. Please complete Phase 1 first.")

# Load commands
try:
    commands_file = "commands.json"
    with open(os.path.join(commands_path, commands_file), "r", encoding="utf-8") as f:
        commands = json.load(f)
    st.subheader("🧠 GPT-Generated Zone Tags + Commands")
    st.json(commands)
except:
    st.info("⏳ No zone tagging file found yet. Run GPT zone tagger module to see results.")
