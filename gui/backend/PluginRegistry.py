import os
import json

class PluginRegistry:
    def __init__(self, base_folder):
        self.base_folder = base_folder
        self.plugin_folder = os.path.join(base_folder, "plugins")
        self.status_path = os.path.join(base_folder, "status.json")
        self.plugins = []
        self.status_data = {}

        self.load_plugins()
        self.load_status()

    def load_plugins(self):
        self.plugins = []
        if not os.path.exists(self.plugin_folder):
            return
        for file in os.listdir(self.plugin_folder):
            if file.endswith(".py") and not file.startswith("__"):
                self.plugins.append(file)

    def load_status(self):
        try:
            with open(self.status_path, "r") as f:
                self.status_data = json.load(f)
        except Exception:
            self.status_data = {}

    def get_health(self, plugin_name):
        return self.status_data.get(plugin_name, {}).get("health", "unknown")

    def get_all_plugins(self):
        return [
            {
                "name": p,
                "health": self.get_health(p),
                "enabled": self.status_data.get(p, {}).get("enabled", False)
            }
            for p in self.plugins
        ]