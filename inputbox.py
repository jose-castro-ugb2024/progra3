import tkinter


class Aplicacion:
    def __init__(self):
        self.formulario01= tkinter.Tk()
        self.formulario01.title("Operaciones")

        self.label01= tkinter.label(self.formulario01, text="Ingrese el numero: ")
        self.label01.grid(column=0, row=0)

        self.dato01=tkinter.StringVar()
        self.entry01 = tkinter.Entry(self.formulario01, width=10,textvariable=self.dato01)

        self.boton01=tkinter.Button(self.formulario01, text="Calcular", command=self.calcular)

        self.boton01.grid(column=0, row=2)

        self.label02=tkinter.Label(self.formulario01, text="Resultado: ")
        self.label02.grid(column=0, row=3)

    def calcular(self):
        valor= int(self.dato01.get())
        cuadrado= valor*valor
        self.label02.configure(text=cuadrado)

        self.formulario01.mainloop()

ejecutar = Aplicacion()

