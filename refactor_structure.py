import os
import shutil

BASE = os.getcwd()

# Target structure
RECOMMENDED = {
    "cockpit": [],
    "core/registry": ["SiteRegistry.py", "__init__.py"],
    "plugins": [],
    "reference": ["my_sites.csv"],
    "status": [],
    "utils": [],
}

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[+] Created: {path}")
    else:
        print(f"[✔] Exists: {path}")

def move_file(filename, target_dir):
    for root, dirs, files in os.walk(BASE):
        if filename in files:
            src = os.path.join(root, filename)
            dst = os.path.join(BASE, target_dir, filename)
            if src != dst:
                shutil.move(src, dst)
                print(f"[→] Moved: {filename} → {target_dir}")
            return
    print(f"[!] File not found: {filename}")

def setup_structure():
    for folder, files in RECOMMENDED.items():
        folder_path = os.path.join(BASE, folder)
        ensure_dir(folder_path)

        # Init if needed
        if "__init__.py" in files:
            init_path = os.path.join(folder_path, "__init__.py")
            if not os.path.exists(init_path):
                open(init_path, "w").close()
                print(f"[+] Created empty __init__.py in {folder}")

        # Move files
        for fname in files:
            if fname != "__init__.py":
                move_file(fname, folder)

def cleanup_obsolete_dirs():
    expected_dirs = {os.path.join(BASE, d.split("/")[0]) for d in RECOMMENDED.keys()}
    current_dirs = {os.path.join(BASE, d) for d in os.listdir(BASE) if os.path.isdir(d)}
    extra = current_dirs - expected_dirs
    for d in extra:
        print(f"[?] Extra folder detected: {d}")
        # Optional: Prompt before deleting or moving contents

if __name__ == "__main__":
    print("🔧 Harmonizing NetMorph file structure...")
    setup_structure()
    cleanup_obsolete_dirs()
    print("✅ Refactor complete.")