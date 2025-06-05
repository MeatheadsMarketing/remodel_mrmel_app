# FOLDER_SANITY_CLEANER — Intelligent GPT Zip + File Cleaner for Remodel_MrMel
# Sorts, deduplicates, and restructures all files in a messy directory

import os
import shutil
from pathlib import Path

def clean_folder(root_dir="."):
    os.makedirs("remodel_mrmel_cleaned/phase_zips", exist_ok=True)
    os.makedirs("remodel_mrmel_cleaned/streamlit_tabs", exist_ok=True)
    os.makedirs("remodel_mrmel_cleaned/core_modules", exist_ok=True)
    os.makedirs("remodel_mrmel_cleaned/docs", exist_ok=True)
    os.makedirs("remodel_mrmel_cleaned/archive_trash", exist_ok=True)

    seen = {}

    for file in os.listdir(root_dir):
        path = os.path.join(root_dir, file)
        if not os.path.isfile(path):
            continue

        ext = Path(file).suffix
        base = Path(file).stem

        # Classify by extension
        if file.endswith(".gptpkg.zip"):
            target = "remodel_mrmel_cleaned/phase_zips"
        elif file.startswith("streamlit_tab") and file.endswith(".py"):
            target = "remodel_mrmel_cleaned/streamlit_tabs"
        elif file.endswith(".py"):
            target = "remodel_mrmel_cleaned/core_modules"
        elif ext in [".md", ".txt"]:
            target = "remodel_mrmel_cleaned/docs"
        else:
            target = "remodel_mrmel_cleaned/archive_trash"

        # Deduplication by file name
        if file in seen:
            existing_size = os.path.getsize(seen[file])
            new_size = os.path.getsize(path)
            if new_size > existing_size:
                os.replace(path, os.path.join(target, file))
                os.remove(seen[file])
            else:
                os.remove(path)
        else:
            shutil.move(path, os.path.join(target, file))
            seen[file] = os.path.join(target, file)

if __name__ == "__main__":
    clean_folder()
    print("✅ Folder cleaned and organized into /remodel_mrmel_cleaned/")
