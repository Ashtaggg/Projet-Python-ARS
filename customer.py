import tkinter as tk
from tkinter import filedialog
import initialization
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import datetime
import base64
import io
import query
import statistiques
import re
import page_accueil
import choice_person


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
        scroll_canva.create_text(650, (i * 150) + 105, text=str(self.TotalAmount) + " €",
                                 font=('Helvetica', 10, 'bold'))

        scroll_canva.create_rectangle(100, (i * 150) + 10, 775, (i * 150) + 130)


class customer():
    def __init__(self, CustomerID, FirstName, LastName, Email, BirthDate, Password, Type, PhotoProfil):
        self.CustomerID = CustomerID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.BirthDate = BirthDate
        self.Password = Password
        self.Type = Type
        self.PhotoProfil = PhotoProfil

    def pastFlights(self, canvas, image):
        TitleRight = tk.Label(text="Past flights", font=('Helvetica', 20, 'bold'))
        TitleRight.place(x=1015, y=205)

        pastFlights = booking(0, 0, 0, 0, 0, 0)
        nbrBooking = booking.findNbrBooking(pastFlights, self.CustomerID)

        scroll_canva = tk.Canvas(canvas, bg=initialization.bg_color)
        scroll_canva.config(highlightthickness=0, borderwidth=0)
        scroll_canva.place(x=652, y=275, width=869, height=525)

        yscrollbar = tk.Scrollbar(canvas, orient="vertical", command=scroll_canva.yview)
        yscrollbar.place(x=1521, y=275, width=15, height=550)

        scroll_canva.configure(yscrollcommand=yscrollbar.set)
        scroll_canva.bind('<Configure>', lambda e: scroll_canva.configure(scrollregion=scroll_canva.bbox("all")))

        display_frame = tk.Frame(scroll_canva)
        display_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        scroll_canva.create_window((0, 0), window=display_frame, anchor="nw")

        if nbrBooking == 0:
            noBooking = tk.Label(scroll_canva, text="No previous flights booked", font=('Helvetica', 11, 'bold'))
            noBooking.place(x=345, y=75)
        else:
            request = "SELECT BookingID FROM booking WHERE CustomerID = '" + str(self.CustomerID) + "';"
            output = query.requestDataBase(request)

            for i in range(nbrBooking):
                booking.pastBookingShow(pastFlights, output[i][0], i, image, scroll_canva)
            
        if self.Type == 1:
            returnAdmin = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'))
            returnAdmin.place(x=700, y=200)
            returnAdmin.bind("<Button-1>", lambda event=None:customer.returnAdmin(self, canvas, image, scroll_canva, TitleRight, returnAdmin))


    def verify_submit(DepartureCity, ArrivalCity, DepartureDay, DepartureHours, DepartureMin, ArrivalDay, ArrivalHours, ArrivalMin, TicketPrice, SeatsAvailable, verify):
        DepartureTime = str(DepartureDay) + " " + str(DepartureHours) + ":" + str(DepartureMin) + ":00"
        ArrivalTime = str(ArrivalDay) + " " + str(ArrivalHours) + ":" + str(ArrivalMin) + ":00"

        date_now = datetime.now()
        date_departure = datetime.strptime(DepartureTime, "%Y-%m-%d %H:%M:%S")
        date_arrival = datetime.strptime(ArrivalTime, "%Y-%m-%d %H:%M:%S")

        if DepartureCity == "" or ArrivalCity == "" or DepartureDay == "" or DepartureHours == "" or DepartureMin == "" or ArrivalDay == "" or ArrivalHours == "" or ArrivalMin == "" or TicketPrice == "" or SeatsAvailable == "":
            verify.config(text="Please complete all the fields")
        elif DepartureCity == ArrivalCity:
            verify.config(text="You cannot have the same departure and arrival city")
        elif date_now > date_departure or date_arrival < date_departure:
            verify.config(text="Dates are not possible")
        else:
            verify.config(text="")
            request = "INSERT INTO `flight` (`DepartureCity`, `ArrivalCity`, `DepartureTime`, `ArrivalTime`, `TicketPrice`, `SeatsAvailable`) VALUES('" + str(DepartureCity) + "', '" + str(ArrivalCity) + "', '" + str(DepartureTime) + "', '" + str(ArrivalTime) + "', '" + str(TicketPrice) + "', '" + str(SeatsAvailable) + "');"
            query.requestDataBase(request)






    def createFlights(self, canvas, image):
        TitleRight = tk.Label(text="Create Flights", font=('Helvetica', 20, 'bold'))
        TitleRight.place(x=990, y=205)

        x0 = 652
        y0 = 275

        scroll_canva = tk.Canvas(canvas, bg=initialization.bg_color)
        scroll_canva.place(x=652, y=275, width=869, height=525)

        if self.Type == 1:
            returnAdmin = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'))
            returnAdmin.place(x=700, y=200)
            returnAdmin.bind("<Button-1>", lambda event=None:customer.returnAdmin(self, canvas, image, scroll_canva, TitleRight, returnAdmin))

        departureCity = tk.Label(scroll_canva, text="Departure City :", font=('Helvetica', 10, 'bold'))
        departureCity.place(x=725-x0, y=300-y0)

        DepartureCity_frame = tk.Frame(scroll_canva)
        DepartureCity_frame.place(x=725-x0, y=320-y0)

        DepartureCity = tk.Entry(DepartureCity_frame, fg="black", bg="white", width=50)
        DepartureCity.pack(ipady=5)

        arrivalCity = tk.Label(scroll_canva, text="Arrival City :", font=('Helvetica', 10, 'bold'))
        arrivalCity.place(x=1150-x0, y=300-y0)

        ArrivalCity_frame = tk.Frame(scroll_canva)
        ArrivalCity_frame.place(x=1150-x0, y=320-y0)

        ArrivalCity = tk.Entry(ArrivalCity_frame, fg="black", bg="white", width=50)
        ArrivalCity.pack(ipady=5)

        departureDay = tk.Label(scroll_canva, text="Departure Day :", font=('Helvetica', 10, 'bold'))
        departureDay.place(x=725-x0, y=370-y0)

        DepartureDay_frame = tk.Frame(scroll_canva)
        DepartureDay_frame.place(x=725-x0, y=390-y0)

        DepartureDay = DateEntry(DepartureDay_frame, date_pattern="yyyy-mm-dd", fg="black", bg="white", width=18,
                                 font=('Helvetica', 10, 'bold'))
        DepartureDay.pack(ipady=5)

        departureHours = tk.Label(scroll_canva, text="Hours :", font=('Helvetica', 10, 'bold'))
        departureHours.place(x=880-x0, y=370-y0)

        DepartureHours_frame = tk.Frame(scroll_canva)
        DepartureHours_frame.place(x=880-x0, y=390-y0)

        DepartureHours = tk.ttk.Combobox(DepartureHours_frame, width=8, values=(
        "00h", "01h", "02h", "03h", "04h", "05h", "06h", "07h", "08h", "09h", "10h", "11h", "12h", "13h", "14h", "15h",
        "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h"), state="readonly")
        DepartureHours.pack(ipady=5)

        departureMin = tk.Label(scroll_canva, text="Minutes :", font=('Helvetica', 10, 'bold'))
        departureMin.place(x=958-x0, y=370-y0)

        DepartureMin_frame = tk.Frame(scroll_canva)
        DepartureMin_frame.place(x=958-x0, y=390-y0)

        DepartureMin = tk.ttk.Combobox(DepartureMin_frame, width=8, values=(
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
        "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53",
        "54", "55", "56", "57", "58", "59"), state="readonly")
        DepartureMin.pack(ipady=5)

        arrivalDay = tk.Label(scroll_canva, text="Arrival Day :", font=('Helvetica', 10, 'bold'))
        arrivalDay.place(x=1150-x0, y=370-y0)

        ArrivalDay_frame = tk.Frame(scroll_canva)
        ArrivalDay_frame.place(x=1150-x0, y=390-y0)

        ArrivalDay = DateEntry(ArrivalDay_frame, date_pattern="yyyy-mm-dd", fg="black", bg="white", width=18,
                               font=('Helvetica', 10, 'bold'))
        ArrivalDay.pack(ipady=5)

        arrivalHours = tk.Label(scroll_canva, text="Hours :", font=('Helvetica', 10, 'bold'))
        arrivalHours.place(x=1305-x0, y=370-y0)

        ArrivalHours_frame = tk.Frame(scroll_canva)
        ArrivalHours_frame.place(x=1305-x0, y=390-y0)

        ArrivalHours = tk.ttk.Combobox(ArrivalHours_frame, width=8, values=(
        "00h", "01h", "02h", "03h", "04h", "05h", "06h", "07h", "08h", "09h", "10h", "11h", "12h", "13h", "14h", "15h",
        "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h"), state="readonly")
        ArrivalHours.pack(ipady=5)

        arrivalMin = tk.Label(scroll_canva, text="Minutes :", font=('Helvetica', 10, 'bold'))
        arrivalMin.place(x=1383-x0, y=370-y0)

        ArrivalMin_frame = tk.Frame(scroll_canva)
        ArrivalMin_frame.place(x=1383-x0, y=390-y0)

        ArrivalMin = tk.ttk.Combobox(ArrivalMin_frame, width=8, values=(
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
        "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53",
        "54", "55", "56", "57", "58", "59"), state="readonly")
        ArrivalMin.pack(ipady=5)

        ticketPrice = tk.Label(scroll_canva, text="Ticket Price :", font=('Helvetica', 10, 'bold'))
        ticketPrice.place(x=725-x0, y=450-y0)

        TicketPrice_frame = tk.Frame(scroll_canva)
        TicketPrice_frame.place(x=725-x0, y=470-y0)

        TicketPrice = tk.Entry(TicketPrice_frame, fg="black", bg="white", width=50)
        TicketPrice.pack(ipady=5)

        seatsAvailable = tk.Label(scroll_canva, text="Seats Available :", font=('Helvetica', 10, 'bold'))
        seatsAvailable.place(x=1150-x0, y=450-y0)

        SeatsAvailable_frame = tk.Frame(scroll_canva)
        SeatsAvailable_frame.place(x=1150-x0, y=470-y0)

        SeatsAvailable = tk.Entry(SeatsAvailable_frame, fg="black", bg="white", width=50)
        SeatsAvailable.pack(ipady=5)

        Submit = tk.Button(
            scroll_canva,
            text="Submit",
            bg="black",
            fg="white",
            font=('Helvetica', 10, 'bold'),
            command=lambda: customer.verify_submit(DepartureCity.get(), ArrivalCity.get(), DepartureDay.get(),
                                                   DepartureHours.get()[:2], DepartureMin.get(), ArrivalDay.get(),
                                                   ArrivalHours.get()[:2], ArrivalMin.get(), TicketPrice.get(),
                                                   SeatsAvailable.get(), verify))

        Submit.place(x=1060-x0, y=550-y0)

        verify = tk.Label(scroll_canva, text = "",font = ('Helvetica' , 10, 'bold'))
        verify.place(x=1130-x0, y=552-y0)
    


    def verify_modif(self, canvas, verify, FlightID, DepartureCity, ArrivalCity, DepartureDay, ArrivalDay, DepartureHours, ArrivalHours, TicketPrice, SeatsAvailable):
        DepartureTime = str(DepartureDay) + " " + str(DepartureHours) + ":00"
        ArrivalTime = str(ArrivalDay) + " " + str(ArrivalHours) + ":00"

        date_departure = datetime.strptime(DepartureTime, "%Y-%m-%d %H:%M:%S")
        date_arrival = datetime.strptime(ArrivalTime, "%Y-%m-%d %H:%M:%S")


        if DepartureCity == "" or ArrivalCity == "" or DepartureDay == "" or DepartureHours == "" or ArrivalDay == "" or ArrivalHours == "" or TicketPrice == "" or SeatsAvailable == "":
            verify.config(text="Please complete all the fields")
        elif DepartureCity == ArrivalCity:
            verify.config(text="You cannot have the same departure and arrival city")
        elif date_arrival < date_departure:
            verify.config(text="Dates are not possible")
        else:
            verify.config(text="")
            request = "UPDATE `flight` SET `DepartureCity` = '" + str(DepartureCity) + "', `ArrivalCity` = '" + str(ArrivalCity) + "', `DepartureTime` = '" + str(DepartureTime) + "', `ArrivalTime` = '" + str(ArrivalTime) + "', `TicketPrice` = '" + str(TicketPrice) + "', `SeatsAvailable` = '" + str(SeatsAvailable) + "' WHERE `FlightID` = '" + str(FlightID) + "';"
            query.requestDataBase(request)




    def modifFlight(self, canvas, num, scroll_canva, image, TitleRight):
        scroll_canva.delete("all")
        scroll_canva.destroy()

        request = "SELECT DepartureCity, ArrivalCity, DepartureTime, ArrivalTime, TicketPrice, SeatsAvailable FROM flight WHERE FlightID = '" + str(num) + "';"
        output = query.requestDataBase(request)

        DepartureDayDate = str(output[0][2])[:10]
        DepartureHourDate = str(output[0][2])[11:16]

        ArrivalDayDate = str(output[0][3])[:10]
        ArrivalHourDate = str(output[0][3])[11:16]



        DepartureCity = tk.Label(text = "Departure City :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        DepartureCity.place(x=800, y=300)

        departureCity_frame = tk.Frame(initialization.cuicui)
        departureCity_frame.place(x=800, y=320)

        departureCity = tk.Entry(departureCity_frame, fg="black", width=30,bg=initialization.bg_color)
        departureCity.insert(0, output[0][0])
        departureCity.pack(ipady=5)


        ArrivalCity = tk.Label(text = "Arrival City :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        ArrivalCity.place(x=1200, y=300)

        arrivalCity_frame = tk.Frame(initialization.cuicui)
        arrivalCity_frame.place(x=1200, y=320)

        arrivalCity = tk.Entry(arrivalCity_frame, fg="black", width=30,bg=initialization.bg_color)
        arrivalCity.insert(0, output[0][1])
        arrivalCity.pack(ipady=5)


        DepartureDay = tk.Label(text = "Departure Time :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        DepartureDay.place(x=800, y=400)

        departureDay_frame = tk.Frame(initialization.cuicui)
        departureDay_frame.place(x=800, y=420)

        departureDay = DateEntry(departureDay_frame, date_pattern="yyyy-mm-dd", fg="black", width=23, font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        departureDay.delete(0, tk.END)
        departureDay.insert(0, DepartureDayDate)
        departureDay.pack(ipady=5)


        ArrivalDay = tk.Label(text = "Arrival Time :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        ArrivalDay.place(x=1200, y=400)

        arrivalDay_frame = tk.Frame(initialization.cuicui)
        arrivalDay_frame.place(x=1200, y=420)

        arrivalDay = DateEntry(arrivalDay_frame, date_pattern="yyyy-mm-dd", fg="black", width=23, font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        arrivalDay.delete(0, tk.END)
        arrivalDay.insert(0, ArrivalDayDate)
        arrivalDay.pack(ipady=5)


        DepartureHour = tk.Label(text = "Departure Hour :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        DepartureHour.place(x=800, y=500)

        departureHour_frame = tk.Frame(initialization.cuicui)
        departureHour_frame.place(x=800, y=520)

        departureHour = tk.Entry(departureHour_frame, fg="black", width=30,bg=initialization.bg_color)
        departureHour.insert(0, DepartureHourDate)
        departureHour.pack(ipady=5)

        ArrivalHour = tk.Label(text = "Arival Hour :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        ArrivalHour.place(x=1200, y=500)

        arrivalHour_frame = tk.Frame(initialization.cuicui)
        arrivalHour_frame.place(x=1200, y=520)

        arrivalHour = tk.Entry(arrivalHour_frame, fg="black", width=30,bg=initialization.bg_color)
        arrivalHour.insert(0, ArrivalHourDate)
        arrivalHour.pack(ipady=5)


        TicketPrice = tk.Label(text = "Ticket Price :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        TicketPrice.place(x=800, y=600)

        ticketPrice_frame = tk.Frame(initialization.cuicui)
        ticketPrice_frame.place(x=800, y=620)

        ticketPrice = tk.Entry(ticketPrice_frame, fg="black", width=30,bg=initialization.bg_color)
        ticketPrice.insert(0, output[0][4])
        ticketPrice.pack(ipady=5)

        SeatsAvailable = tk.Label(text = "Seats Available :",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        SeatsAvailable.place(x=1200, y=600)

        seatsAvailable_frame = tk.Frame(initialization.cuicui)
        seatsAvailable_frame.place(x=1200, y=620)

        seatsAvailable = tk.Entry(seatsAvailable_frame, fg="black", width=30,bg=initialization.bg_color)
        seatsAvailable.insert(0, output[0][5])
        seatsAvailable.pack(ipady=5)

        verifyButton = tk.Button(
        initialization.cuicui,
        text  ="OK",
        bg=initialization.bg_color,
        fg = "black",
        font = ('Helvetica', 10, 'bold'),
        command = lambda: customer.verify_modif(self, canvas, verify, num, departureCity.get(), arrivalCity.get(), departureDay.get(), arrivalDay.get(), departureHour.get(), arrivalHour.get(), ticketPrice.get(), seatsAvailable.get()))
        verifyButton.place(x=1100, y=700)


        verify = tk.Label(text = "",font = ('Helvetica' , 10, 'bold'),bg=initialization.bg_color)
        verify.place(x=1140, y=702)

        



    def manageFlights(self, canvas, image):
        TitleRight = tk.Label(text = "Manage Flights",font = ('Helvetica' , 20, 'bold'),bg=initialization.bg_color)
        TitleRight.place(x=1000, y=200)

        if self.Type == 1:
            returnAdmin = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'))
            returnAdmin.place(x=700, y=200)
            returnAdmin.bind("<Button-1>", lambda event=None:customer.returnAdmin(self, canvas, image, scroll_canva, TitleRight, returnAdmin))

        request = "SELECT FlightID FROM flight WHERE DepartureTime > NOW();"
        output = query.requestDataBase(request)
        
        id_fly = output

        scroll_canva = tk.Canvas(canvas, bg=initialization.bg_color)
        scroll_canva.config(highlightthickness=0, borderwidth=0)
        scroll_canva.place(x=652, y=275, width=869, height=525)

        yscrollbar = tk.Scrollbar(canvas, orient="vertical", command=scroll_canva.yview)
        yscrollbar.place(x=1521, y=275, width=15, height=550)

        scroll_canva.configure(yscrollcommand=yscrollbar.set)
        scroll_canva.bind('<Configure>', lambda e: scroll_canva.configure(scrollregion=scroll_canva.bbox("all")))

        display_frame = tk.Frame(scroll_canva)
        display_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        scroll_canva.create_window((0, 0), window=display_frame, anchor="nw")

        boutons=[]

        for i in range(len(id_fly)):
            request = f"SELECT DepartureCity, ArrivalCity, DepartureTime, ArrivalTime, TicketPrice, SeatsAvailable FROM flight WHERE FlightID = '{id_fly[i][0]} ';"
            output = query.requestDataBase(request)

            fly = [str(output[0][0]),str(output[0][1]),str(output[0][2]),str(output[0][3]),str(output[0][4]),output[0][5]]

            scroll_canva.create_text(240, (i * 150) + 40, text=fly[0] + "  >  " + fly[1], font=('Helvetica', 14, 'bold'))
            scroll_canva.create_text(325, (i * 150) + 80, text=str(fly[2])[:16], font=('Helvetica', 10, 'bold'))
            scroll_canva.create_text(450, (i * 150) + 80, text=fly[0], font=('Helvetica', 10, 'bold'))
            scroll_canva.create_text(325, (i * 150) + 100, text=str(fly[3])[:16], font=('Helvetica', 10, 'bold'))
            scroll_canva.create_text(450, (i * 150) + 100, text=fly[1], font=('Helvetica', 10, 'bold'))
            scroll_canva.create_rectangle(105, (i * 150) + 10, 795, (i * 150) + 130)


            bouton = tk.Button(canvas, text=f"Manage", command=lambda num=id_fly[i][0]: customer.modifFlight(self, canvas ,num, scroll_canva, image, TitleRight),bg=initialization.bg_color)
            bouton.pack(padx=20,pady=20)
            scroll_canva.create_window(650, (i * 150) + 100, window=bouton)  # Position du bouton dans le canevas

            boutons.append(bouton)




    
    def returnAdmin(self, canvas, image2, scroll_canva, TitleRight, returnAdmin):
        scroll_canva.delete("all")
        scroll_canva.destroy()
        
        TitleRight.destroy()
        returnAdmin.destroy()

        customer.adminOrNot(self, canvas, image2)



    def adminTools(self, canvas, image2, bouton, bouton_canva):
        bouton_canva.delete("all")
        bouton_canva.destroy()
        if bouton == 1:
            customer.pastFlights(self, canvas, image2)
        elif bouton == 2:
            customer.createFlights(self, canvas, image2)
        elif bouton == 3:
            customer.manageFlights(self, canvas, image2)
        elif bouton == 4:
            statistiques.stat_page(self)


    def adminOrNot(self, canvas, image2):
        request = "SELECT Type FROM Customer WHERE CustomerID = '" + str(self.CustomerID) + "';"
        output = query.requestDataBase(request)
        if output[0][0] == 0:
            customer.pastFlights(self, canvas, image2)
        elif output[0][0] == 1:
            
            bouton_canva = tk.Canvas(canvas, bg=initialization.bg_color, borderwidth=0)
            bouton_canva.place(x=652, y=200, width=869, height=525)

            bouton_canva.create_text(440, 25, text="Admin Tools ", font=('Helvetica', 20, 'bold'))

            PastFlight = tk.Button(
            bouton_canva,
            text="Past Flight",
            bg="black",
            fg="white",
            font=('Helvetica', 10, 'bold'),
            command=lambda: customer.adminTools(self, canvas, image2, 1, bouton_canva))
            PastFlight.place(x=395, y=150)

            CreateFlight = tk.Button(
            bouton_canva,
            text="Create Flight",
            bg="black",
            fg="white",
            font=('Helvetica', 10, 'bold'),
            command=lambda: customer.adminTools(self, canvas, image2, 2, bouton_canva))
            CreateFlight.place(x=389, y=200)

            ManageFlight = tk.Button(
            bouton_canva,
            text="Manage Flight",
            bg="black",
            fg="white",
            font=('Helvetica', 10, 'bold'),
            command=lambda: customer.adminTools(self, canvas, image2, 3, bouton_canva))
            ManageFlight.place(x=385, y=250)

            Statistiques = tk.Button(
            bouton_canva,
            text="Statistiques",
            bg="black",
            fg="white",
            font=('Helvetica', 10, 'bold'),
            command=lambda: customer.adminTools(self, canvas, image2, 4, bouton_canva))
            Statistiques.place(x=393, y=300)



    def changeModif(self, tag, new):
        if tag == "FirstName":
            request = "UPDATE `customer` SET `FirstName` = '" + str(new) + "' WHERE `CustomerID` = '" + str(self.CustomerID) + "';"
        elif tag == "Name":
            request = "UPDATE `customer` SET `LastName` = '" + str(new) + "' WHERE `CustomerID` = '" + str(self.CustomerID) + "';"
        elif tag == "Email":
            request = "UPDATE `customer` SET `Email` = '" + str(new) + "' WHERE `CustomerID` = '" + str(self.CustomerID) + "';"
        elif tag == "Birth":
            request = "UPDATE `customer` SET `BirthDate` = '" + str(new) + "' WHERE `CustomerID` = '" + str(self.CustomerID) + "';"
        output = query.requestDataBase(request)


        if tag == "FirstName":
            request = "SELECT FirstName FROM customer WHERE CustomerID = '" + str(self.CustomerID) + "';"
            output = query.requestDataBase(request)
            self.FirstName = output[0][0]
        elif tag == "Name":
            request = "SELECT LastName FROM customer WHERE CustomerID = '" + str(self.CustomerID) + "';"
            output = query.requestDataBase(request)
            self.LastName = output[0][0]
        elif tag == "Email":
            request = "SELECT Email FROM customer WHERE CustomerID = '" + str(self.CustomerID) + "';"
            output = query.requestDataBase(request)
            self.Email = output[0][0]
        elif tag == "Birth":
            request = "SELECT BirthDate FROM customer WHERE CustomerID = '" + str(self.CustomerID) + "';"
            output = query.requestDataBase(request)
            self.BirthDate = output[0][0]


        for widget in initialization.cuicui.winfo_children():
            widget.destroy()
        customer.customer_page(self)


    def modifProfil(self, tag):
        y0 = 125
        modif = tk.Frame(initialization.cuicui)
        valid = tk.Button(
        text = "OK",
        bg = "black",
        fg = "white",
        font = ('Helvetica' , 10, 'bold'),
        command = lambda: customer.changeModif(self, tag, modif.get()))
        
        if tag == "FirstName":
            modif.place(x=170, y=y0 + 410)
            valid.place(x=390, y=y0 + 410)
            modif = tk.Entry(modif, fg="black", bg="white", width=35)
        elif tag == "Name":
            modif.place(x=170, y=y0 + 450)
            valid.place(x=390, y=y0 + 450)
            modif = tk.Entry(modif, fg="black", bg="white", width=35)
        elif tag == "Birth":
            modif.place(x=170, y=y0 + 488)
            valid.place(x=390, y=y0 + 490)
            modif = DateEntry(modif, date_pattern="yyyy-mm-dd", fg="black", bg="white", width=27, font = ('Helvetica' , 10, 'bold'), dayfield=('entry', 1))
        elif tag == "Email":
            modif.place(x=170, y=y0 + 530)
            valid.place(x=390, y=y0 + 530)
            modif = tk.Entry(modif, fg="black", bg="white", width=35)

        modif.pack(ipady=5)


    def modifPhoto(self, tag):
        fichier = filedialog.askopenfilename(title="Choisir un fichier")
        if fichier:
            pattern = re.compile("/photos/(.+)")
            fichier = pattern.search(fichier)
            fichier = fichier.group(0)
            fichier = "." + str(fichier)

            image = Image.open(fichier)
            image = image.resize((200, 200))
            with open(fichier, "rb") as image_file:
                image_data = image_file.read()
            PhotoProfil = base64.b64encode(image_data).decode('utf-8')

            request = "UPDATE `customer` SET `PhotoProfil` = '" + str(PhotoProfil) + "' WHERE `CustomerID` = '" + str(self.CustomerID) + "';"
            output = query.requestDataBase(request)

            request = "SELECT PhotoProfil FROM customer WHERE CustomerID = '" + str(self.CustomerID) + "';"
            output = query.requestDataBase(request)
            self.PhotoProfil = output[0][0]


            for widget in initialization.cuicui.winfo_children():
                widget.destroy()
            customer.customer_page(self)

    def logout(self):
        initialization.login = 0
        page_accueil.CuicuiAirlinesApp.welcome_page(initialization.cuicui)

    def customer_page(self):
        y0 = 125

        canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080, bg=initialization.bg_color)
        canvas.place(x=0, y=0)
        canvas.create_line(0, 0, 1920, 0, width=150, fill="black")
        canvas.create_line(650, 220, 650, 700, width=2, fill="black")

        Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white",
                          bg="black")
        Cuicui.place(x=50, y=15)

        image = base64.b64decode(self.PhotoProfil)
        image = io.BytesIO(image)
        image = Image.open(image)
        image = image.resize((200, 200))
        image = ImageTk.PhotoImage(image)
        canvas.create_image(170, 200, anchor=tk.NW, image=image, tags="image")
        canvas.tag_bind("image", "<Button-1>", lambda event, tag="image": customer.modifPhoto(self, tag))


        Title = tk.Label(text="Account", font=('Helvetica', 30, 'bold'))
        Title.place(x=700, y=y0 - 25)

        if initialization.lastPage == "page_accueil":
            returnTo = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'))
            returnTo.place(x=50, y=100)
            returnTo.bind("<Button-1>", lambda event=None:page_accueil.CuicuiAirlinesApp.welcome_page(initialization.cuicui))
        elif initialization.lastPage == "choice_person":
            returnTo = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'))
            returnTo.place(x=50, y=100)
            returnTo.bind("<Button-1>", lambda event=None:choice_person.flight.debut(initialization.FlightID))

        TitleLeft = tk.Label(text="General informations", font=('Helvetica', 20, 'bold'))
        TitleLeft.place(x=170, y=y0 + 320)

        firstname = tk.Label(text=self.FirstName, font=('Helvetica', 12, 'bold'))
        firstname.place(x=170, y=y0 + 410)

        imageModifFirstName = Image.open("./photos/customer/modif.png")
        imageModifFirstName = imageModifFirstName.resize((16, 16))
        imageModifFirstName = ImageTk.PhotoImage(imageModifFirstName)
        canvas.create_image(500, y0 + 413, anchor=tk.NW, image=imageModifFirstName, tags="imageModifFirstName")
        canvas.tag_bind("imageModifFirstName", "<Button-1>", lambda event, tag="FirstName": customer.modifProfil(self, tag))

        name = tk.Label(text=self.LastName, font=('Helvetica', 12, 'bold'))
        name.place(x=170, y=y0 + 450)

        imageModifName = Image.open("./photos/customer/modif.png")
        imageModifName = imageModifName.resize((16, 16))
        imageModifName = ImageTk.PhotoImage(imageModifName)
        canvas.create_image(500, y0 + 453, anchor=tk.NW, image=imageModifName, tags="imageModifName")
        canvas.tag_bind("imageModifName", "<Button-1>", lambda event, tag="Name": customer.modifProfil(self, tag))

        BirthDate = tk.Label(text="Date of birth :", font=('Helvetica', 10, 'bold'))
        BirthDate.place(x=170, y=y0 + 491)

        birthDate = tk.Label(text=self.BirthDate, font=('Helvetica', 12, 'bold'))
        birthDate.place(x=265, y=y0 + 490)
    
        imageModifBirth = Image.open("./photos/customer/modif.png")
        imageModifBirth = imageModifBirth.resize((16, 16))
        imageModifBirth = ImageTk.PhotoImage(imageModifBirth)
        canvas.create_image(500, y0 + 493, anchor=tk.NW, image=imageModifBirth, tags="imageModifBirth")
        canvas.tag_bind("imageModifBirth", "<Button-1>", lambda event, tag="Birth": customer.modifProfil(self, tag))

        email = tk.Label(text=self.Email, font=('Helvetica', 12, 'bold'))
        email.place(x=170, y=y0 + 530)

        imageModifEmail = Image.open("./photos/customer/modif.png")
        imageModifEmail = imageModifEmail.resize((16, 16))
        imageModifEmail = ImageTk.PhotoImage(imageModifEmail)
        canvas.create_image(500, y0 + 533, anchor=tk.NW, image=imageModifEmail, tags="imageModifEmail")
        canvas.tag_bind("imageModifEmail", "<Button-1>", lambda event, tag="Email": customer.modifProfil(self, tag))


        image2 = Image.open("./photos/profil_picture/photo_profil.png")
        image2 = image2.resize((20, 20))
        image2 = ImageTk.PhotoImage(image2)

        logout = tk.Button(
        initialization.cuicui,
        text  ="Log Out",
        bg="black",
        fg = "white",
        font = ('Helvetica', 10, 'bold'),
        command = lambda: customer.logout(self))
        logout.place(x=170, y=750)

        customer.adminOrNot(self, canvas, image2)

        initialization.cuicui.mainloop()


if __name__ == "__main__":
    customer.customer_page(initialization.member)