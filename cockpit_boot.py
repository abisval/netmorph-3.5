import tkinter as tk
from gui import CockpitGUI

def main():
    root = tk.Tk()
    cockpit = CockpitGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()