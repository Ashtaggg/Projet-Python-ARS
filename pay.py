# pay.py

import tkinter as tk
from tkinter import simpledialog, messagebox

import initialization

def process_payment(main_window, passenger_list):
    payment_page = tk.Toplevel(main_window)
    payment_page.title("Processus de Paiement")

    payment_label = tk.Label(payment_page, text="Veuillez saisir les informations de paiement :", font=("Broadway", 14))
    payment_label.pack()

    card_label = tk.Label(payment_page, text="Numéro de carte :", font=("Broadway", 12))
    card_entry = tk.Entry(payment_page, show="*")
    card_label.pack()
    card_entry.pack()

    expiry_label = tk.Label(payment_page, text="Date d'expiration (MM/YY) :", font=("Broadway", 12))
    expiry_entry = tk.Entry(payment_page)
    expiry_label.pack()
    expiry_entry.pack()

    cvv_label = tk.Label(payment_page, text="CVV :", font=("Broadway", 12))
    cvv_entry = tk.Entry(payment_page, show="*")
    cvv_label.pack()
    cvv_entry.pack()

    def validate_payment():
        card_number = card_entry.get()
        expiry_date = expiry_entry.get()
        cvv = cvv_entry.get()

        if len(card_number) == 16 and len(expiry_date) == 5 and len(cvv) == 3:
            messagebox.showinfo("Paiement réussi", "Votre paiement a été traité avec succès. Merci!")
            payment_page.destroy()
            main_window.deiconify()  # Redonne la visibilité à la fenêtre principale
        else:
            messagebox.showerror("Erreur de paiement", "Veuillez vérifier vos informations de paiement.")

    pay_button = tk.Button(payment_page, text="Payer", font=("Broadway", 14), command=validate_payment)
    pay_button.pack()

# Nouvelle fonction calculate_price
def calculate_price(passenger_list):
    # Prix par classe
    class_prices = {'Economy': 100, 'Premium': 200, 'Business': 300}

    # Coefficients par âge
    age_coefficients = {'children': 0.5, 'regular': 1, 'senior': 0.8}

    total_price = 0

    for passenger_details in passenger_list:
        class_price = class_prices.get(passenger_details['ticket_type'], 0)
        age_coefficient = age_coefficients.get(passenger_details['member_type'], 1)
        total_price += class_price * age_coefficient

    return total_price

# Appel de la fonction principale
if __name__ == "__main__":
    pass  # Ajoutez ici d'autres fonctionnalités ou tests si nécessaire
