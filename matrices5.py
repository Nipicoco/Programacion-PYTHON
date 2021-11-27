'''
Genere una matriz de 4 x 7 donde 4 es el número de semanas de un mes y 7 es el número de días durante la semana. La matriz será rellenada con números enteros aleatorios entre 2 y 32, este número indicará la temperatura que hubo durante el día, La columna 0 representa el día lunes, la columna 1 representa el día martes así sucesivamente
'''
from random import randint as r

matrix = []
#almacenamos la matriz
print("Nuestra matriz quedaría de la siguiente manera: ")
for x in range(0, 4):
    list = []
    for z in range(0, 7):
        number = r(2, 32)
        list.append(number)
    matrix.append(list)
#printearemos la matriz
for y in range(len(matrix)):
    for e in range(len(matrix[y])):
        print(matrix[y][e],end=("  "))
    print()
b = len(matrix)
f = len(matrix[0])
max = 0
for i in range(0, b):
    for j in range(0, f):
        if matrix[i][j] > max:
            max = matrix[i][j]
#printearemos la temperatura mas alta
print("En el rango semanal, la temperatura mas alta fue de" ,max, "grados")
print("")
min = matrix[0][0]
for i in range(len(matrix)):#tabeamos la matriz
    for j in range(len(matrix[i])):
        if matrix[i][j] < min:
            min = matrix[i][j]
print("En el rango semanal, la temperatura mas baja fue de" ,min, "grados")#primnteamos la temperatura mas baja
print("")

prom = []
for i in range(len(matrix)):
    temp = 0
    for j in range(len(matrix[i])):
        temp += matrix[i][j]
    prom.append(temp)#tabeamos el promedio
for i in range(len(prom)):
    redon = round(prom[i]/7, 1)
    prom[i] = redon
print("Los promedios por semana son de:" ,prom,)