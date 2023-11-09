import tkinter as tk
from initialization import cuicui

def effacer_page():
    for widget in cuicui.winfo_children():
        widget.destroy()