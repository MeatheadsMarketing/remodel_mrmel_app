
import os
import subprocess
import json

def find_git_repos(root_dir):
    git_repos = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            git_repos.append(dirpath)
            dirnames[:] = []  # Don't recurse deeper
    return git_repos

def convert_to_ssh(remote_url):
    if remote_url.startswith("https://github.com/"):
        path = remote_url.replace("https://github.com/", "")
        return f"git@github.com:{path}"
    return None

def patch_repo(repo_path):
    os.chdir(repo_path)
    log_entry = {"repo": repo_path, "status": "", "original_url": "", "new_url": ""}
    try:
        original_url = subprocess.check_output(
            ['git', 'remote', 'get-url', 'origin'], text=True
        ).strip()
        log_entry["original_url"] = original_url

        ssh_url = convert_to_ssh(original_url)
        if ssh_url:
            subprocess.run(['git', 'remote', 'set-url', 'origin', ssh_url])
            log_entry["new_url"] = ssh_url
            log_entry["status"] = "patched"
            print(f"✅ Patched: {repo_path} → {ssh_url}")
        else:
            log_entry["status"] = "already_ssh"
            print(f"🔒 Already SSH: {repo_path}")
    except Exception as e:
        log_entry["status"] = "error"
        log_entry["error"] = str(e)
        print(f"❌ Error patching {repo_path}: {e}")
    return log_entry

if __name__ == "__main__":
    HOME = os.path.expanduser("~")
    scan_paths = [
        os.path.join(HOME, "Desktop"),
        os.path.join(HOME, "Documents"),
        os.path.join(HOME, "Projects"),
    ]

    all_logs = []

    for base in scan_paths:
        print(f"\n🔍 Scanning: {base}")
        repos = find_git_repos(base)
        for repo in repos:
            log_entry = patch_repo(repo)
            all_logs.append(log_entry)

    with open("patch_log.jsonl", "w") as f:
        for entry in all_logs:
            f.write(json.dumps(entry) + "\n")
