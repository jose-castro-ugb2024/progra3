print ("________________________________________________")
print("Lista - Sumar todos")
print ("________________________________________________")
#solicitar un numero final de la lista
num1=int(input("Ingrese un numero hasta 100:"     ))

#crea la lista desde el 1 hasta el $num1
recado = list(range(1, num1+1))

#Calcular la suma
resultado=sum(recado)

#imprimir el resultado
print(f"la suma de la lista {num1} es {resultado}  " )

