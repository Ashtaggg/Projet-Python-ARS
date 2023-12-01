import tkinter as tk
from tkinter import ttk
import initialization
import query
import customer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime



def returnAdmin(Customer, canvas, figure, figure2):
    canvas.delete("all")
    canvas.destroy()

    plt.close(figure)
    plt.close(figure2)

    customer.customer.customer_page(Customer)




def nbrBooking(canvas):
    request = "SELECT DATE(`Timestamp`) AS BookingDate, COUNT(*) FROM `booking` GROUP BY BookingDate;"
    output = query.requestDataBase(request)

    dates = []
    numberOfBookings = []

    for i in output:
        dates.append(i[0])
        numberOfBookings.append(i[1])

    maxNumber = max(numberOfBookings)


    """for i in range(len(dates)):
        dates[i] = dates[i].strftime('%m-%d')"""


    figure, courbe = plt.subplots(figsize=(5, 4), facecolor=initialization.bg_color)
    courbe.bar(dates, numberOfBookings, color='black')

    plt.xticks(rotation=70)
    plt.subplots_adjust(left=0.15, bottom=0.35, right=0.95, top=0.90)
    courbe.xaxis.set_label_coords(0.5, -0.50)
    courbe.yaxis.set_label_coords(-0.080, 0.5)

    figure_canva = FigureCanvasTkAgg(figure, master=canvas)
    figure2_canva = figure_canva.get_tk_widget()
    figure2_canva.place(x=50, y=250)

    plt.ylim(0, maxNumber + 5)
    plt.xlabel("Date", fontdict={'fontname': 'Arial', 'fontsize': 14, 'fontweight': 'bold'})
    plt.ylabel("Number of Bookings", fontdict={'fontname': 'Arial', 'fontsize': 14, 'fontweight': 'bold'})
    plt.title("Bookings analysis", fontdict={'fontname': 'Arial', 'fontsize': 18, 'fontweight': 'bold'})

    return figure




def nbrFlight(canvas):
    request = "SELECT ArrivalCity, COUNT(*) FROM flight GROUP BY ArrivalCity;"
    output = query.requestDataBase(request)

    destination = []
    numberOfFlights = []

    for i in output:
        destination.append(i[0])
        numberOfFlights.append(i[1])

    maxNumber = max(numberOfFlights)


    figure, courbe = plt.subplots(figsize=(9, 4), facecolor=initialization.bg_color)
    courbe.bar(destination, numberOfFlights, color='black')
    
    plt.xticks(rotation=70)
    plt.subplots_adjust(left=0.1, bottom=0.35, right=0.95, top=0.90)
    courbe.xaxis.set_label_coords(0.5, -0.50)
    courbe.yaxis.set_label_coords(-0.055, 0.5)

    figure_canva = FigureCanvasTkAgg(figure, master=canvas)
    figure2_canva = figure_canva.get_tk_widget()
    figure2_canva.place(x=575, y=250)

    plt.ylim(0, maxNumber + 5)
    plt.xlabel("Destination", fontdict={'fontname': 'Arial', 'fontsize': 14, 'fontweight': 'bold'})
    plt.ylabel("Number of Flights", fontdict={'fontname': 'Arial', 'fontsize': 14, 'fontweight': 'bold'})
    plt.title("Flights analysis", fontdict={'fontname': 'Arial', 'fontsize': 18, 'fontweight': 'bold'})

    return figure





def stat_page(Customer):
    canvas = tk.Canvas(initialization.cuicui, width=1920, height=1080,bg=initialization.bg_color)
    canvas.place(x=0, y=0)
    canvas.create_line(0, 0, 1920, 0, width=150, fill="black")

    Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font = ('Helvetica' , 30, 'bold'), fg="white", bg="black")
    Cuicui.place(x=50, y=15)


    Title = tk.Label(text="Statistics",font = ('Helvetica' , 30, 'bold'),bg=initialization.bg_color)
    Title.place(x=700, y=100)

    returnTo = tk.Label(text="<",font = ('Helvetica' , 22, 'bold'),bg=initialization.bg_color)
    returnTo.place(x=50, y=100)
    returnTo.bind("<Button-1>", lambda event=None:returnAdmin(Customer, canvas, figure, figure2))


    figure = nbrBooking(canvas)
    figure2 = nbrFlight(canvas)