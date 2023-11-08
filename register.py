import hashlib
import initialization
import tkinter as tk
import effacer
import login
import query
import customer




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




def verify_register(Firstname, Name, Email, BirthDate, Password, Type, MembershipNumber, verify):

    request = "SELECT COUNT(*) FROM customer WHERE Email = '" + str(Email) + "';"

    output = query.requestDataBase(request)

    if Firstname == "" or Name == "" or Email == "" or Password == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855":
        verify.config(text="Please complete all the fields")
    elif output[0][0] != 0:
        verify.config(text="Your email is not available")
    else:
        verify.config(text="")
        request = "INSERT INTO `customer` (`FirstName`, `LastName`, `Email`, `BirthDate`, `Password`, `Type`, `MembershipNumber`) VALUES('" + str(Firstname) + "', '" + str(Name) + "', '" + str(Email) + "', '" + str(BirthDate) + "', '" + str(Password) + "', '" + str(Type) + "', '" + str(MembershipNumber) + "');"
        query.requestDataBase(request)





def register_page():
    y0 = 125

    canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080)
    canvas.place(x=0, y=0)
    canvas.create_line(0, 75, 1920, 75, width=5, fill="black")

    Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font = ('broadway' , 30))
    Cuicui.place(x=50, y=0)

    Title = tk.Label(text = "Create new account",font = ('broadway' , 20))
    Title.place(x=610, y=y0+50)

    Login = tk.Label(text = "Already Registered ? Login",font = ('broadway' , 10))
    Login.place(x=665, y=y0+100)
    Login.bind("<Button-1>", go_login)
    

    Name = tk.Label(text = "Name :",font = ('broadway' , 10))
    Name.place(x=600, y=y0+180)

    name = tk.Entry(fg = "black", bg = "white", width = 50)
    name.place(x=600, y=y0+200)



    Firstname = tk.Label(text = "Firstname :",font = ('broadway' , 10))
    Firstname.place(x=600, y=y0+230)

    firstname = tk.Entry(fg = "black", bg = "white", width = 50)
    firstname.place(x=600, y=y0+250)



    Email = tk.Label(text = "Email :",font = ('broadway' , 10))
    Email.place(x=600, y=y0+280)

    email = tk.Entry(fg = "black", bg = "white", width = 50)
    email.place(x=600, y=y0+300)



    Password = tk.Label(text="Password :",font = ('broadway' , 10))
    Password.place(x=600, y=y0+330)

    password = tk.Entry(fg = "black", bg = "white", width = 50, show = "*")
    password.place(x=600, y=y0+350)
    
    passwordButton = tk.Button(
        text = "Show",
        bg = "white",
        fg = "black",
        font = ('broadway' , 10),
        command = lambda: toggle_password_visibility(password, passwordButton))
    passwordButton.place(x=910, y=y0+345)
    


    Date = tk.Label(text = "Date of birth : (yyyy-mm-dd)",font = ('broadway' , 10))
    Date.place(x=600, y=y0+380)

    date = tk.Entry(fg = "black", bg = "white", width = 50)
    date.place(x=600, y=y0+400)



    signup = tk.Button(
    initialization.cuicui,
    text  ="Sign up",
    bg = "black",
    fg = "white",
    font = ('broadway', 10),
    command = lambda: verify_register(firstname.get(), name.get(), email.get(), date.get(), hashlib.sha256(password.get().encode()).hexdigest(), 0, 0, verify))
    signup.place(x=730, y=y0+450)


    verify = tk.Label(text = "",font = ('broadway' , 10))
    verify.place(x=800, y=y0+452)



    initialization.cuicui.mainloop() 




if __name__ == "__main__":
    register_page()
    