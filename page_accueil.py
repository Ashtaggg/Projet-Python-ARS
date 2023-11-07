from initialization import cuicui
import tkinter as tk
from PIL import Image, ImageTk


# Crée un libellé pour le titre de la page d'accueil
titre_label = tk.Label(cuicui, text="Welcome on Cuicui Airlines", font=("Helvetica", 24))
titre_label.pack(pady=20)


image = Image.open('./photos/photo_airport_01.jpeg')

photo = ImageTk.PhotoImage(image)

label = tk.Label(cuicui, image=photo)
label.pack()



# Lance la boucle principale de l'application
cuicui.mainloop()

