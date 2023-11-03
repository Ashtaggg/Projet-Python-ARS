import pymysql
from dbconnect import mysqlconnect  # Importez la fonction depuis dbconnect.py
from dbconnect import cuicui
import tkinter as tk

label = tk.Label(cuicui, text="Hello, Accueil!")     # Crée un libellé (label)
label.pack()

cuicui.mainloop()