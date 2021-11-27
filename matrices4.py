'''
Genere 3 matrices de tamaño N x M donde N es el número de estudiantes que existen en el ramo (N se debe solicitar al usuario) y M es el número de tareas que se han realizado durante el año dentro del ramo(M se debe solicitar al usuario). Las notas son números flotantes del 1.0 al 7.0 estos se generarán de forma aleatoria. Los 3 ramos poseen la misma cantidad de tareas y la misma cantidad de estudiantes
'''
from random import uniform as u

matrix = []
matrix2 = []
matrix3 = []
passed = 0
failed = 0
#haremos un almacen de las matrices y valores que usaremos adelaante

n = int(input("Estudiantes: "))
m = int(input("Tareas: "))
#pediremos cantidad de estudiantes y tareas

students = [0]*n
for x in range(n):
    list = []
    for y in range(m):
        val = u(1,7)
        val = val * 10
        natural = int(val)
        val = natural/10
        list.append(val)
    matrix.append(list)

print(matrix)

for x in range(n):
    list = []
    for y in range(m):
        val = u(1,7)
        val = val * 10
        natural = int(val)
        val = natural/10
        list.append(val)
    matrix2.append(list)

print(matrix2)

for x in range(n):
    list = []
    for y in range(m):
        val = u(1,7)
        val = val * 10
        natural = int(val)
        val = natural/10
        list.append(val)
    matrix3.append(list)

print(matrix3)

notes = [0]*n
print("Progra")
for a in range(n):
    prom = 0
    for b in range(m):
        prom += matrix3[a][b]
    prom /= m
    prom *=10
    prom1 = int(prom)
    prom = prom1/10
    if (prom >= 4.0):
        passed += 1
    else:
        failed += 1
        students[a] += 1
    notes[a] += prom
    print("El estudiante",(a+1),"tubo un promedio de",prom)

print("Robot")

for a in range(n):
    prom = 0
    for b in range(m):
        prom += matrix3[a][b]
    prom /= m
    prom *=10
    prom1 = int(prom)
    prom = prom1/10
    if (prom >= 4.0):
        passed += 1
    else:
        failed += 1
        students[a] += 1
    notes[a] += prom
    print("El estudiante",(a+1),"tubo un promedio de",prom)

print("Matematicas")

for a in range(n):
    prom = 0
    for b in range(m):
        prom += matrix3[a][b]
    prom /= m
    prom *=10
    prom1 = int(prom)
    prom = prom1/10
    if (prom >= 4.0):
        passed += 1
    else:
        failed += 1
        students[a] += 1
    notes[a] += prom
    print("El estudiante",(a+1),"obtuvo un promedio de",prom)
#printeamos la cantidad de estudiantes que fallaron
print("la cantidad de estudiantes que reprobaron fue:",failed,"y los que aprovaron fue de:",passed)
for k in range(len(notes)):
    notes[k] = notes[k]/3
    notes[k] = notes[k]*100
    nota = int(notes[k])
    notes[k] = nota/100
print(notes)
total = 0
qeq = 0
for l in range(n):
    if (students[l] >= 2):
        total += 1
    else:
        if (students[l] == 0):
            qeq += 1
print("la cantidad que reprobo fue de:",total)
print("la cantidad que se salvo fue de:",qeq)