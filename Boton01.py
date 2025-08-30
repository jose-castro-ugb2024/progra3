import tkinter as tk

class Aplicacion:
    def __init__(self):

        self.ventana01 = tk.Tk()
        self.valor=1
        self.ventana01.title("Botones")
        self.ventana01.geometry("600x400")


        self.valor = self.valor + 1
        self.label01.config(text=self.valor)


        self.label01= tk.Label(self.ventana01, text=self.valor)
        self.label01.grid(column=0, row=1)
        self.label01.configure(foreground= "blue")

        self.Boton01=tk.Button(self.ventana01, text="sumar", command=self.sumar)
        self.label01.grid(column=0, row=2)
        self.ventana01.mainloop()



def sumar(self):
            self.valor=self.valor+1
            self.label01.config(text=self.valor)

ejecutar =Aplicacion()




