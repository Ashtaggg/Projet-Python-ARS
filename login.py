import pymysql
import hashlib
from dbconnect import mysqlconnect  # Importez la fonction depuis dbconnect.py
from dbconnect import cuicui
import tkinter as tk
import effacer
import register




def go_register():
    effacer.effacer_page()
    register.register_page()



def toggle_password_visibility(password, passwordButton):
    current_show_value = password.cget("show")
    if current_show_value == "*":
        password.config(show="")
        passwordButton.config(text="Hide")
    else:
        password.config(show="*")
        passwordButton.config(text="Show")




def verify_login(Email, Password, verify):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        db='projet_python_ars',
    )

    request = "SELECT COUNT(*) FROM customer WHERE Email = %s;"

    cur = conn.cursor()
    cur.execute(request, Email)
    conn.commit()
    output = cur.fetchall()

    if Email == "" or Password == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855":
        verify.config(text="Please complete all the fields")
    elif output[0][0] == 0:
        verify.config(text="Your email is not available")
    elif output[0][0] != 0:
        request = "SELECT CustomerID FROM customer WHERE Email = %s;"
        cur = conn.cursor()
        cur.execute(request, Email)
        conn.commit()
        output = cur.fetchall()

        request = "SELECT Password FROM customer WHERE CustomerID = %s;"
        cur = conn.cursor()
        cur.execute(request, output[0][0])
        conn.commit()
        output = cur.fetchall()
        if output[0][0] == Password:
            verify.config(text="Bienvenue")
        else:
            verify.config(text="Your password is not available")
        
    conn.close()

    


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
    passwordButton = tk.Button(
        text = "Show",
        bg = "white",
        fg = "black",
        font = ('broadway' , 10),
        command = lambda: toggle_password_visibility(password, passwordButton))

    verify = tk.Label(text = "",font = ('broadway' , 10))

    login = tk.Button(
        cuicui,
        text = "Sign up",
        bg = "black",
        fg = "white",
        font = ('broadway' , 10),
        command = lambda: verify_login(email.get(), hashlib.sha256(password.get().encode()).hexdigest(), verify))
    


    Cuicui.pack()

    Title.pack()

    Register.pack()
    register.pack()

    Email.pack()
    email.pack()

    Password.pack()
    password.pack()
    passwordButton.pack()

    login.pack()

    verify.pack()


    cuicui.mainloop() 




if __name__ == "__main__":
    login_page()