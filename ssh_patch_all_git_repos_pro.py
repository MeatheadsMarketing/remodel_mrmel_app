
import os
import subprocess
import json

def find_git_repos(root_dir):
    git_repos = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            git_repos.append(dirpath)
            dirnames[:] = []  # Do not recurse deeper
    return git_repos

def convert_to_ssh(remote_url):
    if remote_url.startswith("https://github.com/"):
        path = remote_url.replace("https://github.com/", "")
        return f"git@github.com:{path}"
    return None

def inject_auto_push_script(repo_path):
    script_path = os.path.join(repo_path, 'git_auto_push.sh')
    if not os.path.exists(script_path):
        with open(script_path, 'w') as f:
            f.write('#!/bin/bash\ngit add .\ngit commit -m "Auto-push update"\ngit push origin main\n')
        os.chmod(script_path, 0o755)
        return True
    return False

def run_remote_test(repo_path):
    try:
        subprocess.check_output(['git', 'ls-remote', '--exit-code'], cwd=repo_path)
        return "accessible"
    except subprocess.CalledProcessError:
        return "not_accessible"

def patch_repo(repo_path):
    os.chdir(repo_path)
    log_entry = {
        "repo": repo_path,
        "status": "",
        "original_url": "",
        "new_url": "",
        "push_access": "",
        "auto_push_injected": False
    }

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
        else:
            log_entry["status"] = "already_ssh"
            log_entry["new_url"] = original_url

        # Run push access test
        log_entry["push_access"] = run_remote_test(repo_path)

        # Inject git_auto_push.sh
        log_entry["auto_push_injected"] = inject_auto_push_script(repo_path)

        # Add .capsule_git_status file
        with open(os.path.join(repo_path, ".capsule_git_status"), "w") as status_file:
            status_file.write(json.dumps(log_entry, indent=2))

    except Exception as e:
        log_entry["status"] = "error"
        log_entry["error"] = str(e)

    return log_entry

if __name__ == "__main__":
    HOME = os.path.expanduser("~")
    base_path = HOME  # Scan entire user directory

    print(f"🔍 Scanning: {base_path}")
    repos = find_git_repos(base_path)

    all_logs = []

    for repo in repos:
        log_entry = patch_repo(repo)
        print(f"📦 {repo} → {log_entry['status']}")
        all_logs.append(log_entry)

    with open("patch_log_pro.jsonl", "w") as f:
        for entry in all_logs:
            f.write(json.dumps(entry) + "\n")
