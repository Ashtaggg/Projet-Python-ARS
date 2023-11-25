import tkinter as tk
from tkinter import simpledialog, messagebox
import initialization
import effacer




def process_payment(main_window, passenger_list):
    effacer.effacer_page()
    canvas = tk.Canvas(initialization.cuicui, width=1600, height=1000)
    canvas.place(x=0, y=0)
    canvas.create_line(0, 0, 1920, 0, width=150, fill="black")
    #canvas.create_line(775, 220, 775, 700, width=2, fill="black")

    Cuicui = tk.Label(initialization.cuicui, text="Cuicui Airline", font=('Helvetica', 30, 'bold'), fg="white", bg="black")
    Cuicui.place(x=50, y=15)

    #payment_page = tk.Toplevel(main_window)
    #payment_page.title("Payment Process")

    payment_label = tk.Label(text="Payment Information", font=("Helvetica", 25, "bold"))
    payment_label.place(x=600,y=175)
    #payment_label.pack()

    card_label = tk.Label(canvas, text="Card Number", font=("Helvetica", 11, "bold"))
    card_label.place(x=710,y=225)
    card_entry = tk.Entry(canvas, show="*")
    card_entry.place(x=700,y=250)
   # card_label.pack()
   # card_entry.pack()

    expiry_label = tk.Label(canvas, text="Expiration Date (MM/YY)", font=("Helvetica", 11, "bold"))
    expiry_label.place(x=675,y=275)
    expiry_entry = tk.Entry(canvas)
    expiry_entry.place(x=700,y=300)
   # expiry_label.pack()
    #expiry_entry.pack()

    cvv_label = tk.Label(canvas, text="CVV", font=("Helvetica", 11, "bold"))
    cvv_label.place(x=740,y=325)
    cvv_entry = tk.Entry(canvas, show="*")
    cvv_entry.place(x=700,y=350)

   # cvv_label.pack()
   # cvv_entry.pack()
    pay_button = tk.Button(canvas, text="Pay", font=("Helvetica", 12, "bold"),command=lambda: validate_payment(card_entry.get(),expiry_entry.get(),cvv_entry.get(),canvas))
    pay_button.place(x=735,y=400)
    #pay_button.pack()

 
def validate_payment(card_entry,expiry_entry,cvv_entry,canvas):
    card_number = card_entry
    expiry_date = expiry_entry
    cvv = cvv_entry

    if len(card_number) == 16 and len(expiry_date) == 5 and len(cvv) == 3:
        messagebox.showinfo("Payment Successful", "Your payment has been processed successfully. Thank you!")
        canvas.destroy()
        #main_window.deiconify()
    else:
        messagebox.showerror("Payment Error", "Please check your payment information.")



def calculate_price(passenger_list):
    class_prices = {'Economy': 100, 'Premium': 200, 'Business': 300}
    age_coefficients = {'Children': 0.5, 'Regular': 1, 'Senior': 0.8}

    total_price = 0

    for passenger_details in passenger_list:
        class_price = class_prices.get(passenger_details['ticket_type'], 0)
        age_coefficient = age_coefficients.get(passenger_details['member_type'], 1)
        total_price += class_price * age_coefficient

    return total_price

if __name__ == "__main__":
   # CuicuiAirlinesApp.validdation_page(initialization.cuicui)
   #process_payment()
    pass  # Vous pouvez ajouter d'autres fonctionnalités ou tests si nécessaire
