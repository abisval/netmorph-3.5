# Placeholder# gui/TrafficForecastGUI.py

import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TrafficForecastGUI:
    def __init__(self, master, plugin_registry, config_registry):
        self.master = master
        self.plugin_registry = plugin_registry
        self.config_registry = config_registry

        self.df = None  # Will receive KPI data to forecast on
        self.model_var = tk.StringVar(value="Random Forest")
        self.build_ui()

    def build_ui(self):
        ttk.Label(self.master, text="📈 Traffic Forecast Panel", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

        # Model Selector
        ttk.Label(self.master, text="Select Forecast Model:").pack(anchor="w", padx=10)
        model_menu = ttk.Combobox(self.master, textvariable=self.model_var, state="readonly")
        model_menu['values'] = ["Random Forest", "SVR", "ANN"]
        model_menu.pack(anchor="w", padx=10, pady=2)

        ttk.Button(self.master, text="Load Sample KPI Data", command=self.load_sample).pack(anchor="w", padx=10)
        ttk.Button(self.master, text="Run Forecast", command=self.run_forecast).pack(anchor="w", padx=10, pady=5)

        # Chart Canvas
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Log Console
        self.log_text = tk.Text(self.master, height=10, wrap="none")
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def load_sample(self):
        try:
            self.df = pd.read_csv("assets/sample_kpi.csv")
            self.log_text.insert(tk.END, f"✅ Sample data loaded: {len(self.df)} rows\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"❌ Failed to load sample data: {e}\n")

    def run_forecast(self):
        if self.df is None:
            self.log_text.insert(tk.END, "⚠️ No data available. Load KPI data first.\n")
            return

        model_name = self.model_var.get()
        try:
            model_plugin = self.plugin_registry["Predictive"][f"TrafficPredictor{model_name.replace(' ', '')}"]()
            predictions, accuracy = model_plugin.predict(self.df)
            self.ax.clear()
            self.ax.plot(self.df["ActualTraffic"], label="Actual", color="blue")
            self.ax.plot(predictions, label="Predicted", color="orange")
            self.ax.set_title(f"{model_name} Traffic Prediction")
            self.ax.legend()
            self.canvas.draw()

            self.log_text.insert(tk.END, f"✅ Forecast complete (Model: {model_name})\nAccuracy: {accuracy:.2f}\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"❌ Forecast failed: {e}\n")
