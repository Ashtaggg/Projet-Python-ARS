import tkinter as tk
import initialization


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


def customer_page():
    y0 = 125

    canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080)
    canvas.place(x=0, y=0)
    canvas.create_line(0, 75, 1920, 75, width=5, fill="black")

    Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font = ('broadway' , 30))
    Cuicui.place(x=50, y=0)