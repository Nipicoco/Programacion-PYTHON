
edad=int(input('Ingresar edad: '))
mayor=18

if edad>mayor:
    print('Usted es mayor de edad por',edad-mayor,"Años")
elif edad==mayor:
    print('Usted es mayor de edad')
else:
    print('Le faltan',mayor-edad,"años para ser mayor de edad")
input('Enter para terminar')