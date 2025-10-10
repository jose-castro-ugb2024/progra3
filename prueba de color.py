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

# Estilo para botones
style.configure("button.TButton", background="#E4E2E2", foreground="#000")
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="Cambiar color", style="button.TButton")
button.place(x=178, y=170, width=144, height=37)

radio_button_var = tk.IntVar()

# Colores para cada radio button
colors = {
    0: "#73D0BB",  # Verde claro
    1: "#FF0000",  # Rojo
    2: "#0000FF"   # Azul
}

# Crear estilos para cada radio button con su color de texto
for val, color in colors.items():
    style_name = f"radio_button_{val}.TRadiobutton"
    style.configure(style_name, background="#C7C8CAmysql-", foreground=color)
    style.map(style_name, background=[("active", "#E4E2E2")], foreground=[("active", color)])

# Crear radio buttons con estilos personalizados
radio_button_0 = ttk.Radiobutton(master=main, variable=radio_button_var, text="verde claro", value=0, style="radio_button_0.TRadiobutton")
radio_button_0.place(x=288, y=37)

radio_button_1 = ttk.Radiobutton(master=main, variable=radio_button_var, text="Rojo", value=1, style="radio_button_1.TRadiobutton")
radio_button_1.place(x=288, y=61)

radio_button_2 = ttk.Radiobutton(master=main, variable=radio_button_var, text="Azul", value=2, style="radio_button_2.TRadiobutton")
radio_button_2.place(x=288, y=85)

# Función para cambiar el color de fondo según el radio button seleccionado
def cambiar_color():
    selected_value = radio_button_var.get()
    color_seleccionado = colors.get(selected_value, "#C7C8CA")
    main.config(bg=color_seleccionado)

button.config(command=cambiar_color)

style.configure("button1.TButton", background="#C7C8CA", foreground="#000")
style.map("button1.TButton", background=[("active", "#C7C8CA")], foreground=[("active", "#000")])

button1 = ttk.Button(master=main, text="Salir", style="button1.TButton", command=main.destroy)
button1.place(x=414, y=170, width=80, height=40)

main.mainloop()
