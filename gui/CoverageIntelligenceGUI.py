# Placeholder
# gui/CoverageIntelligenceGUI.py

import tkinter as tk
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np

class CoverageIntelligenceGUI:
    def __init__(self, master, plugin_registry, config_registry):
        self.master = master
        self.plugin_registry = plugin_registry
        self.config_registry = config_registry
        self.site_df = None

        self.figure, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)

        self.build_ui()

    def build_ui(self):
        ttk.Label(self.master, text="🗺️ Coverage Intelligence", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

        # Load site config file
        ttk.Button(self.master, text="Load Site Geometry File", command=self.load_geometry).pack(anchor="w", padx=10)
        ttk.Button(self.master, text="Run Kriging Interpolation", command=self.run_kriging).pack(anchor="w", padx=10, pady=3)
        ttk.Button(self.master, text="Run Cluster Detection", command=self.run_cluster).pack(anchor="w", padx=10, pady=3)

        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.log_text = tk.Text(self.master, height=10, wrap="none")
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def load_geometry(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv"), ("Excel", "*.xlsx")])
            loader = self.plugin_registry["Geometry"]["SiteGeometryLoaderPlugin"](file_path)
            self.site_df = loader.load()
            self.log_text.insert(tk.END, f"✅ Loaded {len(self.site_df)} sites from geometry file\n")
            self.draw_sectors(self.site_df)
        except Exception as e:
            self.log_text.insert(tk.END, f"❌ Error loading site geometry: {e}\n")

    def draw_sectors(self, df):
        self.ax.clear()
        for _, row in df.iterrows():
            lat, lon = row["Latitude"], row["Longitude"]
            azimuth = row["Azimuth"]
            beamwidth = 65
            radius = 0.01
            angles = np.radians(np.linspace(azimuth - beamwidth/2, azimuth + beamwidth/2, 20))
            x = lon + radius * np.cos(angles)
            y = lat + radius * np.sin(angles)
            self.ax.plot([lon] + list(x), [lat] + list(y), 'r-', alpha=0.4)
            self.ax.plot(lon, lat, 'ko')
            self.ax.text(lon, lat, row["Site_ID"], fontsize=8, ha="center")
        self.ax.set_title("Sector Beam Overlay")
        self.canvas.draw()

    def run_kriging(self):
        if self.site_df is None:
            self.log_text.insert(tk.END, "⚠️ Load site geometry first.\n")
            return

        try:
            kriging_plugin = self.plugin_registry["Coverage"]["KrigingCoveragePlugin"]()
            heatmap = kriging_plugin.interpolate(self.site_df)
            self.ax.imshow(heatmap, cmap="viridis", extent=(0, 1, 0, 1))
            self.canvas.draw()
            self.log_text.insert(tk.END, "🌡️ Kriging interpolation complete\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"❌ Kriging failed: {e}\n")

    def run_cluster(self):
        try:
            cluster_plugin = self.plugin_registry["Coverage"]["ClusterZonePlugin"]()
            zones = cluster_plugin.detect_hotspots(self.site_df)
            self.log_text.insert(tk.END, f"🔍 Cluster detection complete: {zones}\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"❌ Cluster plugin failed: {e}\n")