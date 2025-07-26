import tkinter as tk
from tkinter import ttk
import json
import os

STATUS_FILE = "status.json"

class HealthDashboardPanel(ttk.Frame):
    def __init__(self, master=None, quit_callback=None):
        super().__init__(master, padding=20)
        self.quit_callback = quit_callback
        self.tree = None
        self.build_ui()
        self.load_status()

    def build_ui(self):
        ttk.Label(self, text="🩺 Health Dashboard", font=("Segoe UI", 14, "bold")).pack(anchor='w', pady=(0, 10))

        self.tree = ttk.Treeview(self, columns=("Health", "Status", "Updated"), show="headings", height=15)
        self.tree.heading("Health", text="Health")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Updated", text="Last Updated")
        self.tree.column("Health", width=80, anchor="center")
        self.tree.column("Status", width=150, anchor="w")
        self.tree.column("Updated", width=120, anchor="center")
        self.tree.pack(fill="both", expand=True)

        # Footer controls
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=20)

        ttk.Button(btn_frame, text="Refresh 🔄", command=self.load_status).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="Close Tab 🔒", command=self.destroy).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="Exit Cockpit ❌", command=self.quit_callback).pack(side="right", padx=10)

    def load_status(self):
        self.tree.delete(*self.tree.get_children())
        if not os.path.exists(STATUS_FILE):
            self.tree.insert("", "end", values=["❌", "status.json missing", "-"])
            return

        try:
            with open(STATUS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            plugins = data.get("plugins", {})
            for name, info in plugins.items():
                icon = {
                    "✅": "🟢",
                    "⚠️": "🟡",
                    "❌": "🔴"
                }.get(info.get("health", ""), "⚪")
                self.tree.insert("", "end", values=[
                    icon, name, info.get("last_updated", "-")
                ])
        except Exception as e:
            self.tree.insert("", "end", values=["❌", "Error reading status.json", "-"])