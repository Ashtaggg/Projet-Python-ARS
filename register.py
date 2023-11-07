import pymysql
import hashlib
from dbconnect import mysqlconnect
from dbconnect import cuicui
import tkinter as tk
import effacer
import login




def go_login():
    effacer.effacer_page()
    login.login_page()




def toggle_password_visibility(password, passwordButton):
    current_show_value = password.cget("show")
    if current_show_value == "*":
        password.config(show="")
        passwordButton.config(text="Hide")
    else:
        password.config(show="*")
        passwordButton.config(text="Show")




def verify_register(Firstname, Name, Email, Username, Password, Type, MembershipNumber, verify):
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
    conn.close()

    if Firstname == "" or Name == "" or Email == "" or Password == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855":
        verify.config(text="Please complete all the fields")
    elif output[0][0] != 0:
        verify.config(text="Your email is not available")
    else:
        verify.config(text="")
        register(Firstname, Name, Email, Username, Password, Type, MembershipNumber)




def register(Firstname, Name, Email, Username, Password, Type, MembershipNumber):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        db='projet_python_ars',
    )

    request = "INSERT INTO `customer` (`FirstName`, `LastName`, `Email`, `Username`, `Password`, `Type`, `MembershipNumber`) VALUES(%s, %s, %s, %s, %s, %s, %s);"

    cur = conn.cursor()
    cur.execute(request, (Firstname, Name, Email, Username, Password, Type, MembershipNumber))
    conn.commit()
    conn.close()




def register_page():

    Cuicui = tk.Label(cuicui, text="Cuicui Airline", font = ('broadway' , 30))

    Title = tk.Label(text = "Create new account",font = ('broadway' , 15))

    Login = tk.Label(text = "Already Registered?",font = ('broadway' , 10))
    login = tk.Button(
        cuicui,
        text = "Login",
        bg = "white",
        fg = "black",
        font = ('broadway' , 10),
        command = go_login)

    Name = tk.Label(text = "Name :",font = ('broadway' , 10))
    name = tk.Entry(fg = "black", bg = "white", width = 50)

    Firstname = tk.Label(text = "Firstname :",font = ('broadway' , 10))
    firstname = tk.Entry(fg = "black", bg = "white", width = 50)

    Email = tk.Label(text = "Email :",font = ('broadway' , 10))
    email = tk.Entry(fg = "black", bg = "white", width = 50)

    Password = tk.Label(text="Password :",font = ('broadway' , 10))
    password = tk.Entry(fg = "black", bg = "white", width = 50, show = "*")
    passwordButton = tk.Button(
        text = "Show",
        bg = "white",
        fg = "black",
        font = ('broadway' , 10),
        command = lambda: toggle_password_visibility(password, passwordButton))
    


    Date = tk.Label(text = "Date of birth :",font = ('broadway' , 10))
    date = tk.Entry(fg = "black", bg = "white", width = 50)


    verify = tk.Label(text = "",font = ('broadway' , 10))


    signup = tk.Button(
    cuicui,
    text  ="Sign up",
    bg = "black",
    fg = "white",
    font = ('broadway', 10),
    command = lambda: verify_register(firstname.get(), name.get(), email.get(), 0, hashlib.sha256(password.get().encode()).hexdigest(), 0, 0, verify))


    Cuicui.pack()

    Title.pack()

    Login.pack()
    login.pack()

    Name.pack()
    name.pack()

    Firstname.pack()
    firstname.pack()

    Email.pack()
    email.pack()

    Password.pack()
    password.pack()
    passwordButton.pack()

    Date.pack()
    date.pack()

    signup.pack()

    verify.pack()

    cuicui.mainloop() 




if __name__ == "__main__":
    register_page()
    