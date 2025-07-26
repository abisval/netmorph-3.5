import tkinter as tk
from tkinter import filedialog, ttk
import os


class CockpitGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("🧭 NetMorph 3.5 – Cockpit")
        self.master.geometry("1000x700")

        self.allowed_extensions = {".csv", ".xml", ".log", ".tsv", ".json", ".txt", ".zip", ".xlsx"}

        self._create_menubar()
        tk.Label(self.master, text="Welcome to NetMorph Cockpit", font=("Segoe UI", 18, "bold")).pack(pady=30)

    def _create_menubar(self):
        menubar = tk.Menu(self.master)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Select Folder for Processing", command=self._launch_file_selector)
        menubar.add_cascade(label="FileProcessing", menu=file_menu)

        self.master.config(menu=menubar)

    def _launch_file_selector(self):
        file_window = tk.Toplevel(self.master)
        file_window.title("📁 Directory Explorer")
        file_window.geometry("650x450")
        file_window.lift()
        file_window.focus_force()

        path_entry = tk.Entry(file_window, width=60)
        path_entry.pack(pady=10)

        def browse_dir():
            selected_dir = filedialog.askdirectory()
            if selected_dir:
                path_entry.delete(0, tk.END)
                path_entry.insert(0, selected_dir)
                self._display_file_list(selected_dir)

        tk.Button(file_window, text="Browse", command=browse_dir).pack(pady=5)

        frame = tk.Frame(file_window)
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_tree = ttk.Treeview(
            frame,
            columns=("Filename", "Filetype", "Size (KB)"),
            show="headings",
            yscrollcommand=scrollbar.set
        )

        self.file_tree.heading("Filename", text="Filename")
        self.file_tree.heading("Filetype", text="Filetype")
        self.file_tree.heading("Size (KB)", text="Size (KB)")

        self.file_tree.column("Filename", width=400)
        self.file_tree.column("Filetype", width=100)
        self.file_tree.column("Size (KB)", width=100)

        self.file_tree.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_tree.yview)

        self._add_hover_preview()

    def _display_file_list(self, directory):
        for item in self.file_tree.get_children():
            self.file_tree.delete(item)

        try:
            files = os.listdir(directory)
            for f in files:
                full_path = os.path.join(directory, f)
                if os.path.isfile(full_path):
                    _, ext = os.path.splitext(f)
                    if ext.lower() not in self.allowed_extensions:
                        continue
                    name = os.path.splitext(f)[0]
                    ext = ext.lstrip(".") or "Unknown"
                    size_kb = os.path.getsize(full_path) // 1024
                    self.file_tree.insert("", tk.END, values=(name, ext, size_kb))
        except Exception as e:
            print(f"⚠️ Error reading directory: {e}")

    def _add_hover_preview(self):
        tooltip = tk.Label(self.master, bg="#ffffe0", relief="solid", bd=1, padx=5, font=("Segoe UI", 9))
        tooltip.place_forget()

        def on_motion(event):
            item = self.file_tree.identify_row(event.y)
            if item:
                values = self.file_tree.item(item, "values")
                tooltip.config(text=f"📄 {values[0]}.{values[1]} | Size: {values[2]} KB")
                tooltip.place(x=event.x_root + 10, y=event.y_root + 10)
            else:
                tooltip.place_forget()

        def on_leave(event):
            tooltip.place_forget()

        self.file_tree.bind("<Motion>", on_motion)
        self.file_tree.bind("<Leave>", on_leave)