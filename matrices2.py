"""Genera 2 matrices de tamaño N x M con números random(positivos y negativos) entre -10 a 10, donde N y M
se deben solicitar al usuario. Luego realiza la operación de suma de matrices."""
from random import randint as r

matrix = []
matriz2 = []
suma = []
#Almacen de valores
n = int(input("N: "))
m = int(input("M: "))
#Pidiendo N y M
for x in range(n):
    list = []
    for y in range(m):
        nat = r(-10,10)
        list.append(nat)
    matrix.append(list)
#Printeando la primera matriz
print('\nLa primera matriz seria:')

for y in range(len(matrix)):
    for e in range(len(matrix[y])):
        print(matrix[y][e],end=("  "))
    print()

for x in range(n):
    list = []
    for y in range(m):
        nat = r(-10,10)
        list.append(nat)
    matriz2.append(list)
#Printeando la segunda matriz
print('\nLa segunda matriz seria:')

for y in range(len(matriz2)):
    for e in range(len(matriz2[y])):
        print(matriz2[y][e],end=("  "))
    print()


for a in range(len(matrix)):
    list = []
    for b in range(len(matrix[a])):
        list.append(matrix[a][b]+matriz2[a][b])
    suma.append(list)
#Printearemos la matriz sumada. tabeandola con range len  al igual que las demas matrices
print('\nLa matriz sumada seria la siguiente:')

for y in range(len(suma)):
    for e in range(len(suma[y])):
        print(suma[y][e],end=("  "))
    print()

