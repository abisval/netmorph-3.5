import os
import zipfile
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

class FileDiscoveryPanel(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.folder_path = tk.StringVar()
        self.supported_exts = [".zip", ".csv", ".xlsx"]

        self.build_ui()

    def build_ui(self):
        ttk.Label(self, text="📁 Select KPI Dump Directory").pack(pady=10)
        entry = ttk.Entry(self, textvariable=self.folder_path, width=80)
        entry.pack(padx=10)

        browse_btn = ttk.Button(self, text="🔍 Browse", command=self.select_folder)
        browse_btn.pack(pady=5)

        scan_btn = ttk.Button(self, text="📊 Scan & Process Files", command=self.scan_files)
        scan_btn.pack(pady=5)

        self.result_box = tk.Text(self, height=20, width=100)
        self.result_box.pack(padx=10, pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def scan_files(self):
        folder = self.folder_path.get()
        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Invalid folder selected.")
            return

        self.result_box.delete("1.0", tk.END)
        all_files = []
        for root, _, files in os.walk(folder):
            for f in files:
                ext = os.path.splitext(f)[1].lower()
                if ext in self.supported_exts:
                    path = os.path.join(root, f)
                    all_files.append(path)

                    # If zip file, extract preview
                    if ext == ".zip":
                        try:
                            with zipfile.ZipFile(path, 'r') as zip_ref:
                                self.result_box.insert(tk.END, f"📦 {f} → Contains: {zip_ref.namelist()[:5]}\n")
                        except Exception as e:
                            self.result_box.insert(tk.END, f"⚠️ Error reading {f}: {str(e)}\n")
                    else:
                        self.result_box.insert(tk.END, f"📄 {f}\n")

        if not all_files:
            self.result_box.insert(tk.END, "🚫 No supported KPI files found.\n")
        else:
            self.result_box.insert(tk.END, f"\n✅ {len(all_files)} KPI files detected.\n")
