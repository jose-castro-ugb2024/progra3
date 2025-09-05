#crear una app que calcule cuantos años tienes

from datetime import date

def calcular_edad(dia, mes, año):
    hoy = date.today()
    edad = hoy.year-año

    # Arreglar si aún no ha pasado tu cumpleaños
    if (hoy.month, hoy.day) < (mes, dia):
        edad -= 1

    return edad

#el calculo de la edad con tu dia, mes y año
print("=== Calculadora de Edad ===")
dia = int(input("Ingresa tu día de nacimiento: "))
mes = int(input("Ingresa tu mes de nacimiento (número): "))
año = int(input("Ingresa tu año de nacimiento: "))

edad = calcular_edad(dia, mes, año)
print(f"Tienes {edad} años.")

