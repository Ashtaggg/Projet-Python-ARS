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

    def get_flights(self, ville_depart, ville_arrivee, date):
        print(date[:10])
        request = f"SELECT DepartureCity, ArrivalCity, DepartureTime FROM flight WHERE DepartureCity ='{ville_depart}' AND ArrivalCity = '{ville_arrivee}' AND LEFT(DepartureTime,10) ='{date[:10]}';"
        output = query.requestDataBase(request)
        return output

    def reserver_vol(self):
        ville_depart = str(self.aeroport_depart_combobox.get())
        ville_arrivee = str(self.aeroport_arrivee_combobox.get())
        date = str(self.date_select.get() + " 00:00:00")

        print("Ville de départ:", ville_depart)
        print("Ville d'arrivée:", ville_arrivee)
        print("Date sélectionnée:", date)

        # Récupérez les vols en fonction des sélections de l'utilisateur
        flights = CuicuiAirlinesApp.get_flights(self, ville_depart, ville_arrivee, date)
        print("test",flights)
        # REMPLIR TOUT LES CHOIX DANS LA CLASSE ET LES AFFICHER

        date = flights[0][2].strftime("%Y-%m-%d_%H:%M:%S")
        flightsNewD, flightsNewA = flights[0][0], flights[0][1]
        print(flightsNewD, flightsNewA, date)

        # METTRE AFFICHAGE VOL ICI
        CuicuiAirlinesApp.affichage_vol(self, flightsNewD, flightsNewA, date)


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
            #delete = "DELETE FROM flight WHERE DepartureTime < NOW();"
            #query.requestDataBase(delete)
            print("fly were delete.")
        else:
            print("RAS.")

if __name__ == "__main__":
    #app = ( )
    CuicuiAirlinesApp.welcome_page(initialization.cuicui)
    #initialization.cuicui.mainloop()
