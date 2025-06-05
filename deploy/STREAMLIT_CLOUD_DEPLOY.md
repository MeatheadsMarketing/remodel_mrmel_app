# Streamlit Cloud Deployment Guide

This file explains how to deploy your `remodel_mrmel_app/` project directly to [Streamlit Cloud](https://share.streamlit.io).

---

## 📦 1. Upload to GitHub

1. Create a new repository (e.g., `remodel-mrmel`)
2. Upload these files:
   - `streamlit_app.py`
   - `requirements.txt`
   - `README.md`
   - All files in `streamlit_tabs/` and `core_modules/`

```
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/remodel-mrmel.git
git push -u origin main
```

---

## 🚀 2. Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "New App" and connect your GitHub repo
3. Set **Main file path** to:
```
streamlit_app.py
```

4. Set environment variable:
```
OPENAI_API_KEY = your-openai-key
```

5. Click “Deploy”

---

## ✅ You’re Live

Your dad can now use a private VR workflow powered by GPT, end-to-end.

All file outputs are mutation-ready, and streamlit logs will help you trace evolution.
