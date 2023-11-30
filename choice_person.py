# Import necessary libraries and modules
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import initialization
import login
import customer
import query
import pay
import page_accueil

# Define a class 'flight' to encapsulate flight-related functionality
class flight():
    # Constructor to initialize Flight object with basic details
    def __init__(self, FlightID, DepartureCity, ArrivalCity, DepartureTime, ArrivalTime, TicketPrice, SeatsAvailable):
        self.FlightID = FlightID
        self.DepartureCity = DepartureCity
        self.ArrivalCity = ArrivalCity
        self.DepartureTime = DepartureTime
        self.ArrivalTime = ArrivalTime
        self.TicketPrice = TicketPrice
        self.SeatsAvailable = SeatsAvailable

    # Method to fetch complete flight details from the database
    def completeFlight(self):
        # Queries to retrieve details from the database
        request = "SELECT DepartureCity FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.DepartureCity = output[0][0]

        request = "SELECT ArrivalCity FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.ArrivalCity = output[0][0]

        request = "SELECT DepartureTime FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.DepartureTime = output[0][0]

        request = "SELECT ArrivalTime FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.ArrivalTime = output[0][0]

        request = "SELECT TicketPrice FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.TicketPrice = output[0][0]

        request = "SELECT SeatsAvailable FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.SeatsAvailable = output[0][0]

    # Method to display flight information on a canvas
    def displayFlight(self, canvas):
        y0 = 75

        canvas.create_text(250, y0 + 190, text=self.DepartureCity + "  >  " + self.ArrivalCity, font=('Helvetica', 14, 'bold'))
        canvas.create_text(275, y0 + 230, text=str(self.DepartureTime)[:16], font=('Helvetica', 10, 'bold'))
        canvas.create_text(400, y0 + 230, text=self.DepartureCity, font=('Helvetica', 10, 'bold'))
        canvas.create_text(275, y0 + 250, text=str(self.ArrivalTime)[:16], font=('Helvetica', 10, 'bold'))
        canvas.create_text(400, y0 + 250, text=self.ArrivalCity, font=('Helvetica', 10, 'bold'))

        canvas.create_text(650, y0 + 255, text=str(self.SeatsAvailable) + " €", font=('Helvetica', 10, 'bold'))

        canvas.create_rectangle(100, y0 + 160, 700, y0 + 280)

    # Method to validate passenger information
    def validationPassenger(self, passagers, verify):
        fieldsCompleted = all(passager['member_type'] is not None and passager['ticket_type'] is not None for passager in passagers)
        if fieldsCompleted:
            fieldsSelected = all(passager['member_type'] != "Select Member Type" and passager['ticket_type'] != "Select ticket class" for passager in passagers)
            if fieldsSelected:
                total_price = pay.calculate_price(passagers)
                #messagebox.showinfo("Total Price", f"The total price is {total_price} €.")
                if initialization.login == 0:
                    initialization.lastPage = "choice_person"
                    verify.config(text="You have to login for pay")
                elif initialization.login == 1:
                    initialization.lastPage = "choice_person"
                    pay.process_payment(initialization.cuicui, passagers, self)
            else:
                verify.config(text="Please complete all the fields")
        else:
            verify.config(text="Please complete all the fields")

    # Method to modify passenger information
    def modifPassenger2(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva, tag, member_type, ticket_type):
        passagers[int(tag)-1]['member_type'] = member_type
        passagers[int(tag)-1]['ticket_type'] = ticket_type

        flight.displayPassenger(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva)

    # Method to initiate passenger modification
    def modifPassenger(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva, tag):
        modiPassenger_canva.create_text(300, 50, text="Passenger " + str(tag) + " :", font=('Helvetica', 14, 'bold'))

        member_type_combobox = ttk.Combobox(modiPassenger_canva, values=['Senior', 'Regular', 'Children'], state="readonly", width=25,background=initialization.bg_color)
        member_type_combobox.set("Select Member Type")
        member_type_combobox.place(x=75, y=80)

        ticket_type_combobox = ttk.Combobox(modiPassenger_canva, values=['Economy', 'Premium', 'Business'], state="readonly", width=25,background=initialization.bg_color)
        ticket_type_combobox.set("Select ticket class")
        ticket_type_combobox.place(x=350, y=80)

        valid = tk.Button(
        modiPassenger_canva,
        text="Valid",
        background=initialization.bg_color,
        fg="white",
        font=('Helvetica', 10, 'bold'),
        command=lambda: flight.modifPassenger2(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva, tag, member_type_combobox.get(), ticket_type_combobox.get()))
        valid.place(x=275, y=110)

    # Method to display passenger information on a canvas
    def displayPassenger(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva):
        scroll_canva.delete("all")
        modiPassenger_canva.delete("all")
        for widget in modiPassenger_canva.winfo_children():
            widget.destroy()

        for i in range(int(number)):
            scroll_canva.create_text(340, (i * 150) + 20, text="Passenger " + str(i + 1) + " :", font=('Helvetica', 14, 'bold'))

            scroll_canva.create_text(150, (i * 150) + 70, text="Member type :", font=('Helvetica', 10, 'bold'))
            scroll_canva.create_text(150, (i * 150) + 90, text="Ticket class :", font=('Helvetica', 10, 'bold'))

            scroll_canva.create_text(250, (i * 150) + 70, text=f"{passagers[i]['member_type']}", font=('Helvetica', 10, 'bold'))
            scroll_canva.create_text(250, (i * 150) + 90, text=f"{passagers[i]['ticket_type']}", font=('Helvetica', 10, 'bold'))

            scroll_canva.create_image(525, (i * 150) + 75, anchor=tk.NW, image=imageModif, tags=f"modif_{i}")
            scroll_canva.tag_bind(f"modif_{i}", "<Button-1>", lambda event, tag=str(i+1): flight.modifPassenger(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva, tag))

            scroll_canva.create_rectangle(50, (i * 150), 600, (i * 150) + 110)

    # Method to select passenger details and display them
    def selectPassengerDetails(self, canvas, number, imageModif):
        scroll_canva = tk.Canvas(canvas,bg=initialization.bg_color)
        scroll_canva.config(highlightthickness=0, borderwidth=0)
        scroll_canva.place(x=825, y=220, width=650, height=550)

        yscrollbar = tk.Scrollbar(canvas, orient="vertical", command=scroll_canva.yview)
        yscrollbar.place(x=1475, y=220, width=15, height=575)

        scroll_canva.configure(yscrollcommand=yscrollbar.set)
        scroll_canva.bind('<Configure>', lambda e: scroll_canva.configure(scrollregion=scroll_canva.bbox("all")))

        display_frame = tk.Frame(scroll_canva)
        display_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        scroll_canva.create_window((0, 0), window=display_frame, anchor="nw")

        modiPassenger_canva = tk.Canvas(canvas,bg=initialization.bg_color)
        modiPassenger_canva.place(x=100, y=550, width=600, height=200)

        passagers = []

        for i in range(int(number)):
            passager_details = {"member_type": None, "ticket_type": None}
            passagers.append(passager_details)

        valid = tk.Button(
            canvas,
            text="Valid",
            bg=initialization.bg_color,
            fg="white",
            font=('Helvetica', 10, 'bold'),
            command=lambda: flight.validationPassenger(self, passagers, verify))
        valid.place(x=1135, y=785)

        verify = tk.Label(text="", font=('Helvetica', 10, 'bold'),bg=initialization.bg_color)
        verify.place(x=1185, y=787)

        flight.displayPassenger(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva)
    
    def connection(self):
        initialization.lastPage = "choice_person"
        initialization.FlightID = self.FlightID
        if initialization.login == 0:
            login.login_page()
        elif initialization.login == 1:
            customer.customer.customer_page(initialization.member)

    # Method to set up the validation page UI
    def validdation_page(self):
        canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080,bg=initialization.bg_color)
        canvas.place(x=0, y=0)
        canvas.create_line(0, 0, 1920, 0, width=150, fill="black")
        canvas.create_line(775, 220, 775, 700, width=2, fill="black")

        Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white", bg="black")
        Cuicui.place(x=50, y=15)

        Title = tk.Label(text="Validation", font=('Helvetica', 30, 'bold'),bg=initialization.bg_color)
        Title.place(x=680, y=100)

        imageCustomer = Image.open("./photos/profil_picture/photo_profil_inverse.png")
        imageCustomer = imageCustomer.resize((60, 60))
        imageCustomer = ImageTk.PhotoImage(imageCustomer)
        canvas.create_image(1420, 10, anchor=tk.NW, image=imageCustomer, tags="image")
        canvas.tag_bind("image", "<Button-1>", lambda event, tag="image": flight.connection(self))

        if initialization.lastPage == "page_accueil":
            returnTo = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'),bg=initialization.bg_color)
            returnTo.place(x=50, y=100)
            returnTo.bind("<Button-1>", lambda event=None:page_accueil.CuicuiAirlinesApp.welcome_page(initialization.cuicui))

        flight.completeFlight(self)
        flight.displayFlight(self, canvas)

        number = tk.Label(text="Select the number of passengers:", font=('Helvetica', 16, 'bold'),bg=initialization.bg_color)
        number.place(x=225, y=450)

        spinbox_frame = tk.Frame(canvas)
        spinbox_frame.place(x=310, y=500)

        spinbox = tk.Spinbox(spinbox_frame, from_=0, to=self.SeatsAvailable, increment=1, state="readonly",bg=initialization.bg_color)
        spinbox.pack(ipady=5)

        imageModif = Image.open("./photos/customer/modif.png")
        imageModif = imageModif.resize((20, 20))
        imageModif = ImageTk.PhotoImage(imageModif)

        valid = tk.Button(
            text="OK",
            bg=initialization.bg_color,
            fg="white",
            font=('Helvetica', 10, 'bold'),
            command=lambda: flight.selectPassengerDetails(self, canvas, spinbox.get(), imageModif))
        valid.place(x=450, y=500)

        initialization.cuicui.mainloop()

    # Class method to initialize and start the application with a given FlightID
    def debut(FlightID):
        Flight = flight(FlightID, 0, 0, 0, 0, 0, 0)
        flight.validdation_page(Flight)

# Entry point of the program
if __name__ == "__main__":
    # Start the application with a specific FlightID
    flight.debut(64)