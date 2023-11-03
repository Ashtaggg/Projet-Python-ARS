import tkinter as tk
from dbconnect import cuicui

def effacer_page():
    for widget in cuicui.winfo_children():
        widget.destroy()