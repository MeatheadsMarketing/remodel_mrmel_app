import streamlit as st
import os

def render_video_upload_tab():
    st.title("🎥 Upload Walkthrough Video")

    st.markdown(
        "Upload a video of the property walkthrough. This will trigger downstream processing: "
        "*transcription*, *snapshot generation*, and *3D blueprint extraction*."
    )

    uploaded_video = st.file_uploader("📤 Upload MP4/MOV File", type=["mp4", "mov"])

    if uploaded_video:
        upload_dir = "inputs"
        os.makedirs(upload_dir, exist_ok=True)
        video_path = os.path.join(upload_dir, uploaded_video.name)

        with open(video_path, "wb") as f:
            f.write(uploaded_video.getbuffer())

        st.success(f"✅ Video uploaded and saved to `{video_path}`")

        # Placeholder for triggering next pipeline step
        st.info("🧠 Ready for transcription and snapshot trigger...")
        st.button("🔁 Begin Transcript & Snapshot Pipeline")