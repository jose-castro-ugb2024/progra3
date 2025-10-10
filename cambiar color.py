# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Cambiar color")
main.config(bg="#E4E2E2")
main.geometry("700x400")


style = ttk.Style(main)
style.theme_use("clam")

style.configure("button.TButton", background="#E4E2E2", foreground="#000")
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="Cambiar color", style="button.TButton")
button.place(x=178, y=170, width=144, height=37)

radio_button_var = tk.IntVar()
style.configure("radio_button.TRadiobutton", background="#E4E2E2", foreground="#000")
style.map("radio_button.TRadiobutton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])


radio_button_0 = ttk.Radiobutton(master=main, variable=radio_button_var, text="Amarrillo", value=0, style="radio_button.TRadiobutton")
radio_button_0.place(x=288, y=37)


radio_button_1 = ttk.Radiobutton(master=main, variable=radio_button_var, text="Rojo", value=1, style="radio_button.TRadiobutton")
radio_button_1.place(x=288, y=61)


radio_button_2 = ttk.Radiobutton(master=main, variable=radio_button_var, text="Azul", value=2, style="radio_button.TRadiobutton")
radio_button_2.place(x=288, y=85)

style.configure("button1.TButton", background="#E4E2E2", foreground="#000")
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button1 = ttk.Button(master=main, text="Salir", style="button1.TButton")
button1.place(x=414, y=170, width=80, height=40)


main.mainloop()