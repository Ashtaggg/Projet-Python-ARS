import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from tkcalendar import DateEntry
import initialization
import effacer

# Fonction pour récupérer les villes depuis la base de données
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

# Fonction pour récupérer les vols en fonction des villes de départ, d'arrivée, et de la date
def get_flights(ville_depart, ville_arrivee, date):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='projet_python_ars'
    )

    try:
        with connection.cursor() as cursor:
            sql = "SELECT DepartureCity, ArrivalCity, DepartureTime FROM flight WHERE DepartureCity = %s AND ArrivalCity = %s AND Date = %s"
            cursor.execute(sql, (ville_depart, ville_arrivee, date))
            result = cursor.fetchall()

            return result

    finally:
        connection.close()

# Fonction pour afficher les détails du vol
def reserver_vol():
    ville_depart = aeroport_depart_combobox.get()
    ville_arrivee = aeroport_arrivee_combobox.get()
    selected_date = date_select.get()

    flights = get_flights(ville_depart, ville_arrivee, selected_date)

    for flight in flights:
        print("Vol de", flight[0], "à", flight[1], "à", flight[2])

# Fonction pour le processus de paiement
def process_payment():
    effacer.effacer_page()

    initialization.cuicui.title("Processus de Paiement")

    payment_label = tk.Label(initialization.cuicui, text="Veuillez saisir les informations de paiement :", font=("Broadway", 14))
    payment_label.pack()

    card_label = tk.Label(initialization.cuicui, text="Numéro de carte :", font=("Broadway", 12))
    card_entry = tk.Entry(initialization.cuicui, show="*")
    card_label.pack()
    card_entry.pack()

    expiry_label = tk.Label(initialization.cuicui, text="Date d'expiration (MM/YY) :", font=("Broadway", 12))
    expiry_entry = tk.Entry(initialization.cuicui)
    expiry_label.pack()
    expiry_entry.pack()

    cvv_label = tk.Label(initialization.cuicui, text="CVV :", font=("Broadway", 12))
    cvv_entry = tk.Entry(initialization.cuicui, show="*")
    cvv_label.pack()
    cvv_entry.pack()

    # Fonction de validation du paiement
    def validate_payment():
        card_number = card_entry.get()
        expiry_date = expiry_entry.get()
        cvv = cvv_entry.get()

        if len(card_number) == 16 and len(expiry_date) == 5 and len(cvv) == 3:
            messagebox.showinfo("Paiement réussi", "Votre paiement a été traité avec succès. Merci!")
            
        else:
            messagebox.showerror("Erreur de paiement", "Veuillez vérifier vos informations de paiement.")

    pay_button = tk.Button(initialization.cuicui, text="Payer", font=("Broadway", 14), command=validate_payment)
    pay_button.pack()

# Crée la fenêtre principale
initialization.cuicui.title("Welcome Page")

# Frame pour le header
header_frame = tk.Frame(initialization.cuicui, highlightbackground="black", highlightthickness=5)
header_frame.pack(pady=20)

# Label pour le titre
titre_label = tk.Label(initialization.cuicui, text="Welcome on Cuicui Airlines", font=("Broadway", 30))
titre_label.pack(pady=20)

# Frame pour le contenu
content_frame = tk.Frame(initialization.cuicui)
content_frame.pack()

# Label et Combobox pour la ville de départ
aeroport_depart_label = tk.Label(content_frame, text="Departure", font=("Broadway", 10))
aeroport_depart_label.grid(row=0, column=0, padx=10, pady=5)

cities = get_cities()
aeroport_depart_combobox = ttk.Combobox(content_frame, values=cities)
aeroport_depart_combobox.grid(row=0, column=1, padx=10, pady=5)

# Label et Combobox pour la ville d'arrivée
aeroport_arrivee_label = tk.Label(content_frame, text="Arrival", font=("Broadway", 10))
aeroport_arrivee_label.grid(row=0, column=2, padx=10, pady=5)

aeroport_arrivee_combobox = ttk.Combobox(content_frame, values=cities)
aeroport_arrivee_combobox.grid(row=0, column=3, padx=10, pady=5)

# Label et Entry pour la date
date_label = tk.Label(content_frame, text="Date", font=("Broadway", 10))
date_label.grid(row=0, column=4, padx=10, pady=5)

date_select = DateEntry(content_frame, date_pattern="yyyy-mm-dd", fg="black", bg="white", width=10, font=('Broadway', 10, 'bold'))
date_select.grid(row=0, column=5, padx=10, pady=5)

# Bouton pour rechercher les vols
reserver_bouton = tk.Button(content_frame, text="Search", font=("Broadway", 10), command=reserver_vol)
reserver_bouton.grid(row=0, column=8, columnspan=2, pady=10)

# Bouton pour afficher la page de paiement
show_payment_button = tk.Button(content_frame, text="Show Payment", font=("Broadway", 10), command=process_payment)
show_payment_button.grid(row=0, column=9, columnspan=2, pady=10)

# Lance la boucle principale
initialization.cuicui.mainloop()
