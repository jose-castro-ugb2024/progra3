def comparar_numero(num1):
    #ver si el numero es negativo, positivo o cero
    if num1 > 0:
        return"El numero es positivo."
    elif num1 < 0:
        return"El numero es negativo."
    else:
        return " El numero es 0."

num1=int(input("Introduce el numero primero para verificar:  "))
print(comparar_numero(num1))