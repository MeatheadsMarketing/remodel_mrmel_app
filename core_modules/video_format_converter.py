# PHASE_1_FILE: Converts input video to standardized .mp4 format for processing
# Origin: Blueprint Phase 1 — VIDEO + VOICE INTAKE
# Role: Converts uploaded videos to .mp4 format with standardized codec + resolution

import os
from moviepy.editor import VideoFileClip

def convert(input_path):
    output_dir = "layout_test/input_video"
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_dir, f"{filename}_converted.mp4")

    try:
        clip = VideoFileClip(input_path)
        clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24)
        return output_path
    except Exception as e:
        print(f"[ERROR] Video conversion failed: {e}")
        return input_path  # Fallback: return original if conversion fails
