print("A continuación deberá ingresar 10 números")
numero_1 = int(input("Ingrese un número"))
numero_2 = int(input("Ingrese un número"))
numero_3 = int(input("Ingrese un número"))
numero_4 = int(input("Ingrese un número"))
numero_5 = int(input("Ingrese un número"))
numero_6 = int(input("Ingrese un número"))
numero_7 = int(input("Ingrese un número"))
numero_8 = int(input("Ingrese un número"))
numero_9 = int(input("Ingrese un número"))
numero_10 = int(input("Ingrese un número"))

numeros_usuario = [numero_1, numero_2, numero_3, numero_4, numero_5, numero_6, numero_7, numero_8, numero_9, numero_10]

print(sum(numeros_usuario), "suma de los numeros elegidos")

numero_11 = int(input("Ingrese un numero mas"))

import numpy as np

numeros_usuario = np.array(
    [numero_1, numero_2, numero_3, numero_4, numero_5, numero_6, numero_7, numero_8, numero_9, numero_10])

print(numeros_usuario * numero_11)

print(min(numeros_usuario), " Numero mas pequeño de la lista")  # Valor mas pequeño

print(max(numeros_usuario), "numero mas grande de la lista")  # Valor mas grande

a = -np.sort(-numeros_usuario)
print(a)

promedio_lista = (sum(numeros_usuario) / 10)  # Promedio de la lista
print(promedio_lista)

print("Por favor ingrese 10 numeros mas")
numero_11 = int(input("Ingrese un numero"))
numero_12 = int(input("Ingrese un numero"))
numero_13 = int(input("Ingrese un numero"))
numero_14 = int(input("Ingrese un numero"))
numero_15 = int(input("Ingrese un numero"))
numero_16 = int(input("Ingrese un numero"))
numero_17 = int(input("Ingrese un numero"))
numero_18 = int(input("Ingrese un numero"))
numero_19 = int(input("Ingrese un numero"))
numero_20 = int(input("Ingrese un numero"))

numeros_usuario_2 = [numero_11, numero_12, numero_13, numero_14, numero_15, numero_16, numero_17, numero_18, numero_19,
                     numero_20]

print(numeros_usuario + numeros_usuario_2)


def printRepetidos(numeros_usuario, tamano):
    print("Los numeros que se repiten dentro de la lista son: ",
          end=' ')
    for i in range(0, tamano - 1):
        for j in range(i + 1, tamano):
            if numeros_usuario[i] == numeros_usuario[j]:
                print(numeros_usuario[i], end=' , ')


numeros_usuario = [numero_1, numero_2, numero_3, numero_4, numero_5, numero_6, numero_7, numero_8, numero_9, numero_10]

numeros_usuario_tamano = len(numeros_usuario)
printRepetidos(numeros_usuario, numeros_usuario_tamano)
