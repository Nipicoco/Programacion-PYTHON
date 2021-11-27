'''Genera 2 matrices de tamaño N x M con números random(positivos y negativos) entre -10 a 10, donde N y M se deben solicitar al usuario.'''

from random import randint as r
matrix=[]
#primera matriz
matrix2=[]
#segunda matriz
sum = []
#matriz sumada
#Pidiendo inputs
n=int(input('Ingresar un numero:'))
#n
m=int(input('Ingresar un numero:'))
#m
for e in range(0, n):
    list = []
    for i in range(0, m):
        random = r(-10,10)
        list.append(random)
    matrix.append(list)

for e in range(0, n):
    list = []
    for i in range(0, m):
        random = r(0,5)
        list.append(random)
    matrix2.append(list)


print("La primera matriz seria:")
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        print(matrix[y][x],end=("  ")) 
    print() 
#Llamando a printear la primera matriz
print("La segunda matriz sería:")
for y in range(len(matrix2)):
    for x in range(len(matrix2[y])):
        print(matrix2[y][x],end=("  ")) 
    print() 
#Printeando la segunda matriz
for a in range(len(matrix)):
    lista = []
    for b in range(len(matrix[a])):
        lista.append(matrix[a][b]+matrix2[a][b])
    sum.append(lista)
#Aqui se llama a la suma de matrices, printeando.
print("Las matrices sumadas serían:")
for y in range(len(sum)):
    for x in range(len(sum[y])):
        print(sum[y][x],end=("  ")) 
    print() 