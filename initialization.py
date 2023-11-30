import tkinter as tk
import customer


cuicui = tk.Tk()
cuicui.title("Cuicui")
cuicui.geometry("1920x1080")

cuicui.columnconfigure(0, weight=1)
cuicui.columnconfigure(1, weight=1)
cuicui.columnconfigure(2, weight=1)
cuicui.columnconfigure(3, weight=1)
cuicui.columnconfigure(4, weight=1)

"""
cuicui.rowconfigure(0, weight=2)
cuicui.rowconfigure(1, weight=1)
cuicui.rowconfigure(2, weight=1)
cuicui.rowconfigure(3, weight=1)
cuicui.rowconfigure(4, weight=1)
"""


member = customer.customer(0, 0, 0, 0, 0, 0, 0, 0)
login = 0
lastPage = ""
<<<<<<< HEAD
bg_color = "#9B9B9B"
=======
FlightID = 0
>>>>>>> 6def03d0a0e54c2bfa55fc9b931cb95a6cc89aac
