# Place# gui/SemanticValidatorGUI.py

import tkinter as tk
from tkinter import ttk
import pandas as pd

class SemanticValidatorGUI:
    def __init__(self, master, plugin_registry, config_registry):
        self.master = master
        self.plugin_registry = plugin_registry
        self.config_registry = config_registry

        self.df = None  # To be passed from Data Prep later
        self.build_ui()

    def build_ui(self):
        ttk.Label(self.master, text="🧪 Semantic Validation Panel", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

        ttk.Button(self.master, text="Load Sample Data (Temp)", command=self.load_sample).pack(anchor="w", padx=10)
        ttk.Button(self.master, text="Run KPI Validation", command=self.run_validator).pack(anchor="w", padx=10, pady=3)
        ttk.Button(self.master, text="Run Cluster Outlier Detection", command=self.run_clustering).pack(anchor="w", padx=10, pady=3)

        self.log_text = tk.Text(self.master, height=15, wrap="none")
        self.log_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def load_sample(self):
        # Temporary loader until we wire DataPrep sharing
        try:
            self.df = pd.read_csv("assets/sample_kpi.csv")
            self.log_text.insert(tk.END, f"✅ Sample data loaded: {len(self.df)} rows\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"❌ Failed to load sample data: {e}\n")

    def run_validator(self):
        if self.df is None:
            self.log_text.insert(tk.END, "⚠️ No data loaded.\n")
            return

        try:
            validator = self.plugin_registry["Validators"]["KPIValidator"]()
            report = validator.validate(self.df)
            self.log_text.insert(tk.END, f"✅ KPI validation complete: {report}\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"❌ Validation failed: {e}\n")

    def run_clustering(self):
        if self.df is None:
            self.log_text.insert(tk.END, "⚠️ No data loaded.\n")
            return

        try:
            cluster_plugin = self.plugin_registry["Validators"]["ClusterOutlierPlugin"]()
            zones = cluster_plugin.detect(self.df)
            self.log_text.insert(tk.END, f"🔍 Cluster detection: {zones}\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"❌ Cluster plugin failed: {e}\n")