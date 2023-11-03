import pymysql
from dbconnect import mysqlconnect  # Importez la fonction depuis dbconnect.py
from dbconnect import cuicui
import tkinter as tk
import effacer
import login

def go_login():
    effacer.effacer_page()
    login.login_page()


def register_page():

    Cuicui = tk.Label(cuicui, text="Cuicui Airline", font = ('broadway' , 30))     # Crée un libellé (label)

    Title = tk.Label(text="Create new account",font = ('broadway' , 15))

    Login = tk.Label(text="Already Registered?",font = ('broadway' , 10))
    login = tk.Button(     # Crée un bouton
        cuicui,
        text = "Login",
        bg = "white",
        fg = "black",
        font  =('broadway' , 10),
        command = go_login)

    Name = tk.Label(text="Name :",font = ('broadway' , 10))
    name = tk.Entry(fg = "black", bg = "white", width = 50)

    Surname = tk.Label(text="Surname :",font = ('broadway' , 10))
    surname = tk.Entry(fg = "black", bg = "white", width = 50)

    Email = tk.Label(text="Email :",font = ('broadway' , 10))
    email = tk.Entry(fg = "black", bg = "white", width = 50)

    Password = tk.Label(text="Password :",fon = ('broadway' , 10))
    password = tk.Entry(fg = "black", bg = "white", width = 50, show = "*")

    Date = tk.Label(text="Date of birth :",font = ('broadway' , 10))
    date = tk.Entry(fg = "black", bg = "white", width = 50)

    singup = tk.Button(     # Crée un bouton
        cuicui,
        text = "Sign up",
        bg = "black",
        fg = "white",
        font = ('broadway' , 10))




    Cuicui.pack()

    Title.pack()

    Login.pack()
    login.pack()

    Name.pack()
    name.pack()

    Surname.pack()
    surname.pack()

    Email.pack()
    email.pack()

    Password.pack()
    password.pack()

    Date.pack()
    date.pack()

    singup.pack()



    cuicui.mainloop() 


if __name__ == "__main__":
    register_page()
    