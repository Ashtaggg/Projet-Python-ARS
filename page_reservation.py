import pymysql  # Importe le module pymysql pour se connecter à la base de données MySQL.
import tkinter as tk  # Importe le module tkinter pour créer une interface graphique.
from PIL import Image, ImageTk  # Importe les modules Pillow (PIL) pour manipuler des images.
from initialization import cuicui  # Importe la variable "cuicui" d'un fichier "initialization" (c'est inhabituel, assurez-vous que cette importation est correcte).

# Définition de la classe principale de l'application.
class FlightReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Réservation de vol / CuiCui Airline")

        # Obtient les dimensions de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcul de la taille initiale de la fenêtre
        initial_width = int(screen_width * 0.8)
        initial_height = int(screen_height * 0.8)

        # Définit la taille initiale et limite la taille maximale et minimale
        self.root.geometry(f"{initial_width}x{initial_height}+{int((screen_width - initial_width) / 2)}+{int((screen_height - initial_height) / 2)}")
        self.root.minsize(int(screen_width * 0.5), int(screen_height * 0.5))
        self.root.maxsize(screen_width, screen_height)

        self.load_flights()
        self.create_widgets()

    # Méthode pour charger les informations des vols depuis la base de données.
    def load_flights(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='projet_python_ars',
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM Flight")  # Exécute une requête SQL pour récupérer tous les vols.
        rows = cur.fetchall()  # Récupère toutes les lignes résultantes de la requête.
        self.flights = rows  # Stocke les informations des vols dans l'attribut "flights" de la classe.
        cur.close()
        conn.close()

    # Méthode pour effectuer une réservation de vol.
    def make_reservation(self):
        flight_id = self.flight_var.get()  # Récupère l'ID du vol sélectionné.
        departure_date = self.departure_date_entry.get()  # Récupère la date de départ entrée par l'utilisateur.
        arrival_date = self.arrival_date_entry.get()  # Récupère la date d'arrivée entrée par l'utilisateur.
        # Ajoutez ici le code pour enregistrer la réservation dans la base de données ou effectuer d'autres opérations.

        # Animation : Changement de couleur et de texte du bouton de réservation.
        self.submit_button.config(text="Réservation en cours...", state="disabled")  # Change le texte et l'état du bouton.
        self.submit_button.update_idletasks()  # Met à jour l'interface utilisateur.
        self.submit_button.after(2000, lambda: self.reset_button())  # Définit un délai pour réinitialiser le bouton.

    # Méthode pour réinitialiser le bouton de réservation après un délai.
    def reset_button(self):
        self.submit_button.config(text="Réserver", state="active")  # Réinitialise le texte et l'état du bouton.
        self.submit_button.update_idletasks()  # Met à jour l'interface utilisateur.

    # Méthode pour créer les éléments de l'interface graphique.
    def create_widgets(self):
        # Charger l'image de fond avec PIL (Pillow).
        bg_image = Image.open("./photos/avion.jpg")  # Charge une image depuis le fichier "avion.jpg".
        bg_photo = ImageTk.PhotoImage(bg_image)  # Crée une version adaptée à tkinter de l'image.

        # Crée un canevas pour afficher l'image de fond.
        canvas = tk.Canvas(cuicui, width=bg_image.width, height=bg_image.height)  # Crée un canevas avec les dimensions de l'image.

        canvas.pack()  # Affiche le canevas dans la fenêtre principale.
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)  # Place l'image sur le canevas.
        canvas.image = bg_photo  # Conserve une référence à l'image pour éviter qu'elle ne soit supprimée par le ramasse-miettes.

        # Crée un cadre pour le contenu de l'interface.
        center_frame = tk.Frame(canvas)  # Crée un cadre à l'intérieur du canevas.
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place le cadre au centre du canevas.

        # Crée une étiquette de bienvenue.
        welcome_label = tk.Label(center_frame, text="Bienvenue sur notre site de réservation de vols", font=("broadway", 16))
        welcome_label.pack()  # Affiche l'étiquette dans le cadre.

        # Crée une variable et un menu déroulant pour sélectionner un vol.
        self.flight_var = tk.StringVar(center_frame)
        self.flight_var.set(self.flights[0][0])  # Définit la valeur initiale de la variable.

        flight_label = tk.Label(center_frame, text="Sélectionnez un vol :", font=("broadway", 14))
        flight_option = tk.OptionMenu(center_frame, self.flight_var, *[flight[0] for flight in self.flights])
        flight_label.pack()
        flight_option.pack()

        # Crée des étiquettes et des champs de texte pour la date de départ et la date d'arrivée.
        departure_date_label = tk.Label(center_frame, text="Date de départ :", font=("broadway", 14))
        self.departure_date_entry = tk.Entry(center_frame)
        departure_date_label.pack()
        self.departure_date_entry.pack()

        arrival_date_label = tk.Label(center_frame, text="Date d'arrivée :", font=("broadway", 14))
        self.arrival_date_entry = tk.Entry(center_frame)
        arrival_date_label.pack()
        self.arrival_date_entry.pack()

        # Crée un bouton pour effectuer la réservation.
        self.submit_button = tk.Button(center_frame, text="Réserver", font=("broadway", 14), command=self.make_reservation)
        self.submit_button.pack()  # Affiche le bouton dans le cadre.

# Point d'entrée du programme.
if __name__ == "__main__":
    app = FlightReservationApp(cuicui)  # Crée une instance de l'application en passant la fenêtre racine "cuicui".
    cuicui.mainloop()  # Démarre la boucle principale de l'interface graphique pour afficher l'application.
