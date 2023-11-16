import tkinter as tk
import initialization
from PIL import Image, ImageTk
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


    def pastFlightsShow(self, FlightID, i):
        flight.findAllFlight(self, FlightID)


        departureCity = tk.Label(text= self.DepartureCity + "  >  " + self.ArrivalCity,font = ('Helvetica' , 15, 'bold'))
        departureCity.place(x=850, y=(i*150)+300)

        DepartureTime = tk.Label(text=self.DepartureTime,font = ('Helvetica' , 10, 'bold'))
        DepartureTime.place(x=850, y=(i*150)+340)

        DepartureCity = tk.Label(text=self.DepartureCity,font = ('Helvetica' , 10, 'bold'))
        DepartureCity.place(x=1000, y=(i*150)+340)

        ArrivalTime = tk.Label(text=self.ArrivalTime,font = ('Helvetica' , 10, 'bold'))
        ArrivalTime.place(x=850, y=(i*150)+360)

        ArrivalCity = tk.Label(text=self.ArrivalCity,font = ('Helvetica' , 10, 'bold'))
        ArrivalCity.place(x=1000, y=(i*150)+360)



        

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


    
    def pastBookingShow(self, BookingID, i, nbrBooking, canvas, image):
        booking.findAllBooking(self, BookingID)
        Flight = flight(0, 0, 0, 0, 0, 0, 0)
        flight.pastFlightsShow(Flight, self.FlightID, i)
        
        canvas.create_image(1280, (i*150)+322, anchor=tk.NW, image=image)
        
        NumberOfTickets = tk.Label(text = "x" + str(self.NumberOfTickets),font = ('Helvetica' , 10, 'bold'))
        NumberOfTickets.place(x=1300, y=(i*150)+320)

        TotalAmount = tk.Label(text = str(self.TotalAmount*self.NumberOfTickets) + " €",font = ('Helvetica' , 10, 'bold'))
        TotalAmount.place(x=1280, y=(i*150)+345)

        canvas.create_line(750, (i*150)+420, 1400, (i*150)+420, width=1, fill="black")








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
        pastFlights = booking(0, 0, 0, 0, 0, 0)
        nbrBooking = booking.findNbrBooking(pastFlights, self.CustomerID)
        request = "SELECT BookingID FROM booking WHERE CustomerID = '" + str(self.CustomerID) + "';"
        output = query.requestDataBase(request)

        for i in range(nbrBooking):
            booking.pastBookingShow(pastFlights, output[i][0], i, nbrBooking, canvas, image)


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

        image2 = Image.open("./photos/photo_profil.png")
        image2 = image2.resize((20, 20))
        image2 = ImageTk.PhotoImage(image2)

        customer.pastFlights(self, canvas, image2)


        initialization.cuicui.mainloop() 






if __name__ == "__main__":
    customer.customer_page(initialization.member)