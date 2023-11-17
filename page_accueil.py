import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import query
import initialization

class CuicuiAirlinesApp():
    def __init__(self, FlightID, DepartureCity, ArrivalCity, DepartureTime, ArrivalTime, TicketPrice, SeatsAvailable):
        self.FlightID = FlightID
        self.DepartureCity = DepartureCity
        self.ArrivalCity = ArrivalCity
        self.DepartureTime = DepartureTime
        self.ArrivalTime = ArrivalTime
        self.TicketPrice = TicketPrice
        self.SeatsAvailable = SeatsAvailable

    def welcome_page(self):
        initialization.cuicui.title("Welcome Page")

        canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080)
        canvas.place(x=0, y=0)
        canvas.create_line(0, 0, 1920, 0, width=150, fill="black")
        canvas.create_line(650, 220, 650, 800, width=2, fill="black")

        Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white",bg="black")
        Cuicui.place(x=50, y=15)

        titre_label = tk.Label(initialization.cuicui, text="Welcome on Cuicui Airlines", font=("Broadway", 30))
        titre_label.place(x=400, y=90)


        #DEPARTURE
        aeroport_depart_label = tk.Label( text="Departure", font=("Broadway", 10))
        aeroport_depart_label.place(x=200, y=150)
        cities = CuicuiAirlinesApp.get_cities(self)
        print("TEST 2 cities ",cities)

        aeroport_depart_combobox = ttk.Combobox( values=cities)
        aeroport_depart_combobox.place(x=300, y=150)

        #ARRIVAL
        aeroport_arrivee_label = tk.Label( text="Arrival", font=("Broadway", 10))
        aeroport_arrivee_label.place(x=450, y=150)
        aeroport_arrivee_combobox = ttk.Combobox( values=cities)
        aeroport_arrivee_combobox.place(x=550, y=150)

        #DATE
        date_label = tk.Label( text="Date", font=("Broadway", 10))
        date_label.place(x=750, y=150)
        date_select = DateEntry( date_pattern="yyyy-mm-dd", fg="black", bg="white", width=10,font=('Broadway', 10, 'bold'))
        date_select.place(x=800, y=150)

        #SEARCH
        reserver_bouton = tk.Button( text="Search", font=("Broadway", 10),command=lambda: CuicuiAirlinesApp.reserver_vol(self,aeroport_depart_combobox,aeroport_arrivee_combobox,date_select))
        reserver_bouton.place(x=950, y=150)

        initialization.cuicui.mainloop()

    def get_cities(self):
        cities=[]
        request = "SELECT DISTINCT DepartureCity FROM flight"
        citie = query.requestDataBase(request)
        for i in range(len(citie)):
            cities.append(citie[i][0])
            print("TEST cities ",cities)

        return cities

    def get_flights(self, departure_city, arrival_city, date):
        print(date[:10])
        print("We are counting the number of fly from ",departure_city," to ",arrival_city," at the date ",date)
        request = f"SELECT COUNT(*) FROM flight WHERE DepartureCity ='{departure_city}' AND ArrivalCity = '{arrival_city}' AND LEFT(DepartureTime,10) ='{date[:10]}';"
        output = query.requestDataBase(request)
        result = output[0][0]
        if(int(result) >= 1):
            print("Fly is existing")
            request = f"SELECT FlightID FROM flight WHERE DepartureCity ='{departure_city}' AND ArrivalCity = '{arrival_city}' AND LEFT(DepartureTime,10) ='{date[:10]}';"
            output = query.requestDataBase(request)
        elif (int(result) == 0):
            print("Fly is not existing at this date ")
            print("We are counting the number of fly from ", departure_city, " to ", arrival_city)
            request = f"SELECT COUNT(*) FROM flight WHERE DepartureCity ='{departure_city}' AND ArrivalCity = '{arrival_city}';"
            output = query.requestDataBase(request)
            result = output[0][0]

            if(int(result) >= 1):
                print("Fly existing")
                request = f"SELECT FlightID FROM flight WHERE DepartureCity = '{departure_city}' AND ArrivalCity = '{arrival_city}';"
                output = query.requestDataBase(request)


            elif(int(result) == 0):
                print("No fly from ",departure_city," for ", arrival_city," the ",date)
        print(" <---------- RESULT ---------->",output)

        return output

    def reserver_vol(self,aeroport_depart_combobox,aeroport_arrivee_combobox,date_select):
        id_fly=[]
        ville_depart = str(aeroport_depart_combobox.get())
        ville_arrivee = str(aeroport_arrivee_combobox.get())
        date = str(date_select.get() + " 00:00:00")

        if not ville_depart or not ville_arrivee:
            print("Veuillez remplir tous les champs.")
            return

        print("Ville de départ:", ville_depart)
        print("Ville d'arrivée:", ville_arrivee)
        print("Date sélectionnée:", date)

        # Récupérez les vols en fonction des sélections de l'utilisateur
        flights = CuicuiAirlinesApp.get_flights(self, ville_depart, ville_arrivee, date)
        print("test len fly",len(flights))


        # REMPLIR TOUT LES CHOIX DANS LA CLASSE ET LES AFFICHER

        if(flights[0][0] == 0):
            print("PAS DE VOL A CETTE DATE")

        else:
            for i in range(len(flights)):
                id_fly.append(flights[i][0])
                print("Test id_fly ", id_fly[i])
            ## PAGE DEROULANTE
            print("LISTE DES VOLS A CETTE DATE")
            CuicuiAirlinesApp.show_fly(self,id_fly)

            # METTRE AFFICHAGE VOL ICI

            # AFFICHAGE IMAGE
            self.image_display = tk.Label(initialization.cuicui)
            #self.image_display.pack()
            self.image_display.place(x=700, y=250)
            #show_image = tk.Button(initialization.cuicui,command=CuicuiAirlinesApp.show_image(self,ville_arrivee))
            CuicuiAirlinesApp.show_image(self, ville_arrivee)
            #show_image.pack()

    def show_fly(self,id_fly):
        print("FLY AVAILABLE")
        TitleRight = tk.Label(text="Fly Available", font=('Helvetica', 22, 'bold'))
        TitleRight.place(x=75, y=200)

        #pastFlights = booking(0, 0, 0, 0, 0, 0)
        #nbrBooking = booking.findNbrBooking(pastFlights, self.CustomerID)
        #if nbrBooking == 0:
        #    noBooking = tk.Label(text="No previous flights booked", font=('Helvetica', 11, 'bold'))
        #    noBooking.place(x=1010, y=350)
        if (True == 1):
            for i in range(len(id_fly)):
                print("IF TRUE",id_fly[i])
                request = f"SELECT ArrivalCity FROM flight WHERE FlightID = '{id_fly[i]} ';"
                output = query.requestDataBase(request)
                print("OUTPUT AFFICHAGE SCROLL",output)

            scroll_canva = tk.Canvas(initialization.cuicui)
            scroll_canva.config(highlightthickness=0, borderwidth=0,background="green")
            scroll_canva.place(x=75, y=275, width=500, height=525)

            yscrollbar = tk.Scrollbar(initialization.cuicui, orient="vertical", command=scroll_canva.yview)
            yscrollbar.place(x=575, y=275, width=50, height=550)

            scroll_canva.configure(yscrollcommand=yscrollbar.set)
            scroll_canva.bind('<Configure>', lambda e: scroll_canva.configure(scrollregion=scroll_canva.bbox("all")))

            display_frame = tk.Frame(scroll_canva)
            display_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

            scroll_canva.create_window((0, 0), window=display_frame, anchor="nw")



    def show_image(self,city):
        # To remove the space
        if " " in city:
            city = city.replace(" ", "_")
        city=city.lower()
        img = Image.open(f"photos/search_city/{city}.jpg")  # Assure-toi que le dossier est correctement spécifié
        #img = img.resize(500, 500)  # Redimensionnement de l'image
        photo = ImageTk.PhotoImage(img)

        self.image_display.configure(image=photo)
        self.image_display.image = photo  # Garde une référence à l'image pour l'affichage



    def affichage_vol(self, flightsNewD, flightsNewA, date):
        fly = flightsNewD + "-" + flightsNewA + "-" + date
        combobox = ttk.Combobox(initialization.cuicui, values=fly, state="readonly",width=50, height=10)
        combobox.pack(padx=10, pady=10)

    def tri_vol(self):
        count = "SELECT COUNT(*) FROM flight;"
        nbDeVol = query.requestDataBase(count)
        nbDeVol = nbDeVol[0][0]
        print(nbDeVol)
        if int(nbDeVol) > 0:
            delete = "DELETE FROM flight WHERE DepartureTime < NOW();"
            query.requestDataBase(delete)
            print("fly were delete.")
        else:
            print("RAS.")

if __name__ == "__main__":
    #app = ( )
    CuicuiAirlinesApp.welcome_page(initialization.cuicui)
    #initialization.cuicui.mainloop()
