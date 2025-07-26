import tkinter as tk
from tkinter import ttk

class PluginPanel(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        ttk.Label(self, text="🔌 Plugin Panel (Coming Soon)").pack(pady=20)