import tkinter as tk
import initialization
from PIL import Image, ImageTk


class customer():
    def __init__(self, CustomerID, FirstName, LastName, Email, BirthDate, Password, Type, MembershipNumber):
        self.CustomerID = CustomerID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.BirthDate = BirthDate
        self.Password = Password
        self.Type = Type
        self.MembershipNumber = MembershipNumber

    def customer_page(self):
        y0 = 125

        canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080)
        canvas.place(x=0, y=0)
        canvas.create_line(0, 0, 1920, 0, width=150, fill="black")
        canvas.create_line(650, 220, 650, 700, width=2, fill="black")

        Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font = ('Helvetica' , 30, 'bold'), fg="white", bg="black")
        Cuicui.place(x=50, y=15)

        image = Image.open("./photos/photo_profil.png")
        image = image.resize((200, 200))
        image = ImageTk.PhotoImage(image)
        canvas.create_image(170, 200, anchor=tk.NW, image=image)

        Title = tk.Label(text="Account",font = ('Helvetica' , 30, 'bold'))
        Title.place(x=700, y=y0-25)

        TitleLeft = tk.Label(text="General informations",font = ('Helvetica' , 20, 'bold'))
        TitleLeft.place(x=170, y=y0+320)

        TitleRight = tk.Label(text="Past flights",font = ('Helvetica' , 20, 'bold'))
        TitleRight.place(x=1030, y=y0+100)



        firstname = tk.Label(text=self.FirstName,font = ('Helvetica' , 12, 'bold'))
        firstname.place(x=170, y=y0+410)


        name = tk.Label(text=self.LastName,font = ('Helvetica' , 12, 'bold'))
        name.place(x=170, y=y0+450)


        email = tk.Label(text=self.Email,font = ('Helvetica' , 12, 'bold'))
        email.place(x=170, y=y0+490)


        BirthDate = tk.Label(text="Date of birth :",font = ('Helvetica' , 10, 'bold'))
        BirthDate.place(x=170, y=y0+532)

        birthDate = tk.Label(text=self.BirthDate,font = ('Helvetica' , 12, 'bold'))
        birthDate.place(x=265, y=y0+530)



        initialization.cuicui.mainloop() 






if __name__ == "__main__":
    customer.customer_page(initialization.member)