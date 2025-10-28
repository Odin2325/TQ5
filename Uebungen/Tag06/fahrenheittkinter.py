import tkinter as tk
from tkinter import messagebox
 
def celsius_zu_fahrenheit():
    """Liest die Celsius-Eingabe, rechnet um und zeigt das Ergebnis an."""
    try:
 
        celsius_str = eingabe_celsius.get()

        celsius = float(celsius_str)

        fahrenheit = (celsius * 9.0 / 5) + 32

        ergebnis_text = f"↔️ {celsius}°C entspricht {round(fahrenheit, 2)}°F"
        label_ergebnis.config(text=ergebnis_text)
       
    except ValueError:
        messagebox.showerror("Fehler", "Ungültige Eingabe! Bitte gib eine Zahl ein.")
        label_ergebnis.config(text="Bitte Zahl eingeben.")
 
root = tk.Tk()
root.title("Celsius 🔄 Fahrenheit")
root.geometry("300x150")

label_prompt = tk.Label(root, text="Temperatur in Celsius (°C):")
label_prompt.pack(pady=5)
 
eingabe_celsius = tk.Entry(root, width=15)
eingabe_celsius.pack(pady=5)
 
button_umrechnen = tk.Button(root, text="Umrechnen", command=celsius_zu_fahrenheit)
button_umrechnen.pack(pady=5)
 
label_ergebnis = tk.Label(root, text="Ergebnis: Warten auf Eingabe...", fg="blue")
label_ergebnis.pack(pady=10)
 
root.mainloop()