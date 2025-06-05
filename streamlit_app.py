# STREAMLIT_APP.PY — Master entry point for Remodel_MrMel VR Builder
# Launches all 8 confirmed capsule phases via tab selector

import streamlit as st
import importlib

st.set_page_config(page_title="🏗️ Remodel MrMel — Full Assistant", layout="wide")

TAB_ROUTES = {
    "📼 1. Upload Video": "streamlit_tab_video_upload",
    "📝 2. Transcript Review": "streamlit_tab_transcript_inspector",
    "📸 3. Snapshot Preview": "streamlit_tab_snapshot_preview",
    "🗺️ 4. Blueprint Viewer": "streamlit_tab_blueprint_viewer",
    "✅ 5. Confirm 2D": "streamlit_tab_confirm_blueprint",
    "🔲 6. Preview 3D": "streamlit_tab_3d_preview",
    "🎮 7. Confirm 3D": "streamlit_tab_confirm_3d_render",
    "📦 8. VR Export": "streamlit_tab_vr_export",
}

st.sidebar.title("🏠 Remodel MrMel")
choice = st.sidebar.radio("Navigate Workflow:", list(TAB_ROUTES.keys()))

module_name = TAB_ROUTES[choice]
try:
    module = importlib.import_module(module_name)
    if hasattr(module, "main"):
        module.main()
    else:
        st.error(f"⚠️ `{module_name}` is missing a `main()` function.")
except ModuleNotFoundError:
    st.error(f"❌ Cannot find module: `{module_name}`. Ensure it’s in the path.")
