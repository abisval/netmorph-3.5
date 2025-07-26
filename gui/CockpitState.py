import json
import os

class CockpitState:
    def __init__(self, config_file="cockpit_config.json"):
        self.config_file = config_file
        self.state = {"last_dir": ""}
        self._load()

    def _load(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                self.state.update(json.load(f))

    def save_last_dir(self, path):
        self.state["last_dir"] = path
        with open(self.config_file, "w") as f:
            json.dump(self.state, f)

    def get_last_dir(self):
        return self.state.get("last_dir", "")
