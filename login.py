import hashlib
import initialization
import tkinter as tk
import effacer
import register
import query
import customer
import page_accueil
import choice_person
import pay



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

    request = "SELECT PhotoProfil FROM customer WHERE Email = '" + str(Email) + "';"
    output = query.requestDataBase(request)
    PhotoProfil = output[0][0]

    initialization.member = customer.customer(CustomerID, FirstName, LastName, Email, BirthDate, Password, Type,
                                              PhotoProfil)


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
            completeMember(Email, Password)

            initialization.login = 1
            #customer.customer.customer_page(initialization.member)
            if initialization.lastPage == "page_accueil":
                page_accueil.CuicuiAirlinesApp.welcome_page(initialization.cuicui)
            elif initialization.lastPage == "choice_person":
                initialization.lastPage = "page_accueil"
                choice_person.flight.debut(initialization.FlightID)
            elif initialization.lastPage == "pay":
                initialization.lastPage = "choice_person"
            else:
                page_accueil.CuicuiAirlinesApp.welcome_page(initialization.cuicui)


        else:
            verify.config(text="Your password is not available")


def login_page():
    y0 = 125

    canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080,bg=initialization.bg_color)
    canvas.place(x=0, y=0)
    canvas.create_line(0, 0, 1920, 0, width=150, fill="black")

    Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white",
                      bg="black")
    Cuicui.place(x=50, y=15)

    Title = tk.Label(text="Login", font=('Helvetica', 30, 'bold'),bg=initialization.bg_color)
    Title.place(x=710, y=y0 + 25)

    if initialization.lastPage == "page_accueil":
        returnTo = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'),bg=initialization.bg_color)
        returnTo.place(x=50, y=100)
        returnTo.bind("<Button-1>", lambda event=None:page_accueil.CuicuiAirlinesApp.welcome_page(initialization.cuicui))
    elif initialization.lastPage == "choice_person":
        returnTo = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'),bg=initialization.bg_color)
        returnTo.place(x=50, y=100)
        returnTo.bind("<Button-1>", lambda event=None:choice_person.flight.debut(initialization.FlightID))
    

    Register = tk.Label(text="Not Registered ? Register", font=('Helvetica', 12, 'bold'),bg=initialization.bg_color)
    Register.place(x=665, y=y0 + 100)
    Register.bind("<Button-1>", go_register)

    Email = tk.Label(text="Email :", font=('Helvetica', 10, 'bold'),bg=initialization.bg_color)
    Email.place(x=610, y=y0 + 180)

    email_frame = tk.Frame(initialization.cuicui)
    email_frame.place(x=610, y=y0 + 200)

    email = tk.Entry(email_frame, fg="black",bg=initialization.bg_color, width=50)
    email.pack(ipady=5)

    Password = tk.Label(text="Password :", font=('Helvetica', 10, 'bold'),bg=initialization.bg_color)
    Password.place(x=610, y=y0 + 250)

    password_frame = tk.Frame(initialization.cuicui)
    password_frame.place(x=610, y=y0 + 270)

    password = tk.Entry(password_frame, fg="black",bg=initialization.bg_color, width=50, show="*")
    password.pack(ipady=5)

    passwordButton = tk.Button(
        text="Show",
        bg = initialization.bg_color,
        fg="black",
        font=('Helvetica', 10, 'bold'),
        command=lambda: toggle_password_visibility(password, passwordButton))
    passwordButton.place(x=920, y=y0 + 270)

    login = tk.Button(
        initialization.cuicui,
        text="Sign up",
        bg=initialization.bg_color,
        fg="black",
        font=('Helvetica', 10, 'bold'),
        command=lambda: verify_login(email.get(), hashlib.sha256(password.get().encode()).hexdigest(), verify))
    login.place(x=740, y=y0 + 320)

    verify = tk.Label(text="", font=('Helvetica', 10, 'bold'),bg=initialization.bg_color)
    verify.place(x=810, y=y0 + 322)

    initialization.cuicui.mainloop()


if __name__ == "__main__":
    login_page()