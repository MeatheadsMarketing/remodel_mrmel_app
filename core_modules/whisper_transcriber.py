# PHASE_1_FILE: Transcribes extracted audio using Whisper
# Origin: Blueprint Phase 1 — VIDEO + VOICE INTAKE
# Role: Runs OpenAI Whisper locally on .wav file and saves transcript as JSON

import os
import whisper
import json

def transcribe(audio_path):
    output_dir = "layout_test/transcript"
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.splitext(os.path.basename(audio_path))[0]
    output_path = os.path.join(output_dir, f"{filename}_transcript.json")

    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        return output_path
    except Exception as e:
        print(f"[ERROR] Transcription failed: {e}")
        return None
