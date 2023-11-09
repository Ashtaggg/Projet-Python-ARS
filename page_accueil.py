import pymysql
#from dbconnect import mysqlconnect  # Importez la fonction depuis dbconnect.py
import initialization
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import query
from PIL import Image, ImageTk

def get_cities():
    request = "SELECT DISTINCT DepartureCity FROM flight"
    cities = query.requestDataBase(request)

    return cities

def get_flights(ville_depart, ville_arrivee, date):
    request = "SELECT DepartureCity, ArrivalCity, DepartureTime FROM flight WHERE DepartureCity ='"+ str(ville_depart) +"'AND ArrivalCity = '" + str(ville_arrivee) + "' AND Date ='" + str(date) + "'; "

    output = query.requestDataBase(request)
    return output



def reserver_vol(aeroport_depart_combobox,aeroport_arrivee_combobox,DateEntry):


    print("Ville de départ:", aeroport_depart_combobox)
    print("Ville d'arrivée:", aeroport_arrivee_combobox)
    print("Date sélectionnée:", DateEntry)

    # Récupérez les vols en fonction des sélections de l'utilisateur
    #flights = (
    flights = get_flights(aeroport_depart_combobox, aeroport_arrivee_combobox, DateEntry)

    # Affichez les informations des vols
    for flight in flights:
        print("Vol de", flight[0], "à", flight[1], "à", flight[2])



initialization.cuicui.title("Welcome Page")
#HEADER

header_frame = tk.Frame(initialization.cuicui, highlightbackground="black", highlightthickness=5)
header_frame.pack(pady=20)

# TITLE
titre_label = tk.Label(initialization.cuicui, text="Welcome on Cuicui Airlines", font=("Broadway", 30))
titre_label.pack(pady=20)


def content():
    # CONTENT
    content_frame = tk.Frame(initialization.cuicui)
    content_frame.pack()

    # DEPARTURE
    aeroport_depart_label = tk.Label(content_frame, text="Departure", font=("Broadway", 10))
    aeroport_depart_label.grid(row=0, column=0, padx=10, pady=5)
    #aeroport_depart_combobox = ttk.Combobox(content_frame, values=["Aéroport 1", "Aéroport 2", "Aéroport 3"])
    #aeroport_depart_combobox.grid(row=0, column=1, padx=10, pady=5)
    cities = get_cities()

    aeroport_depart_combobox = ttk.Combobox(content_frame, values=cities)
    aeroport_depart_combobox.grid(row=0, column=1, padx=10, pady=5)


    # ARRIVAL
    aeroport_arrivee_label = tk.Label(content_frame, text="Arrival", font=("Broadway", 10))
    aeroport_arrivee_label.grid(row=0, column=2, padx=10, pady=5)
    #aeroport_arrivee_combobox = ttk.Combobox(content_frame, values=["Aéroport 1", "Aéroport 2", "Aéroport 3"])
    #aeroport_arrivee_combobox.grid(row=0, column=3, padx=10, pady=5)
    aeroport_arrivee_combobox = ttk.Combobox(content_frame, values=cities)
    aeroport_arrivee_combobox.grid(row=0, column=3, padx=10, pady=5)


    # DATE
    date_label = tk.Label(content_frame, text="Date", font=("Broadway", 10))
    date_label.grid(row=0, column=4, padx=10, pady=5)
    date_select = DateEntry(content_frame, date_pattern="yyyy-mm-dd", fg="black", bg="white", width=10, font = ('Broadway' , 10, 'bold'))
    date_select.grid(row=0, column=5, padx=10, pady=5)


    #FUNCTION RESERVATION
    reserver_bouton = tk.Button(content_frame, text="Search", font=("Broadway", 10) , command=lambda: reserver_vol(str(aeroport_depart_combobox.get()),str(aeroport_arrivee_combobox.get()),str(date_select.get())))
    reserver_bouton.grid(row=0, column=8, columnspan=2, pady=10)
    return 0

# Lance la boucle principale de l'application
content()
initialization.cuicui.mainloop()

