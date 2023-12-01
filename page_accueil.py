import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk

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

    def connection(self):
        initialization.lastPage = "page_accueil"
        if initialization.login == 0:
            login.login_page()
        elif initialization.login == 1:
            customer.customer.customer_page(initialization.member)

    def welcome_page(self):
        initialization.cuicui.title("Booking page")

        canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080,bg=initialization.bg_color)
        canvas.place(x=0, y=0)
        canvas.create_line(0, 0, 1920, 0, width=150, fill="black",)

        Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white",bg="black")
        Cuicui.place(x=50, y=15)

        titre_label = tk.Label(initialization.cuicui, text="Welcome on Cuicui Airlines", font=("Helvetica", 20),bg=initialization.bg_color)
        titre_label.place(x=550, y=90)

        imageCustomer = Image.open("./photos/profil_picture/photo_profil_inverse.png")
        imageCustomer = imageCustomer.resize((60, 60))
        imageCustomer = ImageTk.PhotoImage(imageCustomer)
        canvas.create_image(1420, 10, anchor=tk.NW, image=imageCustomer, tags="image")
        canvas.tag_bind("image", "<Button-1>", lambda event, tag="image": CuicuiAirlinesApp.connection(self))

        # CANVAS SUPP

        canva_sup = tk.Canvas(canvas)
        canva_sup.config(highlightthickness=0, borderwidth=0,bg=initialization.bg_color)
        canva_sup.place(x=75, y=220, width=1350, height=600)

        canva_sup.create_line(600, 0, 600, 800, width=2, fill="black")

        #DEPARTURE
        aeroport_depart_label = tk.Label( text="Departure", font=("Helvetica", 10),bg=initialization.bg_color)
        aeroport_depart_label.place(x=200, y=150)
        cities = CuicuiAirlinesApp.get_cities(self)

        aeroport_depart_combobox = ttk.Combobox(values=cities, state="readonly")
        aeroport_depart_combobox.place(x=300, y=150)

        #ARRIVAL
        aeroport_arrivee_label = tk.Label( text="Arrival", font=("Helvetica", 10),bg=initialization.bg_color)
        aeroport_arrivee_label.place(x=450, y=150)
        aeroport_arrivee_combobox = ttk.Combobox(values=cities, state="readonly")
        aeroport_arrivee_combobox.place(x=550, y=150)

        #DATE
        date_label = tk.Label( text="Date", font=("Helvetica", 10),bg=initialization.bg_color)
        date_label.place(x=750, y=150)
        date_select = DateEntry( date_pattern="yyyy-mm-dd", fg="black", bg="white", width=10,font=('Helvetica', 10, 'bold'))
        date_select.place(x=800, y=150)

        #SEARCH
        reserver_bouton = tk.Button( text="Search", font=("Helvetica", 10),command=lambda: CuicuiAirlinesApp.booking_fly(self,aeroport_depart_combobox,aeroport_arrivee_combobox,date_select,canva_sup),bg=initialization.bg_color)
        reserver_bouton.place(x=950, y=150)

        initialization.cuicui.mainloop()

    def get_cities(self):
        cities=[]
        request = "SELECT DISTINCT DepartureCity FROM flight"
        citie = query.requestDataBase(request)
        for i in range(len(citie)):
            cities.append(citie[i][0])

        return cities

    def get_flights(self, departure_city, arrival_city, date):
        no_fly = 0
        print(date[:10])
        request = f"SELECT COUNT(*) FROM flight WHERE ((DepartureCity ='{departure_city}') AND (ArrivalCity = '{arrival_city}') AND (LEFT(DepartureTime,10) ='{date[:10]}'));"
        output = query.requestDataBase(request)
        result = output[0][0]
        if(int(result) >= 1):
            request = f"SELECT FlightID FROM flight WHERE DepartureCity ='{departure_city}' AND ArrivalCity = '{arrival_city}' AND LEFT(DepartureTime,10) ='{date[:10]}';"
            output = query.requestDataBase(request)
        elif (int(result) == 0):
            request = f"SELECT COUNT(*) FROM flight WHERE DepartureCity ='{departure_city}' AND ArrivalCity = '{arrival_city}' AND LEFT(DepartureTime,10) >='{date[:10]}';"
            output = query.requestDataBase(request)
            result = output[0][0]
            if(int(result) >= 1):
                request = f"SELECT FlightID FROM flight WHERE DepartureCity = '{departure_city}' AND ArrivalCity = '{arrival_city}' AND LEFT(DepartureTime,10) >='{date[:10]}';"
                output = query.requestDataBase(request)


            elif(int(result) == 0):
                no_fly = 1
                request = f"SELECT FlightID FROM flight WHERE DepartureCity = '{departure_city}' AND LEFT(DepartureTime,10) >='{date[:10]}';"
                output = query.requestDataBase(request)
                print("No fly from ",departure_city," for ", arrival_city," the ",date)

        return no_fly,output


    def booking_fly(self,aeroport_depart_combobox,aeroport_arrivee_combobox,date_select,canva_sup):
        for widget in canva_sup.winfo_children():
            widget.destroy()
        id_fly=[]
        ville_depart = str(aeroport_depart_combobox.get())
        ville_arrivee = str(aeroport_arrivee_combobox.get())
        date = str(date_select.get() + " 00:00:00")

        if not ville_depart or not ville_arrivee:
            return

        state,flights = CuicuiAirlinesApp.get_flights(self, ville_depart, ville_arrivee, date)

        if(state == 1): #flights[0][0]
            print("PAS DE VOL A CETTE DATE")
            TitleRight = tk.Label(canva_sup,text=f"No Fly Available from {ville_depart} to {ville_arrivee}", font=('Helvetica', 22, 'bold'),bg=initialization.bg_color)
            TitleRight.place(x=0, y=0)


        for i in range(len(flights)):
            id_fly.append(flights[i][0])

        CuicuiAirlinesApp.show_fly(self,id_fly,canva_sup,state)

        CuicuiAirlinesApp.show_image(self, ville_arrivee,canva_sup)

    def show_fly(self,id_fly,canva_sup,state):
        if (state == 0):
            TitleRight = tk.Label(canva_sup,text="Fly Available", font=('Helvetica', 22, 'bold'),bg=initialization.bg_color)
            TitleRight.place(x=0, y=0)

        if (True == 1):

            scroll_canva = tk.Canvas(canva_sup)
            scroll_canva.config(highlightthickness=0, borderwidth=0,bg=initialization.bg_color,background=initialization.bg_color) #,background="green")
            scroll_canva.place(x=0, y=40, width=500, height=525)

            yscrollbar = tk.Scrollbar(canva_sup, orient="vertical", command=scroll_canva.yview,background=initialization.bg_color)
            yscrollbar.place(x=580, y=50, width=15, height=550)

            scroll_canva.configure(yscrollcommand=yscrollbar.set)
            scroll_canva.bind('<Configure>', lambda e: scroll_canva.configure(scrollregion=scroll_canva.bbox("all")))

            display_frame = tk.Frame(scroll_canva)
            display_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

            scroll_canva.create_window((0, 0), window=display_frame, anchor="nw")

            boutons=[]



            for i in range(len(id_fly)):

                request = f"SELECT DepartureCity, ArrivalCity, DepartureTime, ArrivalTime, TicketPrice, SeatsAvailable FROM flight WHERE FlightID = '{id_fly[i]} ';"
                output = query.requestDataBase(request)

                fly = [str(output[0][0]),str(output[0][1]),str(output[0][2]),str(output[0][3]),str(output[0][4]),output[0][5]]

                scroll_canva.create_text(140, (i * 150) + 40, text=fly[0] + "  >  " + fly[1], font=('Helvetica', 14, 'bold'))
                scroll_canva.create_text(125, (i * 150) + 80, text=str(fly[2])[:16], font=('Helvetica', 10, 'bold'))
                scroll_canva.create_text(250, (i * 150) + 80, text=fly[0], font=('Helvetica', 10, 'bold'))
                scroll_canva.create_text(125, (i * 150) + 100, text=str(fly[3])[:16], font=('Helvetica', 10, 'bold'))
                scroll_canva.create_text(250, (i * 150) + 100, text=fly[1], font=('Helvetica', 10, 'bold'))
                scroll_canva.create_rectangle(5, (i * 150) + 10, 495, (i * 150) + 130)


                bouton = tk.Button(canva_sup, text=f"Reserve", command=lambda num=id_fly[i]: CuicuiAirlinesApp.clicked(self,num),bg=initialization.bg_color)
                bouton.pack(padx=20,pady=20)
                scroll_canva.create_window(450, (i * 150) + 100, window=bouton)  # Position du bouton dans le canevas

                boutons.append(bouton)


    def clicked(self,numBouton):
        effacer.effacer_page()
        initialization.lastPage = "page_accueil"
        choice_person.flight.debut(numBouton)


    def show_image(self,city,canva_sup):
        if " " in city:
            city = city.replace(" ", "_")
        city=city.lower()

        img = Image.open(f"photos/search_city/{city}.jpg")

        img = img.resize((750, 500),Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)

        canva_sup.create_image(700 , 25, anchor=tk.NW, image=self.photo)





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


if __name__ == "__main__":
    CuicuiAirlinesApp.welcome_page(initialization.cuicui)
