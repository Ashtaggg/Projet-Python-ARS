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

        #CuicuiAirlinesApp.tri_vol(self) #Supprime les vols déja passé

        # HEADER
        self.header_frame = tk.Frame(initialization.cuicui, highlightbackground="black", highlightthickness=5)
        self.header_frame.pack(pady=20)

        # TITLE
        self.titre_label = tk.Label(initialization.cuicui, text="Welcome on Cuicui Airlines", font=("Broadway", 30))
        self.titre_label.pack(pady=20)

        # CONTENT
        self.content_frame = tk.Frame(initialization.cuicui)
        self.content_frame.pack()

        # DEPARTURE
        self.aeroport_depart_label = tk.Label(self.content_frame, text="Departure", font=("Broadway", 10))
        self.aeroport_depart_label.grid(row=0, column=0, padx=10, pady=5)
        self.cities = CuicuiAirlinesApp.get_cities(self)
        self.aeroport_depart_combobox = ttk.Combobox(self.content_frame, values=self.cities)
        self.aeroport_depart_combobox.grid(row=0, column=1, padx=10, pady=5)

        # ARRIVAL
        self.aeroport_arrivee_label = tk.Label(self.content_frame, text="Arrival", font=("Broadway", 10))
        self.aeroport_arrivee_label.grid(row=0, column=2, padx=10, pady=5)
        self.aeroport_arrivee_combobox = ttk.Combobox(self.content_frame, values=self.cities)
        self.aeroport_arrivee_combobox.grid(row=0, column=3, padx=10, pady=5)

        # DATE
        self.date_label = tk.Label(self.content_frame, text="Date", font=("Broadway", 10))
        self.date_label.grid(row=0, column=4, padx=10, pady=5)
        self.date_select = DateEntry(self.content_frame, date_pattern="yyyy-mm-dd", fg="black", bg="white", width=10, font=('Broadway', 10, 'bold'))
        self.date_select.grid(row=0, column=5, padx=10, pady=5)

        # FUNCTION RESERVATION
        self.reserver_bouton = tk.Button(self.content_frame, text="Search", font=("Broadway", 10), command= lambda :CuicuiAirlinesApp.reserver_vol(self))
        self.reserver_bouton.grid(row=0, column=8, columnspan=2, pady=10)

        initialization.cuicui.mainloop()
    def get_cities(self):
        request = "SELECT DISTINCT DepartureCity FROM flight"
        cities = query.requestDataBase(request)
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

    def reserver_vol(self):
        ville_depart = str(self.aeroport_depart_combobox.get())
        ville_arrivee = str(self.aeroport_arrivee_combobox.get())
        date = str(self.date_select.get() + " 00:00:00")

        if not ville_depart or not ville_arrivee:
            print("Veuillez remplir tous les champs.")
            return

        print("Ville de départ:", ville_depart)
        print("Ville d'arrivée:", ville_arrivee)
        print("Date sélectionnée:", date)

        # Récupérez les vols en fonction des sélections de l'utilisateur
        flights = CuicuiAirlinesApp.get_flights(self, ville_depart, ville_arrivee, date)
        print("test",flights)
        # REMPLIR TOUT LES CHOIX DANS LA CLASSE ET LES AFFICHER

        if not flights:
            print("PAS DE VOL A CETTE DATE")

        else:
            ## PAGE DEROULANTE
            print("LISTE DES VOLS A CETTE DATE")


            # METTRE AFFICHAGE VOL ICI

            # AFFICHAGE IMAGE
            self.image_display = tk.Label(initialization.cuicui)
            self.image_display.pack()
            self.image_display.place(x=750, y=250)

            show_image_button = tk.Button(initialization.cuicui, command=CuicuiAirlinesApp.show_image(self,ville_arrivee))
            show_image_button.pack()

    def show_image(self,city):
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
