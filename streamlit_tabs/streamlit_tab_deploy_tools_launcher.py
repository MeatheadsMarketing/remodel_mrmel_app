# STREAMLIT TAB: Deploy Tools Launcher
# Allows launching Git automation, .env validator, and cloud prep directly inside Streamlit

import streamlit as st
import os
from streamlit_env_validator import validate_env

st.title("🚀 Deploy Tools Launcher")

st.markdown("This dashboard provides access to your Git push tools, Streamlit Cloud setup guide, and environment validator.")

st.subheader("🔐 Environment Validation")
validate_env()

st.subheader("📄 Key Deployment Files")
deploy_files = [
    "git_auto_push.sh",
    "git_secure_boilerplate.sh",
    "README_BADGES.md",
    "STREAMLIT_CLOUD_DEPLOY.md",
    "streamlit_env_validator.py"
]

for file in deploy_files:
    if os.path.exists(file):
        st.download_button(f"📥 {file}", open(file, "rb").read(), file_name=file)

st.subheader("💬 Instructions")
st.markdown("""
Run `.sh` scripts from your terminal:
```bash
chmod +x git_auto_push.sh
./git_auto_push.sh
```

Deploy to Streamlit Cloud:
- Push code to GitHub
- Use `streamlit_app.py` as entry
- Set `OPENAI_API_KEY` in app secrets
""")
