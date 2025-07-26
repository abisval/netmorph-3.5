import os

folders = [
    "gui",
    "plugin_registry",
    "plugins",
    "plugins/preprocessors",
    "config_loader"
]

for folder in folders:
    init_path = os.path.join(folder, "__init__.py")
    if not os.path.exists(init_path):
        with open(init_path, "w") as f:
            if folder == "gui":
                f.write("from .cockpit_gui import CockpitGUI\n")
            else:
                f.write(f"# {folder.split('/')[-1].capitalize()} init\n")
        print(f"✅ Created: {init_path}")
    else:
        print(f"🔹 Already exists: {init_path}")
