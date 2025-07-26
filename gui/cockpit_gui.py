import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from .CockpitState import CockpitState

class CockpitGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NetMorph Cockpit")
        self.root.state("zoomed")  # Fullscreen mode
        self.state = CockpitState()
        self.plugin_ref = None
        self.selected_dir = ""

        self._setup_ui()
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_exit)

    def _setup_ui(self):
        # ── Toolbar ──
        toolbar = ttk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        ttk.Button(toolbar, text="📂 Select Directory", command=self.choose_directory).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(toolbar, text="🧩 Open Plugin", command=self.open_plugin).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="🛑 Exit", command=self.confirm_exit).pack(side=tk.RIGHT, padx=5)

        # ── Status Bar ──
        self.status_bar = ttk.Label(self.root, text="🟢 Ready", relief=tk.SUNKEN, anchor="w")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def choose_directory(self):
        initial_dir = self.state.get_last_dir() or os.getcwd()
        dir_path = filedialog.askdirectory(title="Select Working Directory", initialdir=initial_dir)
        if dir_path:
            self.state.save_last_dir(dir_path)
            self.selected_dir = dir_path
            self.log_status(f"Directory selected: {dir_path}")

    def open_plugin(self):
        if not self.selected_dir:
            messagebox.showwarning("No Directory", "Please select a directory first.")
            return

        if self.plugin_ref and self.plugin_ref.winfo_exists():
            self.plugin_ref.lift()
            self.plugin_ref.focus_force()
            self.log_status("Plugin already open.")
        else:
            self.plugin_ref = tk.Toplevel(self.root)
            self.plugin_ref.title("Plugin View: File Listing")
            self.plugin_ref.geometry("600x400")
            self.plugin_ref.focus_force()

            ttk.Label(self.plugin_ref, text=f"📁 Files in: {os.path.basename(self.selected_dir)}", font=("Segoe UI", 12)).pack(pady=10)

            listbox = tk.Listbox(self.plugin_ref, width=80, height=20)
            listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

            files = os.listdir(self.selected_dir)
            for file in files:
                listbox.insert(tk.END, f"• {file}")

            self.log_status("Plugin window launched with directory contents.")

    def confirm_exit(self):
        if messagebox.askokcancel("Exit", "Exit NetMorph Cockpit?"):
            self.log_status("Session terminated.")
            self.root.destroy()

    def log_status(self, msg):
        self.status_bar.config(text=msg)
        print("[Status]", msg)

    def run(self):
        self.root.mainloop()