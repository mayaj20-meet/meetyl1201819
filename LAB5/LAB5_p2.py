
import tkinter as tk
from tkinter import simpledialog


year == int(simpledialog.askstring("input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

if year <= 1900:
    print ("Woah, that's the past!")

if year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")

