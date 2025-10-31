import tkinter as tk
from tkinter import ttk, messagebox as mb

from docutils.nodes import title

import Libros

class formulariolibros:
    def __init__(self):
        self.libro1 = Libros.Libros()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Libros")
        self.cuaderno = ttk.Notebook(self.ventana)

        # Crear pestañas
        self.crear_pestaña_insertar()
        self.crear_pestaña_seleccionar()
        self.crear_pestaña_Actualizar()
        self.crear_pestaña_eliminar()

        self.cuaderno.grid(column=0, row=0, padx=10, pady=10)
        self.ventana.mainloop()

    # Pestaña Insertar
    def crear_pestaña_insertar(self):
        pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pagina, text="Insertar")

        labelframe = ttk.LabelFrame(pagina, text="Nuevo Libro")
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(labelframe, text="Titulo:").grid(column=0, row=0, padx=4, pady=4)
        self.titulo_insertar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.titulo_insertar).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(labelframe, text="Autor:").grid(column=0, row=1, padx=4, pady=4)
        self.autor_insertar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.autor_insertar).grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(labelframe, text="Publicacion:").grid(column=0, row=2, padx=4, pady=4)
        self.publicacion_insertar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.publicacion_insertar).grid(column=1, row=2, padx=4, pady=4)

        ttk.Label(labelframe, text="Precio:").grid(column=0, row=3, padx=4, pady=4)
        self.precio_insertar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.precio_insertar).grid(column=1, row=3, padx=4, pady=4)

        ttk.Button(labelframe, text="Guardar", command=self.agregar_libro).grid(column=1, row=4, padx=4, pady=4)

    def agregar_libro(self):
        title = self.titulo_insertar.get()
        author = self.autor_insertar.get()
        publication = self.publicacion_insertar.get()
        price = self.precio_insertar.get()
        if not title or not author:
            mb.showwarning("Advertencia", "Debe completar todos los campos")
            return
        if not publication or not price:
            mb.showwarning("Advertencia", "Debe completar todos los campos")
            return
        try:
            self.libro1.insertar((title, author, publication, price))
            mb.showinfo("Información", "Libro agregado correctamente")
            self.titulo_insertar.set("")
            self.autor_insertar.set("")
            self.publicacion_insertar.set("")
            self.precio_insertar.set("")
        except Exception as e:
            mb.showerror("Error", f"No se pudo agregar el libro:\n{e}")

    # Pestaña Consultar
    def crear_pestaña_seleccionar(self):
        pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pagina, text="Seleccionar")

        labelframe = ttk.LabelFrame(pagina, text="Buscar Libro por ID")
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(labelframe, text="ID Libro:").grid(column=0, row=0, padx=4, pady=4)
        self.id_consulta = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.id_consulta).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(labelframe, text="Titulo:").grid(column=0, row=1, padx=4, pady=4)
        self.titulo_seleccionar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.titulo_seleccionar).grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(labelframe, text="Autor:").grid(column=0, row=2, padx=4, pady=4)
        self.autor_seleccionar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.autor_seleccionar).grid(column=1, row=2, padx=4, pady=4)

        ttk.Label(labelframe, text="Publicacion:").grid(column=0, row=3, padx=4, pady=4)
        self.publicacion_seleccionar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.publicacion_seleccionar).grid(column=1, row=3, padx=4, pady=4)

        ttk.Label(labelframe, text="Precio:").grid(column=0, row=4, padx=4, pady=4)
        self.precio_seleccionar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.precio_seleccionar).grid(column=1, row=4, padx=4, pady=4)

        ttk.Button(labelframe, text="Seleccionar", command=self.seleccionar_libro).grid(column=1, row=5, padx=4, pady=4)

    def seleccionar_libro(self):
        codigo = self.id_consulta.get()
        if not codigo:
            mb.showwarning("Advertencia", "Debe ingresar un ID")
            return
        try:
            resultado = self.libro1.seleccionar((codigo,))
            if resultado:
                self.titulo_seleccionar.set(resultado[0][0])
                self.autor_seleccionar.set(resultado[0][1])
                self.publicacion_seleccionar.set(resultado[0][2])
                self.precio_seleccionar.set(resultado[0][3])
            else:
                self.titulo_seleccionar.set("")
                self.autor_seleccionar.set("")
                self.publicacion_seleccionar.set("")
                self.precio_seleccionar.set("")
                mb.showinfo("Información", "No existe un libro con ese ID")
        except Exception as e:
            mb.showerror("Error", f"No se pudo consultar:\n{e}")

    # Pestaña Modificar
    def crear_pestaña_Actualizar(self):
        pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pagina, text="Actualizar")

        labelframe = ttk.LabelFrame(pagina, text="Actualizar libro")
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(labelframe, text="ID libro:").grid(column=0, row=0, padx=4, pady=4)
        self.id_mod = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.id_mod).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(labelframe, text="Nuevo titulo:").grid(column=0, row=1, padx=4, pady=4)
        self.titulo_mod = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.titulo_mod).grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(labelframe, text="Nuevo autor:").grid(column=0, row=2, padx=4, pady=4)
        self.autor_mod = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.autor_mod).grid(column=1, row=2, padx=4, pady=4)

        ttk.Label(labelframe, text="Nueva publicacion:").grid(column=0, row=3, padx=4, pady=4)
        self.publicacion_mod = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.publicacion_mod).grid(column=1, row=3, padx=4, pady=4)

        ttk.Label(labelframe, text="Nuevo precio:").grid(column=0, row=4, padx=4, pady=4)
        self.precio_mod = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.precio_mod).grid(column=1, row=4, padx=4, pady=4)

        ttk.Button(labelframe, text="Actualizar", command=self.actualizar_libro).grid(column=1, row=5, padx=4, pady=4)

    def actualizar_libro(self):
        codigo = self.id_mod.get()
        title = self.titulo_mod.get()
        autor = self.autor_mod.get()
        publicacion = self.publicacion_mod.get()
        precio = self.precio_mod.get()
        if not codigo or not title or not autor:
            mb.showwarning("Advertencia", "Debe completar todos los campos")
            return
        if not codigo or not publicacion or not precio:
            mb.showwarning("Advertencia", "Debe completar todos los campos")
            return
        try:
            cant = self.libro1.Actualizar((title, autor, publicacion, precio, codigo))
            if cant == 1:
                mb.showinfo("Información", "Libro modificado correctamente")
            else:
                mb.showinfo("Información", "No existe un libro con ese ID")
        except Exception as e:
            mb.showerror("Error", f"No se pudo modificar el libro:\n{e}")

    # Pestaña Borrar
    def crear_pestaña_eliminar(self):
        pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pagina, text="Borrar")

        labelframe = ttk.LabelFrame(pagina, text="Eliminar empleado")
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(labelframe, text="ID Empleado:").grid(column=0, row=0, padx=4, pady=4)
        self.id_borrar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.id_borrar).grid(column=1, row=0, padx=4, pady=4)

        ttk.Button(labelframe, text="Eliminar", command=self.eliminar_libro).grid(column=1, row=1, padx=4, pady=4)

    def eliminar_libro(self):
        codigo = self.id_borrar.get()
        if not codigo:
            mb.showwarning("Advertencia", "Debe ingresar un ID")
            return
        try:
            cant = self.libro1.eliminar((codigo,))
            if cant == 1:
                mb.showinfo("Información", "Empleado eliminado correctamente")
            else:
                mb.showinfo("Información", "No existe un empleado con ese ID")
        except Exception as e:
            mb.showerror("Error", f"No se pudo eliminar el empleado:\n{e}")


if __name__ == "__main__":
    formulariolibros()