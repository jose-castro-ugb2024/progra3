import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.geometry('600x400')
        self.ventana1.title("Suma de dos números")

        # Primer número
        self.label1 = tk.Label(self.ventana1, text="Ingrese el primer número:")
        self.label1.grid(column=0, row=0)

        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        # Segundo número
        self.label2 = tk.Label(self.ventana1, text="Ingrese el segundo número:")
        self.label2.grid(column=0, row=1)

        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)

        # Botón para calcular suma
        self.boton1 = tk.Button(self.ventana1, text="Sumar", command=self.calcular)
        self.boton1.grid(column=0, row=2)

        # Resultado
        self.label_resultado = tk.Label(self.ventana1, text="Resultado:")
        self.label_resultado.grid(column=0, row=3, columnspan=2)

        self.ventana1.mainloop()

    def calcular(self):
        try:
            valor1 = int(self.dato1.get())
            valor2 = int(self.dato2.get())
            suma = valor1 + valor2
            self.label_resultado.configure(text=f"Resultado: {suma}")
        except ValueError:
            self.label_resultado.configure(text="Por favor ingrese números válidos.")

aplicacion1 = Aplicacion()




