"""
Entry point for NetMorph 3.5
Initializes plugins, loads configs, and launches the GUI cockpit.
"""

import tkinter as tk

from plugin_registry.registry import load_all_plugins
from config_loader.config_registry import load_all_configs

def try_import_gui():
    try:
        from gui.cockpit_gui import NetMorphCockpit
        print("✅ cockpit_gui module imported successfully")
        return NetMorphCockpit
    except Exception as e:
        print(f"❌ Failed to import GUI module: {e}")
        return None

def main():
    print("🧠 NetMorph Boot Sequence Initiated")

    # Load plugin registry
    try:
        print("🔌 Loading plugin modules...")
        plugin_registry = load_all_plugins()
        print(f"✅ Loaded plugins: {sum(len(v) for v in plugin_registry.values())}")
    except Exception as e:
        print(f"❌ Plugin loading failed: {e}")
        return

    # Load configuration registry
    try:
        print("⚙️ Loading configuration files...")
        config_registry = load_all_configs()
        print(f"✅ Loaded configs: {len(config_registry)}")
    except Exception as e:
        print(f"❌ Config loading failed: {e}")
        return

    # Import GUI module
    NetMorphCockpit = try_import_gui()
    if NetMorphCockpit is None:
        print("🛑 Aborting launch due to GUI import failure")
        return

    # Launch cockpit GUI
    print("🛫 Launching NetMorph cockpit GUI...")
    try:
        root = tk.Tk()
        root.title("NetMorph 3.5 Cockpit")
        root.geometry("1024x768")
        root.lift()
        root.state("normal")
        root.focus_force()

        app = NetMorphCockpit(root, plugin_registry, config_registry)
        print("🎯 NetMorphCockpit object created successfully")
        root.mainloop()
        print("🧩 GUI event loop exited")
    except Exception as e:
        print(f"❌ GUI failed to launch or crashed during runtime:\n{e}")

if __name__ == "__main__":
    main()