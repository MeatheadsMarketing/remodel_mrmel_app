
# ✅ PATCHED: Streamlit app with fully qualified tab imports

import streamlit as st

from streamlit_tabs import (
    streamlit_tab_video_upload,
    streamlit_tab_transcript_inspector,
    streamlit_tab_snapshot_preview,
    streamlit_tab_blueprint_viewer,
    streamlit_tab_confirm_blueprint,
    streamlit_tab_confirm_3d_render,
    streamlit_tab_3d_preview,
    streamlit_tab_vr_export
)

st.set_page_config(page_title="Remodel MrMel", layout="wide")

st.sidebar.title("🏠 Remodel MrMel")
tab_selection = st.sidebar.radio(
    "Navigate Workflow:",
    [
        "1. Upload Video",
        "2. Transcript Review",
        "3. Snapshot Preview",
        "4. Blueprint Viewer",
        "5. Confirm 2D",
        "6. Preview 3D",
        "7. Confirm 3D",
        "8. VR Export"
    ]
)

if tab_selection == "1. Upload Video":
    streamlit_tab_video_upload.render_video_upload_tab()

elif tab_selection == "2. Transcript Review":
    streamlit_tab_transcript_inspector.main()

elif tab_selection == "3. Snapshot Preview":
    streamlit_tab_snapshot_preview.main()

elif tab_selection == "4. Blueprint Viewer":
    streamlit_tab_blueprint_viewer.main()

elif tab_selection == "5. Confirm 2D":
    streamlit_tab_confirm_blueprint.main()

elif tab_selection == "6. Preview 3D":
    streamlit_tab_3d_preview.main()

elif tab_selection == "7. Confirm 3D":
    streamlit_tab_confirm_3d_render.main()

elif tab_selection == "8. VR Export":
    streamlit_tab_vr_export.main()
