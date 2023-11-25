import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk

import choice_person
import query
import initialization
import effacer
import choice_person
import customer
import login


class CuicuiAirlinesApp():
    def __init__(self, FlightID, DepartureCity, ArrivalCity, DepartureTime, ArrivalTime, TicketPrice, SeatsAvailable):
        self.FlightID = FlightID
        self.DepartureCity = DepartureCity
        self.ArrivalCity = ArrivalCity
        self.DepartureTime = DepartureTime
        self.ArrivalTime = ArrivalTime
        self.TicketPrice = TicketPrice
        self.SeatsAvailable = SeatsAvailable


    def connection():
        initialization.lastPage = "page_accueil"
        if initialization.login == 0:
            login.login_page()
        elif initialization.login == 1:
            customer.customer.customer_page(initialization.member)



    def welcome_page(self):
        initialization.cuicui.title("Booking page")

        canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080)
        canvas.place(x=0, y=0)
        canvas.create_line(0, 0, 1920, 0, width=150, fill="black")

        Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white",bg="black")
        Cuicui.place(x=50, y=15)

        titre_label = tk.Label(initialization.cuicui, text="Welcome on Cuicui Airlines", font=("Broadway", 20))
        titre_label.place(x=550, y=90)

        imageCustomer = Image.open("./photos/profil_picture/photo_profil_inverse.png")
        imageCustomer = imageCustomer.resize((60, 60))
        imageCustomer = ImageTk.PhotoImage(imageCustomer)
        canvas.create_image(1420, 10, anchor=tk.NW, image=imageCustomer, tags="image")
        canvas.tag_bind("image", "<Button-1>", lambda event, tag="image": CuicuiAirlinesApp.connection())

        # CANVAS SUPP

        canva_sup = tk.Canvas(canvas)
        canva_sup.config(highlightthickness=0, borderwidth=0)#
        canva_sup.place(x=75, y=220, width=1350, height=600)

        canva_sup.create_line(600, 0, 600, 800, width=2, fill="black")

        #DEPARTURE
        aeroport_depart_label = tk.Label( text="Departure", font=("Broadway", 10))
        aeroport_depart_label.place(x=200, y=150)
        cities = CuicuiAirlinesApp.get_cities(self)
        #print("TEST 2 cities ",cities)

        aeroport_depart_combobox = ttk.Combobox(values=cities, state="readonly")
        aeroport_depart_combobox.place(x=300, y=150)

        #ARRIVAL
        aeroport_arrivee_label = tk.Label( text="Arrival", font=("Broadway", 10))
        aeroport_arrivee_label.place(x=450, y=150)
        aeroport_arrivee_combobox = ttk.Combobox(values=cities, state="readonly")
        aeroport_arrivee_combobox.place(x=550, y=150)

        #DATE
        date_label = tk.Label( text="Date", font=("Broadway", 10))
        date_label.place(x=750, y=150)
        date_select = DateEntry( date_pattern="yyyy-mm-dd", fg="black", bg="white", width=10,font=('Broadway', 10, 'bold'))
        date_select.place(x=800, y=150)

        #SEARCH
        reserver_bouton = tk.Button( text="Search", font=("Broadway", 10),command=lambda: CuicuiAirlinesApp.reserver_vol(self,aeroport_depart_combobox,aeroport_arrivee_combobox,date_select,canva_sup))
        reserver_bouton.place(x=950, y=150)



        initialization.cuicui.mainloop()

    def get_cities(self):
        cities=[]
        request = "SELECT DISTINCT DepartureCity FROM flight"
        citie = query.requestDataBase(request)
        for i in range(len(citie)):
            cities.append(citie[i][0])
            #print("TEST cities ",cities)

        return cities

    def get_flights(self, departure_city, arrival_city, date):
        #print(date[:10])
        #print("We are counting the number of fly from ",departure_city," to ",arrival_city," at the date ",date)
        request = f"SELECT COUNT(*) FROM flight WHERE DepartureCity ='{departure_city}' AND ArrivalCity = '{arrival_city}' AND LEFT(DepartureTime,10) ='{date[:10]}';"
        output = query.requestDataBase(request)
        result = output[0][0]
        if(int(result) >= 1):
            #print("Fly is existing")
            request = f"SELECT FlightID FROM flight WHERE DepartureCity ='{departure_city}' AND ArrivalCity = '{arrival_city}' AND LEFT(DepartureTime,10) ='{date[:10]}';"
            output = query.requestDataBase(request)
        elif (int(result) == 0):
            #print("Fly is not existing at this date ")
            #print("We are counting the number of fly from ", departure_city, " to ", arrival_city)
            request = f"SELECT COUNT(*) FROM flight WHERE DepartureCity ='{departure_city}' AND ArrivalCity = '{arrival_city}';"
            output = query.requestDataBase(request)
            result = output[0][0]

            if(int(result) >= 1):
                #print("Fly existing")
                request = f"SELECT FlightID FROM flight WHERE DepartureCity = '{departure_city}' AND ArrivalCity = '{arrival_city}';"
                output = query.requestDataBase(request)


            #elif(int(result) == 0):
                #print("No fly from ",departure_city," for ", arrival_city," the ",date)

        #print(" <---------- RESULT ---------->",output)

        return output

    def reserver_vol(self,aeroport_depart_combobox,aeroport_arrivee_combobox,date_select,canva_sup):
        for widget in canva_sup.winfo_children():
            widget.destroy()
        id_fly=[]
        ville_depart = str(aeroport_depart_combobox.get())
        ville_arrivee = str(aeroport_arrivee_combobox.get())
        date = str(date_select.get() + " 00:00:00")

        if not ville_depart or not ville_arrivee:
            #print("Veuillez remplir tous les champs.")
            return

        #effacer.effacer_page()



        #print("Ville de départ:", ville_depart)
        #print("Ville d'arrivée:", ville_arrivee)
        #print("Date sélectionnée:", date)

        # Récupérez les vols en fonction des sélections de l'utilisateur
        flights = CuicuiAirlinesApp.get_flights(self, ville_depart, ville_arrivee, date)
        #print("test len fly",len(flights))


        # REMPLIR TOUT LES CHOIX DANS LA CLASSE ET LES AFFICHER
        #TitleRight = tk.Label(canva_sup,text=f"                                                                                                   ", font=('Helvetica', 22, 'bold'))
        #TitleRight.place(x=0, y=0)

        if(flights[0][0] == 0):
            #print("PAS DE VOL A CETTE DATE")
            TitleRight = tk.Label(canva_sup,text=f"No Fly Available from {ville_depart} to {ville_arrivee}", font=('Helvetica', 22, 'bold'))
            TitleRight.place(x=0, y=0)

        else:
            for i in range(len(flights)):
                id_fly.append(flights[i][0])
                #print("Test id_fly ", id_fly[i])
            ## PAGE DEROULANTE
            #print("LISTE DES VOLS A CETTE DATE")
            CuicuiAirlinesApp.show_fly(self,id_fly,canva_sup)

            # METTRE AFFICHAGE VOL ICI

            # AFFICHAGE IMAGE
            #self.image_display = tk.Label(initialization.cuicui)
            #self.image_display.pack()
            #self.image_display.place(x=700, y=250)
            #show_image = tk.Button(initialization.cuicui,command=CuicuiAirlinesApp.show_image(self,ville_arrivee))
            CuicuiAirlinesApp.show_image(self, ville_arrivee,canva_sup)
            #show_image.pack()

    def show_fly(self,id_fly,canva_sup):
        #print("FLY AVAILABLE")
        TitleRight = tk.Label(canva_sup,text="Fly Available", font=('Helvetica', 22, 'bold'))
        TitleRight.place(x=0, y=0)

        #scroll_canva = tk.Canvas(initialization.cuicui)

        #for widget in scroll_canva.winfo_children():
        #    widget.destroy()

        #pastFlights = booking(0, 0, 0, 0, 0, 0)
        #nbrBooking = booking.findNbrBooking(pastFlights, self.CustomerID)
        #if nbrBooking == 0:
        #    noBooking = tk.Label(text="No previous flights booked", font=('Helvetica', 11, 'bold'))
        #    noBooking.place(x=1010, y=350)
        if (True == 1):

            scroll_canva = tk.Canvas(canva_sup)
            scroll_canva.config(highlightthickness=0, borderwidth=0) #,background="green")
            scroll_canva.place(x=0, y=40, width=500, height=525)

            yscrollbar = tk.Scrollbar(canva_sup, orient="vertical", command=scroll_canva.yview)
            yscrollbar.place(x=580, y=0, width=15, height=600)

            scroll_canva.configure(yscrollcommand=yscrollbar.set)
            scroll_canva.bind('<Configure>', lambda e: scroll_canva.configure(scrollregion=scroll_canva.bbox("all")))

            display_frame = tk.Frame(scroll_canva)
            display_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

            scroll_canva.create_window((0, 0), window=display_frame, anchor="nw")

            boutons=[]



            for i in range(len(id_fly)):
                #print("IF TRUE",id_fly[i])

                request = f"SELECT DepartureCity, ArrivalCity, DepartureTime, ArrivalTime, TicketPrice, SeatsAvailable FROM flight WHERE FlightID = '{id_fly[i]} ';"
                output = query.requestDataBase(request)

                #print("OUTPUT AFFICHAGE SCROLL", output)
                fly = [str(output[0][0]),str(output[0][1]),str(output[0][2]),str(output[0][3]),str(output[0][4]),output[0][5]]

                #affichage_vol_label.place(x=75, y=i*40 + 50)
                #print("AFFICHAGE FLY : ",fly[0])
                scroll_canva.create_text(100, (i * 150) + 40, text=fly[0] + "  >  " + fly[1], font=('Helvetica', 14, 'bold'))
                scroll_canva.create_text(125, (i * 150) + 80, text=str(fly[2])[:16], font=('Helvetica', 10, 'bold'))
                scroll_canva.create_text(250, (i * 150) + 80, text=fly[0], font=('Helvetica', 10, 'bold'))
                scroll_canva.create_text(125, (i * 150) + 100, text=str(fly[3])[:16], font=('Helvetica', 10, 'bold'))
                scroll_canva.create_text(250, (i * 150) + 100, text=fly[1], font=('Helvetica', 10, 'bold'))
                scroll_canva.create_rectangle(5, (i * 150) + 10, 495, (i * 150) + 130)


                bouton = tk.Button(canva_sup, text=f"Reserve", command=lambda num=id_fly[i]: CuicuiAirlinesApp.clicked(self,num))
                bouton.pack(padx=20,pady=20)
                scroll_canva.create_window(450, (i * 150) + 100, window=bouton)  # Position du bouton dans le canevas

                boutons.append(bouton)


    def clicked(self,numBouton):
        # PAGE POUR ANTO
        #print("le bouton ",numBouton," est clické")
        effacer.effacer_page()
        choice_person.flight.debut(numBouton)
        #choice_person.affichage()



    '''
                for i in range(100):
                bouton = tk.Button(initialization.cuicui, text=f"Mon Bouton {i}", command=lambda num=i: CuicuiAirlinesApp.clicked(self,num))
                scroll_canva.create_window(75, i*40 + 50, window=bouton)  # Position du bouton dans le canevas

                #scroll_canva.create_text(75, (i * 20), text="x test connard",font=('Helvetica', 10, 'bold'))
                   def clicked():
                   on_button_click(number)
                   bouton = tk.Button(root, text=f"Mon Bouton {number}", command=clicked)
                   scroll_canvas.create_window(75, number * 40 + 50, window=bouton)

                   
    '''

    def show_image(self,city,canva_sup):
        # To remove the space
        if " " in city:
            city = city.replace(" ", "_")
        city=city.lower()

        img = Image.open(f"photos/search_city/{city}.jpg")

        img = img.resize((750, 500),Image.LANCZOS)#, Image.ANTIALIAS) 750 500

        #img = img.resize(500, 500)  # Redimensionnement de l'image
        self.photo = ImageTk.PhotoImage(img)

        canva_sup.create_image(700 , 25, anchor=tk.NW, image=self.photo)
        #self.image_display.configure(image=photo)
        #self.image_display.image = photo




    def affichage_vol(self, flightsNewD, flightsNewA, date):
        fly = flightsNewD + "-" + flightsNewA + "-" + date
        combobox = ttk.Combobox(initialization.cuicui, values=fly, state="readonly",width=50, height=10)
        combobox.pack(padx=10, pady=10)

    def tri_vol(self):
        count = "SELECT COUNT(*) FROM flight;"
        nbDeVol = query.requestDataBase(count)
        nbDeVol = nbDeVol[0][0]
        #print(nbDeVol)
        if int(nbDeVol) > 0:
            delete = "DELETE FROM flight WHERE DepartureTime < NOW();"
            query.requestDataBase(delete)
            #print("fly were delete.")
        #else:
            #print("RAS.")

if __name__ == "__main__":
    CuicuiAirlinesApp.welcome_page(initialization.cuicui)
