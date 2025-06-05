#!/bin/bash

echo "🔧 Initializing Git + pushing to GitHub..."

# Replace with your repo URL
REPO_URL="https://github.com/MeatheadsMarketing/remodel_mrmel_app.git"

# Step 1: Initialize
git init
git config --global init.defaultBranch main
git config --global push.autoSetupRemote true

# Step 2: Add + commit
git add .
git commit -m "🚀 Auto push from GPT package"

# Step 3: Remote + push
git remote add origin "$REPO_URL"
git push -u origin main

echo "✅ Push complete. Repo live at:"
echo "$REPO_URL"
