# PHASE_1_FILE: Extracts .wav audio track from input video
# Origin: Blueprint Phase 1 — VIDEO + VOICE INTAKE
# Role: Extracts clean audio from converted .mp4 video for Whisper transcription

import os
from moviepy.editor import VideoFileClip

def extract(video_path):
    output_dir = "layout_test/extracted_audio"
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(output_dir, f"{filename}.wav")

    try:
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(output_path, fps=16000)
        return output_path
    except Exception as e:
        print(f"[ERROR] Audio extraction failed: {e}")
        return None
