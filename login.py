import hashlib
import initialization
import tkinter as tk
import effacer
import register
import query
import customer
import page_reservation



def go_register(temp):
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



def completeMember(Email, Password):

    request = "SELECT CustomerID FROM customer WHERE Email = '" + str(Email) + "';"
    output = query.requestDataBase(request)
    CustomerID = output[0][0]

    request = "SELECT Firstname FROM customer WHERE Email = '" + str(Email) + "';"
    output = query.requestDataBase(request)
    FirstName = output[0][0]

    request = "SELECT LastName FROM customer WHERE Email = '" + str(Email) + "';"
    output = query.requestDataBase(request)
    LastName = output[0][0]

    request = "SELECT BirthDate FROM customer WHERE Email = '" + str(Email) + "';"
    output = query.requestDataBase(request)
    BirthDate = output[0][0]

    request = "SELECT Type FROM customer WHERE Email = '" + str(Email) + "';"
    output = query.requestDataBase(request)
    Type = output[0][0]

    request = "SELECT MembershipNumber FROM customer WHERE Email = '" + str(Email) + "';"
    output = query.requestDataBase(request)
    MembershipNumber = output[0][0]


    initialization.member = customer.customer(CustomerID, FirstName, LastName, Email, BirthDate, Password, Type, MembershipNumber)
    



def verify_login(Email, Password, verify):

    request = "SELECT COUNT(*) FROM customer WHERE Email = '" + str(Email) + "';"

    output = query.requestDataBase(request)

    if Email == "" or Password == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855":
        verify.config(text="Please complete all the fields")
    elif output[0][0] == 0:
        verify.config(text="Your email is not available")
    elif output[0][0] != 0:
        request = "SELECT CustomerID FROM customer WHERE Email = '" + str(Email) + "';"
        output = query.requestDataBase(request)

        request = "SELECT Password FROM customer WHERE CustomerID = '" + str(output[0][0]) + "';"
        output = query.requestDataBase(request)
        if output[0][0] == Password:
            effacer.effacer_page()
            page_reservation.FlightReservationApp(cuicui)
            completeMember(Email, Password)
        else:
            verify.config(text="Your password is not available")

    


def login_page():
    y0 = 125

    canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080)
    canvas.place(x=0, y=0)
    canvas.create_line(0, 75, 1920, 75, width=5, fill="black")

    Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font = ('broadway' , 30))
    Cuicui.place(x=50, y=0)


    Title = tk.Label(text="Login",font = ('broadway' , 20))
    Title.place(x=715, y=y0+50)


    Register = tk.Label(text="Not Registered ? Register",font = ('broadway' , 10))
    Register.place(x=665, y=y0+100)
    Register.bind("<Button-1>", go_register)


    Email = tk.Label(text="Email :",font = ('broadway' , 10))
    Email.place(x=600, y=y0+180)

    email = tk.Entry(fg = "black", bg = "white", width = 50)
    email.place(x=600, y=y0+200)



    Password = tk.Label(text="Password :",fon = ('broadway' , 10))
    Password.place(x=600, y=y0+230)
    
    password = tk.Entry(fg = "black", bg = "white", width = 50, show = "*")
    password.place(x=600, y=y0+250)

    passwordButton = tk.Button(
        text = "Show",
        bg = "white",
        fg = "black",
        font = ('broadway' , 10),
        command = lambda: toggle_password_visibility(password, passwordButton))
    passwordButton.place(x=910, y=y0+245)


    login = tk.Button(
            initialization.cuicui,
            text = "Sign up",
            bg = "black",
            fg = "white",
            font = ('broadway' , 10),
            command = lambda: verify_login(email.get(), hashlib.sha256(password.get().encode()).hexdigest(), verify))
    login.place(x=730, y=y0+300)


    verify = tk.Label(text = "",font = ('broadway' , 10))
    verify.place(x=800, y=y0+302)


    initialization.cuicui.mainloop() 




if __name__ == "__main__":
    login_page()