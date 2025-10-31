import tkinter as tk
from tkinter import ttk, messagebox as mb
import Empleados

class FormularioEmpleados:
    def __init__(self):
        self.empleado1 = Empleados.Empleados()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Empleados")
        self.cuaderno = ttk.Notebook(self.ventana)

        # Crear pestañas
        self.crear_pestaña_insertar()
        self.crear_pestaña_consultar()
        self.crear_pestaña_modificar()
        self.crear_pestaña_borrar()

        self.cuaderno.grid(column=0, row=0, padx=10, pady=10)
        self.ventana.mainloop()

    # Pestaña Insertar
    def crear_pestaña_insertar(self):
        pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pagina, text="Insertar")

        labelframe = ttk.LabelFrame(pagina, text="Nuevo Empleado")
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(labelframe, text="Nombre:").grid(column=0, row=0, padx=4, pady=4)
        self.nombre_insertar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.nombre_insertar).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(labelframe, text="Cargo:").grid(column=0, row=1, padx=4, pady=4)
        self.cargo_insertar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.cargo_insertar).grid(column=1, row=1, padx=4, pady=4)

        ttk.Button(labelframe, text="Guardar", command=self.agregar_empleado).grid(column=1, row=2, padx=4, pady=4)

    def agregar_empleado(self):
        nombre = self.nombre_insertar.get()
        cargo = self.cargo_insertar.get()
        if not nombre or not cargo:
            mb.showwarning("Advertencia", "Debe completar todos los campos")
            return
        try:
            self.empleado1.alta((nombre, cargo))
            mb.showinfo("Información", "Empleado agregado correctamente")
            self.nombre_insertar.set("")
            self.cargo_insertar.set("")
        except Exception as e:
            mb.showerror("Error", f"No se pudo agregar el empleado:\n{e}")

    # Pestaña Consultar
    def crear_pestaña_consultar(self):
        pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pagina, text="Consultar")

        labelframe = ttk.LabelFrame(pagina, text="Buscar empleado por ID")
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(labelframe, text="ID Empleado:").grid(column=0, row=0, padx=4, pady=4)
        self.id_consulta = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.id_consulta).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(labelframe, text="Nombre:").grid(column=0, row=1, padx=4, pady=4)
        self.nombre_consulta = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.nombre_consulta, state="readonly").grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(labelframe, text="Cargo:").grid(column=0, row=2, padx=4, pady=4)
        self.cargo_consulta = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.cargo_consulta, state="readonly").grid(column=1, row=2, padx=4, pady=4)

        ttk.Button(labelframe, text="Consultar", command=self.consultar_empleado).grid(column=1, row=3, padx=4, pady=4)

    def consultar_empleado(self):
        codigo = self.id_consulta.get()
        if not codigo:
            mb.showwarning("Advertencia", "Debe ingresar un ID")
            return
        try:
            resultado = self.empleado1.consulta((codigo,))
            if resultado:
                self.nombre_consulta.set(resultado[0][0])
                self.cargo_consulta.set(resultado[0][1])
            else:
                self.nombre_consulta.set("")
                self.cargo_consulta.set("")
                mb.showinfo("Información", "No existe un empleado con ese ID")
        except Exception as e:
            mb.showerror("Error", f"No se pudo consultar:\n{e}")

    # Pestaña Modificar
    def crear_pestaña_modificar(self):
        pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pagina, text="Modificar")

        labelframe = ttk.LabelFrame(pagina, text="Actualizar empleado")
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(labelframe, text="ID Empleado:").grid(column=0, row=0, padx=4, pady=4)
        self.id_mod = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.id_mod).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(labelframe, text="Nuevo nombre:").grid(column=0, row=1, padx=4, pady=4)
        self.nombre_mod = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.nombre_mod).grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(labelframe, text="Nuevo cargo:").grid(column=0, row=2, padx=4, pady=4)
        self.cargo_mod = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.cargo_mod).grid(column=1, row=2, padx=4, pady=4)

        ttk.Button(labelframe, text="Actualizar", command=self.actualizar_empleado).grid(column=1, row=3, padx=4, pady=4)

    def actualizar_empleado(self):
        codigo = self.id_mod.get()
        nombre = self.nombre_mod.get()
        cargo = self.cargo_mod.get()
        if not codigo or not nombre or not cargo:
            mb.showwarning("Advertencia", "Debe completar todos los campos")
            return
        try:
            cant = self.empleado1.modificacion((nombre, cargo, codigo))
            if cant == 1:
                mb.showinfo("Información", "Empleado modificado correctamente")
            else:
                mb.showinfo("Información", "No existe un empleado con ese ID")
        except Exception as e:
            mb.showerror("Error", f"No se pudo modificar el empleado:\n{e}")

    # Pestaña Borrar
    def crear_pestaña_borrar(self):
        pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pagina, text="Borrar")

        labelframe = ttk.LabelFrame(pagina, text="Eliminar empleado")
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(labelframe, text="ID Empleado:").grid(column=0, row=0, padx=4, pady=4)
        self.id_borrar = tk.StringVar()
        ttk.Entry(labelframe, textvariable=self.id_borrar).grid(column=1, row=0, padx=4, pady=4)

        ttk.Button(labelframe, text="Eliminar", command=self.eliminar_empleado).grid(column=1, row=1, padx=4, pady=4)

    def eliminar_empleado(self):
        codigo = self.id_borrar.get()
        if not codigo:
            mb.showwarning("Advertencia", "Debe ingresar un ID")
            return
        try:
            cant = self.empleado1.baja((codigo,))
            if cant == 1:
                mb.showinfo("Información", "Empleado eliminado correctamente")
            else:
                mb.showinfo("Información", "No existe un empleado con ese ID")
        except Exception as e:
            mb.showerror("Error", f"No se pudo eliminar el empleado:\n{e}")


if __name__ == "__main__":
    FormularioEmpleados()
