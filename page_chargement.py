# Importation of all the librairy needed
import time
import tkinter as tk
from PIL import Image, ImageTk
import random

# Importation of all the files needed to run the program
import initialization
import page_accueil


def loading_screen():
    """
    This function is the main function of the program.
    The function creates the canvas on which all the loading elements will be displayed.
    """
    initialization.cuicui.title("Loading Page")  # Creation of the page

    # Creation of the canvas on which all the element will be displayed
    canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080,bg=initialization.bg_color)
    canvas.pack()
    # Coordinates  on which the top left corner of the canvas is
    canvas.place(x=0, y=0)
    # Creation of the black line behind the title
    canvas.create_line(0, 0, 1920, 0, width=150, fill="black")
    # Creation of the header text
    cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white",
                      bg="black")
    # Coordinates of the header text
    cuicui.place(x=50, y=15)

    # Creation of the title text
    tittle_label = tk.Label(initialization.cuicui, text="Welcome on Cuicui Airlines", font=("Broadway", 30),bg=initialization.bg_color)
    # Coordinates of the title text
    tittle_label.place(x=400, y=90)
    # List of the cities which have image to print on the loading screen
    cities = ["amsterdam", "barcelona", "berlin", "chicago", "denver", "houston", "las_vegas", "lisbon", "london",
              "los_angeles", "madrid", "miami", "paris", "rome", "san_fransisco"]

    # Function print_loading
    print_loading(canvas, cities)

    initialization.cuicui.mainloop()


def print_loading(canvas, cities):
    """
    This function print the images and loading bar on the canvas.
    :param canvas: canvas on which the element will be
    :param cities: list of the cities
    :return: nothing
    """
    # Creation of the bar of the loading screen
    canvas.create_rectangle(198, 598, 1367, 652, outline='black', fill='black')
    canvas.update()
    # Display of the first picture (with the function show_image_loading)
    photo_city = show_image_loading("paris")
    # Display of the first green rectangle (with the function show_image)
    photo_green = show_image()
    # Initialisation of the variable x

    list_green_rectangle = []

    # Loop with 99 iteration
    for i in range(1, 100):
        # Selection of a random city in the list of cities
        city = random.choice(cities)
        # Display of the loading percentage
        loading = tk.Label(text=f"Loading... [{i}%]", font=("Helvetica", 32),bg=initialization.bg_color)
        # Coordinate of the loading percentage
        loading.place(x=200, y=300)
        # A pause between each iteration
        time.sleep(0.05)
        # if the "i" is a multiple of 5
        if i % 5 == 0:
            # Call of the function photo_green for the next rectangle
            photo_green = show_image()

            list_green_rectangle.append(photo_green)
        # if the "i" is a multiple of 10
        if i % 10 == 0:
            # Call of the function photo_green for the next photo
            photo_city = show_image_loading(city)

        x = 140
        # Display of the next green rectangle
        for j in range(len(list_green_rectangle)):
            # Increase of the x coordinate
            x = 140 + 60 * (i / 5)
            canvas.create_image(x, 600, anchor=tk.NW, image=photo_green)
            canvas.pack()
            canvas.image = photo_green

        # Display of the next photo
        canvas.create_image(710, 225, anchor=tk.NW, image=photo_city)
        canvas.pack()
        canvas.image = photo_city

        # Updating the canvas to display the picture
        canvas.update()

    # Call of the welcome_page at the end of the loop (when the loading is at 100%)
    page_accueil.CuicuiAirlinesApp.welcome_page(initialization.cuicui)


def show_image():
    """
    This function return the correct green rectangle needed
    :return: green rectangle
    """
    # We divide "i" by 5
    # Opening of the green rectangle image
    img = Image.open(f"photos/other_photos/green_rectangles/green_rectangle_0.png")
    # Resize of the image
    img = img.resize((25, 50), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    # Return the new green rectangle
    return photo


def show_image_loading(city):
    """
    This function return the correct city picture needed
    :param city: The city needed
    :return: the photo of the city
    """
    # Opening of the city needed
    img = Image.open(f"photos/search_city/{city}.jpg")
    # Resize of the image
    img = img.resize((500, 350), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    # Return the photo of the city
    return photo


if __name__ == "__main__":
    loading_screen()
