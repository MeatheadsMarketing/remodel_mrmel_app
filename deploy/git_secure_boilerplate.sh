#!/bin/bash

echo "🔐 Setting up secure Git boilerplate for Streamlit/GPT deployment..."

# Step 1: Create .gitignore if not exists
echo -e ".env\n__pycache__/\n*.zip\n*.gptpkg.zip\nlayout_test/\n.vscode/" > .gitignore
echo "✅ .gitignore created."

# Step 2: Add .env example
echo -e "OPENAI_API_KEY=your-openai-key-here" > .env
echo "✅ .env file stub created. Be sure to update your real key securely."

# Step 3: Git init + add
git init
git config --global init.defaultBranch main
git config --global push.autoSetupRemote true
git add .
git commit -m "🔐 Add secure boilerplate (.env + .gitignore)"

# Step 4: Remote setup
REPO_URL="https://github.com/MeatheadsMarketing/remodel_mrmel_app.git"
git remote add origin "$REPO_URL"
git push -u origin main

echo "✅ Secure GitHub repo pushed."
