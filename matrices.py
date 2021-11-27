'''
Genere una matriz de N x M donde N es el número de pisos que existen en un hotel (N se debe solicitar al usuario) y M es el número de habitaciones que existirán por piso (M se debe solicitar al usuario). La matriz será rellenada con números enteros aleatorios entre 0 y 5, este número indicará cuántas personas actualmente se están alojando en la habitación del hotel, pero la columna central de la matriz los valores deben completarse con 0 debido que representaran el pasillo principal y las escaleras, nadie se puede alojar en la columna principal. El hotel cobra por persona $12.000 el día.
'''

from random import randint as r
matriz = []
personas=0
piezas=0
#almacenamos contadores para personas y piezas, para matriz hacemos una lista.

#Pidiendo la cantidad de pisos
floors = int(input("Pisos: "))
while floors < 2:
    floors = int(input("Pisos: "))
#Pidiendo la cantidad de habitaciones
rooms = int(input("Habitaciones: "))
while (rooms < 3) or (rooms % 2 == 0):
    rooms = int(input("Habitaciones: "))
#almacenando la matriz
for q in range(0, floors):
    list = []
    for w in range(0, rooms):
        num_random = r(0,5)
        list.append(num_random)
    matriz.append(list)
#rango de pisos y de piezas
for u in range(floors):
    i = (int((rooms/2)+(rooms%2)))
    matriz[u][i-1] = 0
#Haciendo el contador de personas
for x in range(floors):
    for d in range(rooms):
        personas+=matriz[x][d]
#Haciendo el contador de piezas vacias
for x in range(floors):
    for d in range(rooms):
        if (matriz[x][d] == 0):
            piezas+=1
#almacenando las ganancias
earnings=personas*12000
total_earnings=(((floors*rooms)-floors)*12000)*5
#almacenando las ganancias maximas
print("\nLa matriz seria la siguiente: \n")
for y in range(len(matriz)):
    for x in range(len(matriz[y])):
        print(matriz[y][x],end=("  ")) 
    print() 
#Printeamos todos los datos necesarios
print('Las ganancias totales si se quedan 5 personas por pieza:',total_earnings)
print('')
print('Las ganancias totales de las personas que se quedan en el hotel seria:',earnings)
print('')
print('La cantidad de personas alojadas actualmente es de:',personas)
print('')
print('La cantidad de piezas vacias es de :',piezas)

