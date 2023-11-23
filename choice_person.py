import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import initialization
import query
import pay


class flight():
    def __init__(self, FlightID, DepartureCity, ArrivalCity, DepartureTime, ArrivalTime, TicketPrice, SeatsAvailable):
        self.FlightID = FlightID
        self.DepartureCity = DepartureCity
        self.ArrivalCity = ArrivalCity
        self.DepartureTime = DepartureTime
        self.ArrivalTime = ArrivalTime
        self.TicketPrice = TicketPrice
        self.SeatsAvailable = SeatsAvailable

    def completeFlight(self):

        request = "SELECT DepartureCity FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.DepartureCity = output[0][0]

        request = "SELECT ArrivalCity FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.ArrivalCity = output[0][0]

        request = "SELECT DepartureTime FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.DepartureTime = output[0][0]

        request = "SELECT ArrivalTime FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.ArrivalTime = output[0][0]

        request = "SELECT TicketPrice FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.TicketPrice = output[0][0]

        request = "SELECT SeatsAvailable FROM flight WHERE FlightID = '" + str(self.FlightID) + "';"
        output = query.requestDataBase(request)
        self.SeatsAvailable = output[0][0]

    
    def displayFlight(self, canvas):
        y0 = 75

        canvas.create_text(250, y0 + 190, text=self.DepartureCity + "  >  " + self.ArrivalCity, font=('Helvetica', 14, 'bold'))
        canvas.create_text(275, y0 + 230, text=str(self.DepartureTime)[:16], font=('Helvetica', 10, 'bold'))
        canvas.create_text(400, y0 + 230, text=self.DepartureCity, font=('Helvetica', 10, 'bold'))
        canvas.create_text(275, y0 + 250, text=str(self.ArrivalTime)[:16], font=('Helvetica', 10, 'bold'))
        canvas.create_text(400, y0 + 250, text=self.ArrivalCity, font=('Helvetica', 10, 'bold'))

        canvas.create_text(650, y0 + 255, text=str(self.SeatsAvailable) + " €", font=('Helvetica', 10, 'bold'))

        canvas.create_rectangle(100, y0 + 160, 700, y0 + 280)



    def validationPassenger(self, passagers, verify):
        fieldsCompleted = all(passager['member_type'] is not None and passager['ticket_type'] is not None for passager in passagers)
        if fieldsCompleted:
            fieldsSelected = all( passager['member_type'] != "Select Member Type" and passager['ticket_type'] != "Select ticket class" for passager in passagers)
            if fieldsSelected:
                print("tout est ok, on peut aller sur la page de paiment")
                #On appel le pay.py
                #Avec dedans à gauche, le recap de Anthonyavec toutes les infos
                #Et à droite, les informations de paiment
            else:
                verify.config(text="Please complete all the fields")
        else:
            verify.config(text="Please complete all the fields")




    def modifPassenger2(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva, tag, member_type, ticket_type):
        passagers[int(tag)-1]['member_type'] = member_type
        passagers[int(tag)-1]['ticket_type'] = ticket_type

        flight.displayPassenger(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva)



    def modifPassenger(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva, tag):
        modiPassenger_canva.create_text(300, 50, text="Passenger " + str(tag) + " :", font=('Helvetica', 14, 'bold'))

        member_type_combobox = ttk.Combobox(modiPassenger_canva, values=['Senior', 'Regular', 'Children'], state="readonly", width=25)
        member_type_combobox.set("Select Member Type")
        member_type_combobox.place(x=75, y=80)

        ticket_type_combobox = ttk.Combobox(modiPassenger_canva, values=['Economy', 'Premium', 'Business'], state="readonly", width=25)
        ticket_type_combobox.set("Select ticket class")
        ticket_type_combobox.place(x=350, y=80)

        


        valid = tk.Button(
        modiPassenger_canva,
        text = "Valid",
        bg = "black",
        fg = "white",
        font = ('Helvetica' , 10, 'bold'),
        command = lambda: flight.modifPassenger2(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva, tag, member_type_combobox.get(), ticket_type_combobox.get()))
        valid.place(x = 275, y = 110)



    def displayPassenger(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva):
        scroll_canva.delete("all")
        modiPassenger_canva.delete("all")
        for widget in modiPassenger_canva.winfo_children():
            widget.destroy()

        for i in range (int(number)):
            scroll_canva.create_text(340, (i * 150) + 20, text="Passenger " + str(i + 1) + " :", font=('Helvetica', 14, 'bold'))

            scroll_canva.create_text(150, (i * 150) + 70, text="Member type :", font=('Helvetica', 10, 'bold'))
            scroll_canva.create_text(150, (i * 150) + 90, text="Ticket class :", font=('Helvetica', 10, 'bold'))

            scroll_canva.create_text(250, (i * 150) + 70, text=f"{passagers[i]['member_type']}", font=('Helvetica', 10, 'bold'))
            scroll_canva.create_text(250, (i * 150) + 90, text=f"{passagers[i]['ticket_type']}", font=('Helvetica', 10, 'bold'))


            scroll_canva.create_image(525, (i * 150) + 75, anchor=tk.NW, image=imageModif, tags=f"modif_{i}")
            scroll_canva.tag_bind(f"modif_{i}", "<Button-1>", lambda event, tag=str(i+1): flight.modifPassenger(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva, tag))

            scroll_canva.create_rectangle(50, (i * 150), 600, (i * 150) + 110)




    def selectPassengerDetails(self, canvas, number, imageModif):
        scroll_canva = tk.Canvas(canvas)
        scroll_canva.config(highlightthickness=0, borderwidth=0)
        scroll_canva.place(x=825, y=220, width=650, height=550)

        yscrollbar = tk.Scrollbar(canvas, orient="vertical", command=scroll_canva.yview)
        yscrollbar.place(x=1475, y=220, width=15, height=575)

        scroll_canva.configure(yscrollcommand=yscrollbar.set)
        scroll_canva.bind('<Configure>', lambda e: scroll_canva.configure(scrollregion=scroll_canva.bbox("all")))

        display_frame = tk.Frame(scroll_canva)
        display_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        scroll_canva.create_window((0, 0), window=display_frame, anchor="nw")


        modiPassenger_canva = tk.Canvas(canvas)
        modiPassenger_canva.place(x=100, y=550, width=600, height=200)


        passagers = []

        for i in range(int(number)):
            passager_details = {"member_type": None, "ticket_type": None}
            passagers.append(passager_details)

        
        valid = tk.Button(
        canvas,
        text = "Valid",
        bg = "black",
        fg = "white",
        font = ('Helvetica' , 10, 'bold'),
        command = lambda: flight.validationPassenger(self, passagers, verify))
        valid.place(x = 1135, y = 785)

        verify = tk.Label(text = "",font = ('Helvetica' , 10, 'bold'))
        verify.place(x=1185, y=787)


        flight.displayPassenger(self, canvas, scroll_canva, number, passagers, imageModif, modiPassenger_canva)
        

        


    def validdation_page(self):
        canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080)
        canvas.place(x=0, y=0)
        canvas.create_line(0, 0, 1920, 0, width=150, fill="black")
        canvas.create_line(775, 220, 775, 700, width=2, fill="black")

        Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white", bg="black")
        Cuicui.place(x=50, y=15)

        Title = tk.Label(text="Validation", font=('Helvetica', 30, 'bold'))
        Title.place(x=680, y=100)


        flight.completeFlight(self)
        flight.displayFlight(self, canvas)

        number = tk.Label(text="Select the number of passengers:", font=('Helvetica', 16, 'bold'))
        number.place(x=225, y=450)


        spinbox_frame = tk.Frame(canvas)
        spinbox_frame.place(x=310, y=500)

        spinbox = tk.Spinbox(spinbox_frame, from_ = 0, to = self.SeatsAvailable, increment=1, state="readonly")
        spinbox.pack(ipady=5)

        imageModif = Image.open("./photos/customer/modif.png")
        imageModif = imageModif.resize((20, 20))
        imageModif = ImageTk.PhotoImage(imageModif)

        valid = tk.Button(
        text = "OK",
        bg = "black",
        fg = "white",
        font = ('Helvetica' , 10, 'bold'),
        command = lambda: flight.selectPassengerDetails(self, canvas, spinbox.get(), imageModif))
        valid.place(x = 450, y = 500)


        initialization.cuicui.mainloop()
    


    def debut(FlightID):
        Flight = flight(FlightID, 0, 0, 0, 0, 0, 0)
        flight.validdation_page(Flight)




if __name__ == "__main__":
    flight.debut(64)








"""
def get_passenger_details(canvas):
    passenger_count = simpledialog.askinteger("Nombre de passagers", "Entrez le nombre de passagers:")
    print(f"Demande pour {passenger_count} passagers.")

    passenger_list = []



    scroll_canva = tk.Canvas(canvas, bg="green")
    scroll_canva.config(highlightthickness=0, borderwidth=0)
    scroll_canva.place(x=300, y=250, width=900, height=550)

    yscrollbar = tk.Scrollbar(canvas, orient="vertical", command=scroll_canva.yview)
    yscrollbar.place(x=1200, y=250, width=15, height=550)

    scroll_canva.configure(yscrollcommand=yscrollbar.set)
    scroll_canva.bind('<Configure>', lambda e: scroll_canva.configure(scrollregion=scroll_canva.bbox("all")))

    display_frame = tk.Frame(scroll_canva)
    display_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    scroll_canva.create_window((0, 0), window=display_frame, anchor="nw")



    for passenger_number in range(1, passenger_count + 1):
        passenger_details = {}

        # Catégorie du membre
        member_type_var = tk.StringVar()

        member_question_label = tk.Label(scroll_canva, text=f"Passager {passenger_number} : Choisissez le type de membre", font=("Helvetica", 10,"bold"))
        member_question_label.place(x=50, y=(passenger_number*150) + 50)

        member_type_combobox = ttk.Combobox(scroll_canva, textvariable=member_type_var, values=['Senior', 'Regular', 'Children'], state="readonly")
        member_type_combobox.set("Sélectionnez le type de membre")
        member_type_combobox.place(x=50, y=(passenger_number*150) + 70)

        member_label = tk.Label(scroll_canva, text="", font=("Helvetica", 9,"bold"))
        member_label.place(x=50, y=(passenger_number*150) + 90)

        def update_member_label(*args):
            member_label.config(text=f"Type de membre pour le passager {passenger_number} : {member_type_var.get().capitalize()}")

        member_type_var.trace_add("write", update_member_label)

        
        while True:
            initialization.cuicui.wait_variable(member_type_var)
            selected_member_type = member_type_var.get().lower()

            if selected_member_type in ['senior', 'regular', 'children']:
                passenger_details['passenger_number'] = passenger_number
                passenger_details['member_type'] = selected_member_type
                break
            else:
                tk.messagebox.showerror("Erreur", "Veuillez choisir un type de membre valide.")

        # Classe du billet
        ticket_types = ['Economy', 'Premium', 'Business']
        ticket_type_var = tk.StringVar()

        ticket_question_label = tk.Label(scroll_canva, text=f"Passager {passenger_number} : Choisissez le type de billet", font=("Helvetica", 10,"bold"))
        ticket_question_label.place(x=50, y=(passenger_number*150) + 110)

        ticket_type_combobox = ttk.Combobox(scroll_canva, textvariable=ticket_type_var, values=ticket_types, state="readonly")
        ticket_type_combobox.set("Sélectionnez le type de billet")
        ticket_type_combobox.place(x=50, y=(passenger_number*150) + 130)

        ticket_label = tk.Label(scroll_canva, text="", font=("Helvetica", 9, "bold"))
        ticket_label.place(x=50, y=(passenger_number*150) + 150)

        def update_ticket_label(*args):
            ticket_label.config(text=f"Type de billet pour le passager {passenger_number} : {ticket_type_var.get().capitalize()}")

        ticket_type_var.trace_add("write", update_ticket_label)

        while True:
            initialization.cuicui.wait_variable(ticket_type_var)
            selected_ticket_type = ticket_type_var.get().capitalize()

            if selected_ticket_type in ticket_types:
                passenger_details['ticket_type'] = selected_ticket_type
                break
            else:
                tk.messagebox.showerror("Erreur", "Veuillez choisir un type de billet valide.")

        passenger_list.append(passenger_details)

    return passenger_list


def choose_ticket_type(canvas):
    passenger_list = get_passenger_details(canvas)
    show_summary(passenger_list)


def show_summary(passenger_list):
    summary = "Récapitulatif des demandes :\n\n"

    for passenger_details in passenger_list:
        summary += f"Passager {passenger_details['passenger_number']} :\n"
        summary += f"   Type de membre : {passenger_details['member_type']}\n"
        summary += f"   Type de billet : {passenger_details['ticket_type']}\n\n"

    total_price = pay.calculate_price(passenger_list)
    summary += f"Prix total : {total_price} euros\n"

    payment_button = tk.Button(initialization.cuicui, text="Payer", font=("Helvetica", 12,"bold"), command=lambda: open_payment_window(initialization.cuicui, passenger_list))
    payment_button.pack(pady=10)

    result = messagebox.askokcancel("Récapitulatif des demandes", summary)


def open_payment_window(main_window, passenger_list):
    main_window.withdraw()
    pay.process_payment(main_window, passenger_list)


def affichage():
    initialization.cuicui.title("Welcome Page")

    canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080)
    canvas.place(x=0, y=0)
    canvas.create_line(0, 0, 1920, 0, width=150, fill="black")

    Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font = ('Helvetica' , 30, 'bold'), fg="white", bg="black")
    Cuicui.place(x=50, y=15)

    titre_label = tk.Label(text="Welcome on Cuicui Airlines", font=("Helvetica", 30, "bold"))
    titre_label.place(x=500, y=125)


    passenger_button = tk.Button(text="Choisir le nombre de passagers", font=("Helvetica", 12,"bold"), command=lambda: choose_ticket_type(canvas))
    passenger_button.place(x=600, y=200)

    initialization.cuicui.mainloop()


# Appelle la fonction d'affichage
if __name__ == "__main__":
    affichage()
"""








'''
import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
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

# Liste pour stocker les détails de chaque passager
passenger_details_list = []

# Fonction pour afficher les détails du vol
def reserver_vol(passenger_details):
    ville_depart = aeroport_depart_combobox.get()
    ville_arrivee = aeroport_arrivee_combobox.get()
    selected_date = date_select.get()

    flights = get_flights(ville_depart, ville_arrivee, selected_date)

    if flights:
        for flight in flights:
            print(f"Vol de {flight[0]} à {flight[1]} à {flight[2]} pour Passager {passenger_details['passenger_number']}")

        passenger_details['flights'] = flights  # Stocke les détails du vol dans le dictionnaire du passager
        return True  # Retourne que des vols ont été trouvés
    else:
        print("Aucun vol trouvé pour les critères spécifiés.")
        return False  # Retourne qu'aucun vol n'a été trouvé

# Fonction pour le processus de paiement pour un passager
def process_payment(passenger_details):
    effacer.effacer_page()

    initialization.cuicui.title(f"Processus de Paiement - Passager {passenger_details['passenger_number']}")

    print(f"Type de membre pour Passager {passenger_details['passenger_number']} : {passenger_details['member_type']}")

    payment_label = tk.Label(initialization.cuicui, text=f"Passager {passenger_details['passenger_number']}, veuillez saisir les informations de paiement en tant que {passenger_details['member_type']} :", font=("Broadway", 14))
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
            messagebox.showinfo("Paiement réussi", f"Paiement pour Passager {passenger_details['passenger_number']} traité avec succès. Merci!")
        else:
            messagebox.showerror("Erreur de paiement", "Veuillez vérifier vos informations de paiement.")

    pay_button = tk.Button(initialization.cuicui, text="Payer", font=("Broadway", 14), command=validate_payment)
    pay_button.pack()

# Fonction pour le processus complet pour un nombre spécifié de passagers
def process_for_passenger_count():
    passenger_count = simpledialog.askinteger("Nombre de passagers", "Entrez le nombre de passagers:")
    print(f"Demande de réservation pour {passenger_count} passagers.")

    for passenger_number in range(1, passenger_count + 1):
        passenger_details = {}  # Dictionnaire pour stocker les détails du passager
        passenger_details['passenger_number'] = passenger_number

        # Boucle de saisie pour garantir un type de membre valide
        while True:
            member_type = tk.simpledialog.askstring("Type de membre", f"Passager {passenger_number} : Êtes-vous un senior, un client régulier ou un enfant?")
            if member_type.lower() in ['senior', 'regular', 'children']:
                break
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un type de membre valide (senior, regular, children).")

        passenger_details.append(member_type)
        print(passenger_details[passenger_number-1])

        # Affiche le message en fonction du résultat de la réservation
        if reserver_vol(passenger_details):
            process_payment(passenger_details)
        else:
            print("Aucun vol n'a été réservé pour le passager ", passenger_number)

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
reserver_bouton = tk.Button(content_frame, text="Search", font=("Broadway", 10), command=process_for_passenger_count)
reserver_bouton.grid(row=0, column=8, columnspan=2, pady=10)

# Lance la boucle principale
initialization.cuicui.mainloop() 
'''

""""
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from tkcalendar import DateEntry

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
            sql = "SELECT DepartureCity, ArrivalCity, DepartureTime FROM flight WHERE DepartureCity = %s AND ArrivalCity = %s AND Date = %s"
            cursor.execute(sql, (ville_depart, ville_arrivee, date))
            result = cursor.fetchall()

            return result

    finally:
        connection.close()

def reserver_vol():
    ville_depart = aeroport_depart_combobox.get()
    ville_arrivee = aeroport_arrivee_combobox.get()
    selected_date = date_select.get()

    flights = get_flights(ville_depart, ville_arrivee, selected_date)

    for flight in flights:
        print("Vol de", flight[0], "à", flight[1], "à", flight[2])

def process_payment():
    cuicui.withdraw()  

    payment_page = tk.Toplevel()
    payment_page.title("Processus de Paiement")

    payment_label = tk.Label(payment_page, text="Veuillez saisir les informations de paiement :", font=("Broadway", 14))
    payment_label.pack()

    card_label = tk.Label(payment_page, text="Numéro de carte :", font=("Broadway", 12))
    card_entry = tk.Entry(payment_page, show="*")
    card_label.pack()
    card_entry.pack()

    expiry_label = tk.Label(payment_page, text="Date d'expiration (MM/YY) :", font=("Broadway", 12))
    expiry_entry = tk.Entry(payment_page)
    expiry_label.pack()
    expiry_entry.pack()

    cvv_label = tk.Label(payment_page, text="CVV :", font=("Broadway", 12))
    cvv_entry = tk.Entry(payment_page, show="*")
    cvv_label.pack()
    cvv_entry.pack()

    def validate_payment():
        card_number = card_entry.get()
        expiry_date = expiry_entry.get()
        cvv = cvv_entry.get()

        if len(card_number) == 16 and len(expiry_date) == 5 and len(cvv) == 3:
            messagebox.showinfo("Paiement réussi", "Votre paiement a été traité avec succès. Merci!")
            payment_page.destroy()  
            cuicui.deiconify()  
        else:
            messagebox.showerror("Erreur de paiement", "Veuillez vérifier vos informations de paiement.")

    pay_button = tk.Button(payment_page, text="Payer", font=("Broadway", 14), command=validate_payment)
    pay_button.pack()

cuicui = tk.Tk()
cuicui.title("Welcome Page")

header_frame = tk.Frame(cuicui, highlightbackground="black", highlightthickness=5)
header_frame.pack(pady=20)

titre_label = tk.Label(cuicui, text="Welcome on Cuicui Airlines", font=("Broadway", 30))
titre_label.pack(pady=20)

content_frame = tk.Frame(cuicui)
content_frame.pack()

aeroport_depart_label = tk.Label(content_frame, text="Departure", font=("Broadway", 10))
aeroport_depart_label.grid(row=0, column=0, padx=10, pady=5)

cities = get_cities()
aeroport_depart_combobox = ttk.Combobox(content_frame, values=cities)
aeroport_depart_combobox.grid(row=0, column=1, padx=10, pady=5)

aeroport_arrivee_label = tk.Label(content_frame, text="Arrival", font=("Broadway", 10))
aeroport_arrivee_label.grid(row=0, column=2, padx=10, pady=5)

aeroport_arrivee_combobox = ttk.Combobox(content_frame, values=cities)
aeroport_arrivee_combobox.grid(row=0, column=3, padx=10, pady=5)

date_label = tk.Label(content_frame, text="Date", font=("Broadway", 10))
date_label.grid(row=0, column=4, padx=10, pady=5)

date_select = DateEntry(content_frame, date_pattern="yyyy-mm-dd", fg="black", bg="white", width=10, font=('Broadway', 10, 'bold'))
date_select.grid(row=0, column=5, padx=10, pady=5)

reserver_bouton = tk.Button(content_frame, text="Search", font=("Broadway", 10), command=reserver_vol)
reserver_bouton.grid(row=0, column=8, columnspan=2, pady=10)

show_payment_button = tk.Button(content_frame, text="Show Payment", font=("Broadway", 10), command=process_payment)
show_payment_button.grid(row=0, column=9, columnspan=2, pady=10)

cuicui.mainloop()
"""