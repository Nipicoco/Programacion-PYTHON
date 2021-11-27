'''
Genera una matriz de 5 x 5 con números enteros aleatorios entre -10 a 10, imprime por pantalla la matriz y luego muestra por pantalla la matriz transpuesta de la matriz que acabas de generar
'''
from random import randint as r
matrix=[]   
n=5
m=5
#definimos n y m como 5 para usarlos en la operacion
print("\nLa matriz sería: \n")
for n in range(0, n):
    listado = []
    for i in range(0, m):
        random = r(-10,10)
        listado.append(random)
    matrix.append(listado)
#Printeamos la matriz

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        print(matrix[y][x],end=("  ")) 
    print()

print("\nLa matriz dada vuelta sería: \n")
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        print(matrix[x][y],end=("  ")) 
    print() 
