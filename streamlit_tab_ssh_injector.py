
import streamlit as st
import subprocess
import os

st.set_page_config(page_title="SSH Key Injector", layout="centered")

st.title("🔐 GitHub SSH Key Injector & Verifier")

key_path = os.path.expanduser("~/.ssh/id_ed25519")

if not os.path.exists(key_path):
    st.error("❌ SSH key not found at ~/.ssh/id_ed25519. Generate one first using ssh-keygen.")
else:
    st.success("✅ SSH key detected at ~/.ssh/id_ed25519")

    if st.button("➡️ Add SSH Key to Agent"):
        try:
            subprocess.run(["ssh-agent", "-s"], shell=True, check=True)
            subprocess.run(["ssh-add", key_path], check=True)
            st.success("🔑 SSH key added to agent successfully.")
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to add key: {e}")

    if st.button("✅ Test GitHub SSH Connection"):
        try:
            result = subprocess.run(["ssh", "-T", "git@github.com"], capture_output=True, text=True)
            if "successfully authenticated" in result.stdout:
                st.success("🎉 GitHub SSH authentication successful!")
                st.code(result.stdout)
            else:
                st.warning("⚠️ GitHub SSH authentication failed.")
                st.code(result.stderr + result.stdout)
        except subprocess.CalledProcessError as e:
            st.error(f"SSH Test Error: {e}")
