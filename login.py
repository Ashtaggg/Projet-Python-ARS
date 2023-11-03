import pymysql
from dbconnect import mysqlconnect  # Importez la fonction depuis dbconnect.py
from dbconnect import cuicui
import tkinter as tk
import effacer
import register

def go_register():
    effacer.effacer_page()
    register.register_page()


def login_page():
    Cuicui = tk.Label(cuicui, text="Cuicui Airline", font = ('broadway' , 30))

    Title = tk.Label(text="Login",font = ('broadway' , 15))

    Register = tk.Label(text="Not Registered?",font = ('broadway' , 10))
    register = tk.Button(
        cuicui,
        text = "Register",
        bg = "white",
        fg = "black",
        font  =('broadway' , 10),
        command = go_register)


    Email = tk.Label(text="Email :",font = ('broadway' , 10))
    email = tk.Entry(fg = "black", bg = "white", width = 50)

    Password = tk.Label(text="Password :",fon = ('broadway' , 10))
    password = tk.Entry(fg = "black", bg = "white", width = 50, show = "*")

    login = tk.Button(
        cuicui,
        text = "Sign up",
        bg = "black",
        fg = "white",
        font = ('broadway' , 10))
    


    Cuicui.pack()

    Title.pack()

    Register.pack()
    register.pack()

    Email.pack()
    email.pack()

    Password.pack()
    password.pack()

    login.pack()


    cuicui.mainloop() 


if __name__ == "__main__":
    login_page()