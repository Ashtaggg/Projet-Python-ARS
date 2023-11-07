import pymysql
import tkinter as tk
from initialization import cuicui
from PIL import Image, ImageTk

class FlightReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Réservation de vol / CuiCui Airline")
        self.load_flights()

        self.create_widgets()

    def load_flights(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='projet_python_ars',
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM Flight")
        rows = cur.fetchall()
        self.flights = rows
        cur.close()
        conn.close()

    def make_reservation(self):
        flight_id = self.flight_var.get()
        departure_date = self.departure_date_entry.get()
        arrival_date = self.arrival_date_entry.get()
        # Ajoutez ici le code pour enregistrer la réservation dans la base de données ou effectuer d'autres opérations.

        # Animation : Changement de couleur et de texte
        self.submit_button.config(text="Réservation en cours...", state="disabled")
        self.submit_button.update_idletasks()
        self.submit_button.after(2000, lambda: self.reset_button())

    def reset_button(self):
        self.submit_button.config(text="Réserver", state="active")
        self.submit_button.update_idletasks()

    def create_widgets(self):
        # Charger l'image de fond avec PIL (Pillow)
        bg_image = Image.open("avion.jpg")
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Créer un canevas pour afficher l'image de fond
        canvas = tk.Canvas(self.root, width=bg_image.width, height=bg_image.height)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)
        canvas.image = bg_photo

        # Créer un cadre pour le contenu
        center_frame = tk.Frame(canvas)
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        welcome_label = tk.Label(center_frame, text="Bienvenue sur notre site de réservation de vols", font=("broadway", 16))
        welcome_label.pack()

        self.flight_var = tk.StringVar(center_frame)
        self.flight_var.set(self.flights[0][0])

        flight_label = tk.Label(center_frame, text="Sélectionnez un vol :", font=("broadway", 14))
        flight_option = tk.OptionMenu(center_frame, self.flight_var, *[flight[0] for flight in self.flights])
        flight_label.pack()
        flight_option.pack()

        departure_date_label = tk.Label(center_frame, text="Date de départ :", font=("broadway", 14))
        self.departure_date_entry = tk.Entry(center_frame)
        departure_date_label.pack()
        self.departure_date_entry.pack()

        arrival_date_label = tk.Label(center_frame, text="Date d'arrivée :", font=("broadway", 14))
        self.arrival_date_entry = tk.Entry(center_frame)
        arrival_date_label.pack()
        self.arrival_date_entry.pack()

        self.submit_button = tk.Button(center_frame, text="Réserver", font=("broadway", 14), command=self.make_reservation)
        self.submit_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightReservationApp(root)
    root.mainloop()
