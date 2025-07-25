# Placehold# gui/DataPrepGUI.py

import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd

class DataPrepGUI:
    def __init__(self, master, plugin_registry, config_registry):
        self.master = master
        self.plugin_registry = plugin_registry
        self.config_registry = config_registry

        self.df = None  # Loaded data

        self.build_ui()

    def build_ui(self):
        ttk.Label(self.master, text="📁 LTE Data Loader", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
        ttk.Button(self.master, text="Load CSV/Excel File", command=self.load_file).pack(anchor="w", padx=10)

        self.file_label = ttk.Label(self.master, text="No file loaded", foreground="gray")
        self.file_label.pack(anchor="w", padx=10, pady=3)

        ttk.Button(self.master, text="Run Preprocessing", command=self.run_cleaning).pack(anchor="w", padx=10, pady=10)

        self.log_text = tk.Text(self.master, height=15, wrap="none")
        self.log_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
        if file_path:
            self.df = pd.read_csv(file_path) if file_path.endswith(".csv") else pd.read_excel(file_path)
            self.file_label.config(text=f"Loaded: {file_path.split('/')[-1]}")
            self.log_text.insert(tk.END, f"✅ Loaded {len(self.df)} rows from file\n")

    def run_cleaning(self):
        if self.df is None:
            self.log_text.insert(tk.END, "⚠️ No file loaded. Please load a dataset first.\n")
            return

        try:
            cleaner = self.plugin_registry["Preprocessor"]["DataCleanerPlugin"]()
            cleaned_df = cleaner.process(self.df)
            self.df = cleaned_df
            self.log_text.insert(tk.END, "✨ Preprocessing complete – nulls imputed, KPIs normalized\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"❌ Error during preprocessing: {e}\n")
