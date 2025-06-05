# PHASE_3_FILE: Captures snapshot frames from walkthrough video at specified intervals or timestamps
# Origin: Blueprint Phase 3 — FRAME SNAPSHOT GENERATION
# Role: Extracts key video frames as .jpg images for zone alignment

import os
from moviepy.editor import VideoFileClip

def generate_snapshots(video_path, interval_seconds=3):
    output_dir = "layout_test/snapshots"
    os.makedirs(output_dir, exist_ok=True)

    try:
        clip = VideoFileClip(video_path)
        duration = int(clip.duration)

        frame_count = 0
        for t in range(0, duration, interval_seconds):
            frame = clip.get_frame(t)
            frame_filename = f"frame_{frame_count:04d}.jpg"
            frame_path = os.path.join(output_dir, frame_filename)

            clip.save_frame(frame_path, t)
            frame_count += 1

        return output_dir
    except Exception as e:
        print(f"[ERROR] Snapshot generation failed: {e}")
        return None
