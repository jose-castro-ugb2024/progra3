def calcular_promedio(lab1, lab2, parcial):

    nota_final = (lab1 * 0.30) + (lab2 * 0.30) + (parcial * 0.40)
    return nota_final


print("___ Calculadora de Promedio ___")
lab1 = float(input("Ingresa la nota del Laboratorio 1 (0 - 10): "))
lab2 = float(input("Ingresa la nota del Laboratorio 2 (0 - 10): "))
parcial = float(input("Ingresa la nota del Parcial (0 - 10): "))

promedio = calcular_promedio(lab1, lab2, parcial)
print(f"Tu nota")
