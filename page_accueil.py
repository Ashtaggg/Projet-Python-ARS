import pymysql
from dbconnect import mysqlconnect  # Importez la fonction depuis dbconnect.py
from dbconnect import cuicui
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry



from PIL import Image, ImageTk

def get_cities():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='projet_python_ars'
    )

    try:
        with connection.cursor() as cursor:
            sql = "SELECT DISTINCT DepartureCity FROM flight"
            cursor.execute(sql)
            result = cursor.fetchall()
            cities = [row[0] for row in result]

    finally:
        connection.close()

    return cities

def get_flights(ville_depart, ville_arrivee, date):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='projet_python_ars'
    )

    try:
        with connection.cursor() as cursor:
            # Requête SQL pour récupérer les vols en fonction des villes de départ et d'arrivée, et de la date
            sql = "SELECT DepartureCity, ArrivalCity, DepartureTime FROM flight WHERE DepartureCity = %s AND ArrivalCity = %s AND Date = %s"
            cursor.execute(sql, (ville_depart, ville_arrivee, date))
            result = cursor.fetchall()

            return result

    finally:
        connection.close()

def reserver_vol():
    ville_depart = aeroport_depart_combobox.get()
    ville_arrivee = aeroport_arrivee_combobox.get()
    selected_date = DateEntry.get()

    # Récupérez les vols en fonction des sélections de l'utilisateur
    flights = get_flights(ville_depart, ville_arrivee, selected_date)

    # Affichez les informations des vols
    for flight in flights:
        print("Vol de", flight[0], "à", flight[1], "à", flight[2])



cuicui.title("Welcome Page")
#HEADER

header_frame = tk.Frame(cuicui, highlightbackground="black", highlightthickness=5)
header_frame.pack(pady=20)

# TITLE
titre_label = tk.Label(cuicui, text="Welcome on Cuicui Airlines", font=("Broadway", 30))
titre_label.pack(pady=20)

# CONTENT
content_frame = tk.Frame(cuicui)
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

reserver_bouton = tk.Button(content_frame, text="Search", font=("Broadway", 10) , command=reserver_vol)
reserver_bouton.grid(row=0, column=8, columnspan=2, pady=10)


# Lance la boucle principale de l'application
cuicui.mainloop()

