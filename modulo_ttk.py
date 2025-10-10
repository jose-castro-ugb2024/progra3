# This code is generated using PyUIbuilder: https://pyuibuilder.com
import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Controles TTk")
main.config(bg="#E4E2E2")
main.geometry("700x400")

style = ttk.Style(main)
style.theme_use("clam")

style.configure("label.TLabel", background="#fff8f8", foreground="#000")
label = ttk.Label(master=main, text="0", style="label.TLabel")
label.place(x=283, y=21, width=203, height=43)

style.configure("button1.TButton", background="#E4E2E2", foreground="#000"),
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button1 = ttk.Button(master=main, text="Incrementar",  command= lambda:Aumentar(), style="button1.TButton")
button1.place(x=339, y=91, width=80, height=40)

style.configure("button2.TButton", background="#E4E2E2", foreground="#000")
style.map("button2.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button2 = ttk.Button(master=main, command= lambda: Disminuir(), text="Disminuir", style="button2.TButton")
button2.place(x=341, y=149, width=80, height=40)

style.configure("button3.TButton", background="#E4E2E2", foreground="#000")
style.map("button3.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button3 = ttk.Button(master=main, text="Salir", style="button3.TButton", command= lambda: salir())
button3.place(x=344, y=216, width=80, height=40)



def Aumentar():
            valor = int(label.cget("text"))
            valor = valor +1
            label.configure(text=valor)

def Disminuir():
            valor = int(label.cget("text"))
            valor = valor -1
            label.configure(text=valor)

def salir():
    exit()

main.mainloop()


            






