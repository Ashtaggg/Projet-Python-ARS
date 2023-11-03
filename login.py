import pymysql
from dbconnect import mysqlconnect  # Importez la fonction depuis dbconnect.py
from dbconnect import cuicui
import tkinter as tk
import effacer
import register




def login_page():
    effacer.effacer_page()


    Cuicui = tk.Label(cuicui, text="Cuicui Airline", font = ('broadway' , 30))     # Crée un libellé (label)

    Title = tk.Label(text="Create new account",font = ('broadway' , 15))

    Register = tk.Label(text="Already Registered? Login",font = ('broadway' , 10))
    register = tk.Button(     # Crée un bouton
        cuicui,
        text = "Login",
        bg = "black",
        fg = "white",
        font  =('broadway' , 10),
        command = register.login_page)
    


    Cuicui.pack()

    Title.pack()

    Register.pack()
    register.pack()

    cuicui.mainloop() 