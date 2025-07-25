# gui/cockpit_gui.py

import tkinter as tk
from tkinter import ttk

from gui.DataPrepGUI import DataPrepGUI
from gui.SemanticValidatorGUI import SemanticValidatorGUI
from gui.TrafficForecastGUI import TrafficForecastGUI
from gui.CoverageIntelligenceGUI import CoverageIntelligenceGUI
from gui.PluginManagerGUI import PluginManagerGUI
if __name__ == "__main__":
    import tkinter as tk
    from plugin_registry.registry import load_all_plugins
    from config_loader.config_registry import load_all_configs

    root = tk.Tk()
    root.title("NetMorph 3.5 Cockpit [Standalone Test]")
    root.geometry("1024x768")

    plugins = load_all_plugins()
    configs = load_all_configs()

    app = NetMorphCockpit(root, plugins, configs)
    root.mainloop()
class NetMorphCockpit:
    def __init__(self, master, plugin_registry, config_registry):
        self.master = master
        self.master.title("NetMorph 3.5 – Semantic Cockpit")
        self.master.geometry("1200x800")

        # Header
        header = tk.Label(master, text="📡 NetMorph Cockpit", font=("Helvetica", 16, "bold"), bg="#333", fg="#fff")
        header.pack(fill=tk.X, pady=5)

        # Tabs
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        # Create Tab Frames
        self.load_tabs(plugin_registry, config_registry)

    def load_tabs(self, plugin_registry, config_registry):
        # Panel A: Data Prep
        data_prep_tab = tk.Frame(self.notebook)
        DataPrepGUI(data_prep_tab, plugin_registry, config_registry)
        self.notebook.add(data_prep_tab, text="Data Prep")

        # Panel B: Semantic Validation
        validator_tab = tk.Frame(self.notebook)
        SemanticValidatorGUI(validator_tab, plugin_registry, config_registry)
        self.notebook.add(validator_tab, text="Semantic Validation")

        # Panel C: Traffic Forecast
        forecast_tab = tk.Frame(self.notebook)
        TrafficForecastGUI(forecast_tab, plugin_registry, config_registry)
        self.notebook.add(forecast_tab, text="Traffic Forecast")

        # Panel D: Coverage Intelligence
        coverage_tab = tk.Frame(self.notebook)
        CoverageIntelligenceGUI(coverage_tab, plugin_registry, config_registry)
        self.notebook.add(coverage_tab, text="Coverage Intelligence")

        # Panel E: Plugin Manager
        plugin_tab = tk.Frame(self.notebook)
        PluginManagerGUI(plugin_tab, plugin_registry, config_registry)
        self.notebook.add(plugin_tab, text="Plugin Manager")# Placeholder
if __name__ == "__main__":
    import tkinter as tk
    from plugin_registry.registry import load_all_plugins
    from config_loader.config_registry import load_all_configs

    root = tk.Tk()
    root.title("NetMorph 3.5 Cockpit [Standalone Test]")
    root.geometry("1024x768")

    plugins = load_all_plugins()
    configs = load_all_configs()

    app = NetMorphCockpit(root, plugins, configs)
    root.mainloop()