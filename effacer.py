import tkinter as tk
import initialization

def effacer_page():
    for widget in initialization.cuicui.winfo_children():
        widget.destroy()