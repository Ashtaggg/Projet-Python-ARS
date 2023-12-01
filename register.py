import hashlib
import initialization
import tkinter as tk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import base64
import effacer
import login
import query
import customer
import page_accueil
import choice_person




def go_login(temp):
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




def verify_register(Firstname, Name, Email, BirthDate, Password, Type, PhotoProfil, verify):

    
    chemin_image = "./photos/profil_picture/photo_profil.png"
    image = Image.open(chemin_image)
    image = image.resize((200, 200))
    with open(chemin_image, "rb") as image_file:
        image_data = image_file.read()
    PhotoProfil = base64.b64encode(image_data).decode('utf-8')


    request = "SELECT COUNT(*) FROM customer WHERE Email = '" + str(Email) + "';"

    output = query.requestDataBase(request)

    if Firstname == "" or Name == "" or Email == "" or Password == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855":
        verify.config(text="Please complete all the fields")
    elif output[0][0] != 0:
        verify.config(text="Your email is not available")
    else:
        verify.config(text="")
        request = "INSERT INTO `customer` (`FirstName`, `LastName`, `Email`, `BirthDate`, `Password`, `Type`, `PhotoProfil`) VALUES('" + str(Firstname) + "', '" + str(Name) + "', '" + str(Email) + "', '" + str(BirthDate) + "', '" + str(Password) + "', '" + str(Type) + "', '" + str(PhotoProfil) + "');"
        query.requestDataBase(request)
        go_login(0)





def register_page():
    y0 = 125

    canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080,bg=initialization.bg_color)
    canvas.place(x=0, y=0)
    canvas.create_line(0, 0, 1920, 0, width=150, fill="black")

    Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font = ('Helvetica' , 30, 'bold'), fg="white", bg="black")
    Cuicui.place(x=50, y=15)

    Title = tk.Label(text = "Create new account",font = ('Helvetica' , 30, 'bold'),bg=initialization.bg_color)
    Title.place(x=570, y=y0+25)

    if initialization.lastPage == "page_accueil":
        returnTo = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'),bg=initialization.bg_color)
        returnTo.place(x=50, y=100)
        returnTo.bind("<Button-1>", lambda event=None:page_accueil.CuicuiAirlinesApp.welcome_page(initialization.cuicui))
    elif initialization.lastPage == "choice_person":
        returnTo = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'))
        returnTo.place(x=50, y=100)
        returnTo.bind("<Button-1>", lambda event=None:choice_person.flight.debut(initialization.FlightID))

    Login = tk.Label(text = "Already Registered ? Login",font = ('Helvetica' , 12, 'bold'),bg=initialization.bg_color)
    Login.place(x=665, y=y0+100)
    Login.bind("<Button-1>", go_login)
    

    Firstname = tk.Label(text = "Firstname :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
    Firstname.place(x=610, y=y0+180)

    firstname_frame = tk.Frame(initialization.cuicui)
    firstname_frame.place(x=610, y=y0+200)

    firstname = tk.Entry(firstname_frame, fg="black", bg=initialization.bg_color, width=50)
    firstname.pack(ipady=5)



    Name = tk.Label(text = "Name :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
    Name.place(x=610, y=y0+250)

    name_frame = tk.Frame(initialization.cuicui)
    name_frame.place(x=610, y=y0+270)

    name = tk.Entry(name_frame, fg="black", width=50,bg=initialization.bg_color)
    name.pack(ipady=5)



    Email = tk.Label(text = "Email :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
    Email.place(x=610, y=y0+320)

    email_frame = tk.Frame(initialization.cuicui)
    email_frame.place(x=610, y=y0+340)

    email = tk.Entry(email_frame, fg="black", width=50,bg=initialization.bg_color)
    email.pack(ipady=5)



    Password = tk.Label(text="Password :", font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
    Password.place(x=610, y=y0+390)

    password_frame = tk.Frame(initialization.cuicui)
    password_frame.place(x=610, y=y0+410)

    password = tk.Entry(password_frame, fg="black", width=50, show="*",bg=initialization.bg_color)
    password.pack(ipady=5)
    
    passwordButton = tk.Button(
        text = "Show",
        bg=initialization.bg_color,
        fg = "black",
        font = ('Helvetica' , 10, 'bold'),
        command = lambda: toggle_password_visibility(password, passwordButton))
    passwordButton.place(x=920, y=y0+410)
    


    Date = tk.Label(text = "Date of birth :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
    Date.place(x=610, y=y0+460)

    date_frame = tk.Frame(initialization.cuicui)
    date_frame.place(x=610, y=y0+480)

    date = DateEntry(date_frame, date_pattern="yyyy-mm-dd", fg="black", width=40, font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
    date.pack(ipady=5)



    signup = tk.Button(
    initialization.cuicui,
    text  ="Sign up",
    bg=initialization.bg_color,
    fg = "black",
    font = ('Helvetica', 10, 'bold'),
    command = lambda: verify_register(firstname.get(), name.get(), email.get(), date.get(), hashlib.sha256(password.get().encode()).hexdigest(), 0, 0, verify))
    signup.place(x=740, y=y0+530)


    verify = tk.Label(text = "",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
    verify.place(x=810, y=y0+532)



    initialization.cuicui.mainloop() 




if __name__ == "__main__":
    register_page()
    