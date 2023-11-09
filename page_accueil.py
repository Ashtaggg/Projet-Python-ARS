import tkinter as tk
from PIL import Image, ImageTk

class FlightReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bienvenue sur CuiCui Airline")

        self.create_widgets()

    def create_widgets(self):
        bg_image = Image.open("./photos/avion.jpg")
        bg_photo = ImageTk.PhotoImage(bg_image)

        canvas = tk.Canvas(root, width=bg_image.width, height=bg_image.height)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)
        canvas.image = bg_photo

        center_frame = tk.Frame(canvas)
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        welcome_label = tk.Label(center_frame, text="Bienvenue sur CuiCui Airline", font=("broadway", 20, "underline"), fg="blue")
        welcome_label.pack(pady=20)

        motivation_label = tk.Label(center_frame, text="Prêt à explorer le monde?", font=("broadway", 16), fg="green")
        motivation_label.pack(pady=10)

        login_label = tk.Label(center_frame, text="Connexion à votre compte", font=("broadway", 14, "underline"))
        login_label.pack(pady=10)

        # Bouton de connexion
        login_button = tk.Button(center_frame, text="Connexion", font=("broadway", 12), command=self.login)
        login_button.pack(pady=5)

        register_label = tk.Label(center_frame, text="Vous n'êtes pas encore client?", font=("broadway", 14, "underline"))
        register_label.pack(pady=10)

        # Bouton d'inscription
        register_button = tk.Button(center_frame, text="Inscrivez-vous", font=("broadway", 12), command=self.register)
        register_button.pack(pady=5)

        visit_label = tk.Label(center_frame, text="Visiter le site en tant qu'invité", font=("broadway", 14, "underline"))
        visit_label.pack(pady=20)

        # Bouton de visite sans connexion (discret)
        visit_button = tk.Button(center_frame, text="Visiter", font=("broadway", 12, "italic"), command=self.visit_as_guest)
        visit_button.pack(pady=10)

    def login(self):
        # Ajoutez ici le code pour gérer la connexion à un compte utilisateur.
        pass

    def register(self):
        # Ajoutez ici le code pour gérer le processus d'inscription.
        pass

    def visit_as_guest(self):
        # Ajoutez ici le code pour permettre aux utilisateurs de visiter le site sans connexion.
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightReservationApp(root)
    root.mainloop()
