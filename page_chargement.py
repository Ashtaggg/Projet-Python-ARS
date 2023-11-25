
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import query
import random




import initialization
import page_accueil


def chargement():
    print("ENTER THE FUNCTION")
    initialization.cuicui.title("Welcome Page")
    print("WELCOME PAGE")
    canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080)
    canvas.place(x=0, y=0)
    canvas.create_line(0, 0, 1920, 0, width=150, fill="black")

    Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white",bg="black")
    Cuicui.place(x=50, y=15)

    titre_label = tk.Label(initialization.cuicui, text="Welcome on Cuicui Airlines", font=("Broadway", 30))
    titre_label.place(x=400, y=90)
    cities = ["amsterdam","barcelona","berlin","chicago","denver","houston","las_vegas","lisbon","london","los_angeles","madrid","miami","paris","rome","san_fransisco"]
    print("CHARGEMENT PAGE")
    print_chargement(canvas,cities)
    #show_image(canvas)
    initialization.cuicui.mainloop()




    #page_accueil.CuicuiAirlinesApp.welcome_page(initialization.cuicui)

def print_chargement(canvas,cities):
    canvas.create_rectangle(198, 598, 1367, 652, outline='black', fill='blue')
    canvas.update()
    photo = show_image_loading(canvas, "paris")
    for i in range(1, 101):
        print(f"Chargement... [{i}%]")
        loading = tk.Label( text=f"Loading... [{i}%]", font=("Helvetica", 32))
        loading.place(x=200,y=300)
        if(i%5 == 0):
            print("I = ",i)
            show_image(canvas,int(i))
            #canvas.update()
            if(i%10 == 0):
                city = random.choice(cities)
                print("CITY BEFORE SHOW IMAGE",city)
                #photo = (
                show_image_loading(canvas,city)

            canvas.update()
        #initialization.cuicui.update_idletasks()


        time.sleep(0.05)

    print("Chargement terminé!")


def show_image(canvas,i):

    i=int(i/5)
    print("image ", i)

    img = Image.open(f"photos/other_photos/green_rectangles/green_rectangle_{i}.png")

    #print(img)
    img = img.resize((25, 50), Image.LANCZOS)  # , Image.ANTIALIAS) 750 500

    photo = ImageTk.PhotoImage(img)
    canvas.create_image(140 + 60*i, 600, anchor=tk.NW, image=photo)
    canvas.pack()
    canvas.image = photo
    #photo = ImageTk.PhotoImage(img)
    #print(photo)
    #canvas.create_image(100, 100, anchor=tk.NW, image=photo)

    #time.sleep(0.01)

def show_image_loading(canvas,city):
    print("CITY : ",city)
    img = Image.open(f"photos/search_city/{city}.jpg")

    img = img.resize((500, 350), Image.LANCZOS)  # , Image.ANTIALIAS) 750 500

    # img = img.resize(500, 500)  # Redimensionnement de l'image
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(710, 225, anchor=tk.NW, image=photo)
    canvas.pack()
    canvas.image = photo

    #return photo




if __name__ == "__main__":
    #app = ( )
    print("MAIN CODE")
    chargement()#initialization.cuicui)