import pymysql
from dbconnect import mysqlconnect  # Importez la fonction depuis dbconnect.py
from dbconnect import cuicui
import tkinter as tk
#from tkinter import ttk

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='projet_python_ars',
)
cur = conn.cursor()

# Exécuter une requête SQL pour sélectionner les données de la table Flight
cur.execute("SELECT * FROM Flight")

# Récupérer toutes les lignes de résultats
rows = cur.fetchall()

# Fermer le curseur et la connexion à la base de données
cur.close()
conn.close()

flights = []
for row in rows:
    flights.append(row)

for i in flights:
    print(i)
# Liste de vols fictifs     A AFFICHER AVEC LA BDD
#flights = [{"id": 1, "departure": "New York", "arrival": "Los Angeles", "price": 300},{"id": 2, "departure": "Chicago", "arrival": "Miami", "price": 250},{"id": 3, "departure": "San Francisco", "arrival": "Las Vegas", "price": 150},]

# Fonction pour gérer la réservation
def make_reservation():
    flight_id = flight_var.get()
    departure_date = departure_date_entry.get()
    arrival_date = arrival_date_entry.get()
    # Ajoutez ici le code pour enregistrer la réservation dans la base de données ou effectuer d'autres opérations.

    # Animation : Changement de couleur et de texte
    submit_button.config(text="Réservation en cours...", state="disabled")
    submit_button.update_idletasks()
    submit_button.after(2000, lambda: reset_button())

def reset_button():
    submit_button.config(text="Réserver", state="active")
    submit_button.update_idletasks()

# Créer une fenêtre
root = tk.Tk()
root.title("Réservation de vol")

# Libellé de bienvenue
welcome_label = tk.Label(root, text="Bienvenue sur notre site de réservation de vols")
welcome_label.pack()

# Menu déroulant pour la sélection de vol
flight_var = tk.StringVar(root)
flight_var.set(flights[0]["id"])
flight_label = tk.Label(root, text="Sélectionnez un vol :")
flight_option = tk.OptionMenu(root, flight_var, *[(flight["id"], f"{flight['departure']} - {flight['arrival']}") for flight in flights])
flight_label.pack()
flight_option.pack()

# Champ de saisie pour la date de départ
departure_date_label = tk.Label(root, text="Date de départ :")
departure_date_entry = tk.Entry(root)
departure_date_label.pack()
departure_date_entry.pack()

# Champ de saisie pour la date d'arrivée
arrival_date_label = tk.Label(root, text="Date d'arrivée :")
arrival_date_entry = tk.Entry(root)
arrival_date_label.pack()
arrival_date_entry.pack()

# Bouton pour soumettre la réservation
submit_button = tk.Button(root, text="Réserver", command=make_reservation)
submit_button.pack()

# Exécutez la fenêtre
root.mainloop()