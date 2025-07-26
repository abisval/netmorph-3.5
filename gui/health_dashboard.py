# gui/health_dashboard.py

import tkinter as tk
from tkinter import ttk

class HealthDashboardPanel(ttk.Frame):
    def __init__(self, master=None, quit_callback=None):
        super().__init__(master, padding=20)
        self.quit_callback = quit_callback
        ttk.Label(self, text="📊 Health Dashboard (Coming Soon)", font=("Segoe UI", 14)).pack(pady=20)

        # Footer buttons
        footer = ttk.Frame(self)
        footer.pack(fill="x", pady=20)
        ttk.Button(footer, text="Close Tab 🔒", command=self.destroy).pack(side="left", padx=10)
        ttk.Button(footer, text="Exit Cockpit ❌", command=self.quit_callback).pack(side="right", padx=10)