import tkinter as tk
import initialization
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import simpledialog
import query


class flight():
    def __init__(self, FlightID, DepartureCity, ArrivalCity, DepartureTime, ArrivalTime, TicketPrice, SeatsAvailable):
        self.FlightID = FlightID
        self.DepartureCity = DepartureCity
        self.ArrivalCity = ArrivalCity
        self.DepartureTime = DepartureTime
        self.ArrivalTime = ArrivalTime
        self.TicketPrice = TicketPrice
        self.SeatsAvailable = SeatsAvailable

    def findAllFlight(self, FlightID):
        self.FlightID = FlightID

        request = "SELECT DepartureCity FROM flight WHERE FlightID = '" + str(FlightID) + "';"
        output = query.requestDataBase(request)
        self.DepartureCity = output[0][0]

        request = "SELECT ArrivalCity FROM flight WHERE FlightID = '" + str(FlightID) + "';"
        output = query.requestDataBase(request)
        self.ArrivalCity = output[0][0]

        request = "SELECT DepartureTime FROM flight WHERE FlightID = '" + str(FlightID) + "';"
        output = query.requestDataBase(request)
        self.DepartureTime = output[0][0]

        request = "SELECT ArrivalTime FROM flight WHERE FlightID = '" + str(FlightID) + "';"
        output = query.requestDataBase(request)
        self.ArrivalTime = output[0][0]

    def pastFlightsShow(self, FlightID, i, scroll_canva):
        flight.findAllFlight(self, FlightID)

        scroll_canva.create_text(250, (i * 150) + 40, text=self.DepartureCity + "  >  " + self.ArrivalCity,
                                 font=('Helvetica', 14, 'bold'))

        scroll_canva.create_text(275, (i * 150) + 80, text=str(self.DepartureTime)[:16], font=('Helvetica', 10, 'bold'))

        scroll_canva.create_text(400, (i * 150) + 80, text=self.DepartureCity, font=('Helvetica', 10, 'bold'))

        scroll_canva.create_text(275, (i * 150) + 100, text=str(self.ArrivalTime)[:16], font=('Helvetica', 10, 'bold'))

        scroll_canva.create_text(400, (i * 150) + 100, text=self.ArrivalCity, font=('Helvetica', 10, 'bold'))


class booking():
    def __init__(self, BookingID, CustomerID, FlightID, NumberOfTickets, TotalAmount, Timestamp):
        self.BookingID = BookingID
        self.CustomerID = CustomerID
        self.FlightID = FlightID
        self.NumberOfTickets = NumberOfTickets
        self.TotalAmount = TotalAmount
        self.Timestamp = Timestamp

    def findNbrBooking(self, CustomerID):
        request = "SELECT COUNT(*) FROM booking WHERE CustomerID = '" + str(CustomerID) + "';"
        output = query.requestDataBase(request)
        nbrBooking = output[0][0]
        if nbrBooking == 0:
            return nbrBooking
        elif nbrBooking != 0:
            return nbrBooking

    def findAllBooking(self, BookingID):
        request = "SELECT FlightID FROM booking WHERE BookingID = '" + str(BookingID) + "';"
        output = query.requestDataBase(request)
        self.FlightID = output[0][0]

        request = "SELECT NumberOfTickets FROM booking WHERE BookingID = '" + str(BookingID) + "';"
        output = query.requestDataBase(request)
        self.NumberOfTickets = output[0][0]

        request = "SELECT TotalAmount FROM booking WHERE BookingID = '" + str(BookingID) + "';"
        output = query.requestDataBase(request)
        self.TotalAmount = output[0][0]

        request = "SELECT Timestamp FROM booking WHERE BookingID = '" + str(BookingID) + "';"
        output = query.requestDataBase(request)
        self.Timestamp = output[0][0]

    def pastBookingShow(self, BookingID, i, image, scroll_canva):
        booking.findAllBooking(self, BookingID)
        Flight = flight(0, 0, 0, 0, 0, 0, 0)
        flight.pastFlightsShow(Flight, self.FlightID, i, scroll_canva)

        scroll_canva.create_image(625, (i * 150) + 62, anchor=tk.NW, image=image)

        scroll_canva.create_text(655, (i * 150) + 75, text="x" + str(self.NumberOfTickets),
                                 font=('Helvetica', 10, 'bold'))
        scroll_canva.create_text(650, (i * 150) + 105, text=str(self.TotalAmount * self.NumberOfTickets) + " €",
                                 font=('Helvetica', 10, 'bold'))

        if i != 0:
            scroll_canva.create_line(75, (i * 150) + 0, 800, (i * 150) + 0, width=1, fill="black")


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

    def pastFlights(self, canvas, image):
        TitleRight = tk.Label(text="Past flights", font=('Helvetica', 22, 'bold'))
        TitleRight.place(x=1030, y=200)

        pastFlights = booking(0, 0, 0, 0, 0, 0)
        nbrBooking = booking.findNbrBooking(pastFlights, self.CustomerID)
        if nbrBooking == 0:
            noBooking = tk.Label(text="No previous flights booked", font=('Helvetica', 11, 'bold'))
            noBooking.place(x=1010, y=350)
        else:
            request = "SELECT BookingID FROM booking WHERE CustomerID = '" + str(self.CustomerID) + "';"
            output = query.requestDataBase(request)

            scroll_canva = tk.Canvas(canvas)
            scroll_canva.config(highlightthickness=0, borderwidth=0)
            scroll_canva.place(x=652, y=275, width=869, height=525)

            yscrollbar = tk.Scrollbar(canvas, orient="vertical", command=scroll_canva.yview)
            yscrollbar.place(x=1521, y=275, width=15, height=550)

            scroll_canva.configure(yscrollcommand=yscrollbar.set)
            scroll_canva.bind('<Configure>', lambda e: scroll_canva.configure(scrollregion=scroll_canva.bbox("all")))

            display_frame = tk.Frame(scroll_canva)
            display_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

            scroll_canva.create_window((0, 0), window=display_frame, anchor="nw")

            for i in range(nbrBooking):
                booking.pastBookingShow(pastFlights, output[i][0], i, image, scroll_canva)

    def verify_submit(DepartureCity, ArrivalCity, DepartureDay, DepartureHours, DepartureMin, ArrivalDay, ArrivalHours,
                      ArrivalMin, TicketPrice, SeatsAvailable):
        DepartureTime = str(DepartureDay) + " " + str(DepartureHours) + ":" + str(DepartureMin) + ":00"
        ArrivalTime = str(ArrivalDay) + " " + str(ArrivalHours) + ":" + str(ArrivalMin) + ":00"
        print("Départ", DepartureTime, "Arrival", ArrivalTime)

    def createFlights(self):
        TitleRight = tk.Label(text="Create Flights", font=('Helvetica', 20, 'bold'))
        TitleRight.place(x=985, y=225)

        departureCity = tk.Label(text="Departure City :", font=('Helvetica', 10, 'bold'))
        departureCity.place(x=725, y=300)

        DepartureCity_frame = tk.Frame(initialization.cuicui)
        DepartureCity_frame.place(x=725, y=320)

        DepartureCity = tk.Entry(DepartureCity_frame, fg="black", bg="white", width=50)
        DepartureCity.pack(ipady=5)

        arrivalCity = tk.Label(text="Arrival City :", font=('Helvetica', 10, 'bold'))
        arrivalCity.place(x=1150, y=300)

        ArrivalCity_frame = tk.Frame(initialization.cuicui)
        ArrivalCity_frame.place(x=1150, y=320)

        ArrivalCity = tk.Entry(ArrivalCity_frame, fg="black", bg="white", width=50)
        ArrivalCity.pack(ipady=5)

        departureDay = tk.Label(text="Departure Day :", font=('Helvetica', 10, 'bold'))
        departureDay.place(x=725, y=370)

        DepartureDay_frame = tk.Frame(initialization.cuicui)
        DepartureDay_frame.place(x=725, y=390)

        DepartureDay = DateEntry(DepartureDay_frame, date_pattern="yyyy-mm-dd", fg="black", bg="white", width=18,
                                 font=('Helvetica', 10, 'bold'))
        DepartureDay.pack(ipady=5)

        departureHours = tk.Label(text="Hours :", font=('Helvetica', 10, 'bold'))
        departureHours.place(x=880, y=370)

        DepartureHours_frame = tk.Frame(initialization.cuicui)
        DepartureHours_frame.place(x=880, y=390)

        DepartureHours = tk.ttk.Combobox(DepartureHours_frame, width=8, values=(
        "00h", "01h", "02h", "03h", "04h", "05h", "06h", "07h", "08h", "09h", "10h", "11h", "12h", "13h", "14h", "15h",
        "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h"))
        DepartureHours.pack(ipady=5)

        departureMin = tk.Label(text="Minutes :", font=('Helvetica', 10, 'bold'))
        departureMin.place(x=958, y=370)

        DepartureMin_frame = tk.Frame(initialization.cuicui)
        DepartureMin_frame.place(x=958, y=390)

        DepartureMin = tk.ttk.Combobox(DepartureMin_frame, width=8, values=(
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
        "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53",
        "54", "55", "56", "57", "58", "59"))
        DepartureMin.pack(ipady=5)

        arrivalDay = tk.Label(text="Arrival Day :", font=('Helvetica', 10, 'bold'))
        arrivalDay.place(x=1150, y=370)

        ArrivalDay_frame = tk.Frame(initialization.cuicui)
        ArrivalDay_frame.place(x=1150, y=390)

        ArrivalDay = DateEntry(ArrivalDay_frame, date_pattern="yyyy-mm-dd", fg="black", bg="white", width=18,
                               font=('Helvetica', 10, 'bold'))
        ArrivalDay.pack(ipady=5)

        arrivalHours = tk.Label(text="Hours :", font=('Helvetica', 10, 'bold'))
        arrivalHours.place(x=1305, y=370)

        ArrivalHours_frame = tk.Frame(initialization.cuicui)
        ArrivalHours_frame.place(x=1305, y=390)

        ArrivalHours = tk.ttk.Combobox(ArrivalHours_frame, width=8, values=(
        "00h", "01h", "02h", "03h", "04h", "05h", "06h", "07h", "08h", "09h", "10h", "11h", "12h", "13h", "14h", "15h",
        "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h"))
        ArrivalHours.pack(ipady=5)

        arrivalMin = tk.Label(text="Minutes :", font=('Helvetica', 10, 'bold'))
        arrivalMin.place(x=1383, y=370)

        ArrivalMin_frame = tk.Frame(initialization.cuicui)
        ArrivalMin_frame.place(x=1383, y=390)

        ArrivalMin = tk.ttk.Combobox(ArrivalMin_frame, width=8, values=(
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
        "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53",
        "54", "55", "56", "57", "58", "59"))
        ArrivalMin.pack(ipady=5)

        ticketPrice = tk.Label(text="Ticket Price :", font=('Helvetica', 10, 'bold'))
        ticketPrice.place(x=725, y=450)

        TicketPrice_frame = tk.Frame(initialization.cuicui)
        TicketPrice_frame.place(x=725, y=470)

        TicketPrice = tk.Entry(TicketPrice_frame, fg="black", bg="white", width=50)
        TicketPrice.pack(ipady=5)

        seatsAvailable = tk.Label(text="Seats Available :", font=('Helvetica', 10, 'bold'))
        seatsAvailable.place(x=1150, y=450)

        SeatsAvailable_frame = tk.Frame(initialization.cuicui)
        SeatsAvailable_frame.place(x=1150, y=470)

        SeatsAvailable = tk.Entry(SeatsAvailable_frame, fg="black", bg="white", width=50)
        SeatsAvailable.pack(ipady=5)

        Submit = tk.Button(
            initialization.cuicui,
            text="Sign up",
            bg="black",
            fg="white",
            font=('Helvetica', 10, 'bold'),
            command=lambda: customer.verify_submit(DepartureCity.get(), ArrivalCity.get(), DepartureDay.get(),
                                                   DepartureHours.get()[:2], DepartureMin.get(), ArrivalDay.get(),
                                                   ArrivalHours.get()[:2], ArrivalMin.get(), TicketPrice.get(),
                                                   SeatsAvailable.get()))

        Submit.place(x=1100, y=550)

    def adminOrNot(self, canvas, image2):
        request = "SELECT Type FROM Customer WHERE CustomerID = '" + str(self.CustomerID) + "';"
        output = query.requestDataBase(request)
        if output[0][0] == 0:
            customer.pastFlights(self, canvas, image2)
        elif output[0][0] == 1:
            customer.createFlights(self)

    def customer_page(self):
        y0 = 125

        canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080)
        canvas.place(x=0, y=0)
        canvas.create_line(0, 0, 1920, 0, width=150, fill="black")
        canvas.create_line(650, 220, 650, 700, width=2, fill="black")

        Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white",
                          bg="black")
        Cuicui.place(x=50, y=15)

        image = Image.open("./photos/photo_profil.png")
        image = image.resize((200, 200))
        image = ImageTk.PhotoImage(image)
        canvas.create_image(170, 200, anchor=tk.NW, image=image)

        Title = tk.Label(text="Account", font=('Helvetica', 30, 'bold'))
        Title.place(x=700, y=y0 - 25)

        TitleLeft = tk.Label(text="General informations", font=('Helvetica', 20, 'bold'))
        TitleLeft.place(x=170, y=y0 + 320)

        firstname = tk.Label(text=self.FirstName, font=('Helvetica', 12, 'bold'))
        firstname.place(x=170, y=y0 + 410)

        name = tk.Label(text=self.LastName, font=('Helvetica', 12, 'bold'))
        name.place(x=170, y=y0 + 450)

        email = tk.Label(text=self.Email, font=('Helvetica', 12, 'bold'))
        email.place(x=170, y=y0 + 490)

        BirthDate = tk.Label(text="Date of birth :", font=('Helvetica', 10, 'bold'))
        BirthDate.place(x=170, y=y0 + 532)

        birthDate = tk.Label(text=self.BirthDate, font=('Helvetica', 12, 'bold'))
        birthDate.place(x=265, y=y0 + 530)

        image2 = Image.open("./photos/photo_profil.png")
        image2 = image2.resize((20, 20))
        image2 = ImageTk.PhotoImage(image2)

        customer.adminOrNot(self, canvas, image2)

        initialization.cuicui.mainloop()


if __name__ == "__main__":
    customer.customer_page(initialization.member)