
import os
import subprocess
import json

def check_last_commit_hash():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    except subprocess.CalledProcessError:
        return None

def get_remote_url():
    try:
        return subprocess.check_output(['git', 'remote', 'get-url', 'origin'], text=True).strip()
    except subprocess.CalledProcessError:
        return None

def write_status_file():
    commit_hash = check_last_commit_hash()
    remote_url = get_remote_url()

    status = {
        "push_status": "confirmed" if commit_hash and remote_url else "error",
        "last_commit": commit_hash,
        "remote_url": remote_url,
    }

    with open(".capsule_push_status.json", "w") as f:
        json.dump(status, f, indent=2)

    print("✅ .capsule_push_status.json written.")

if __name__ == "__main__":
    write_status_file()
