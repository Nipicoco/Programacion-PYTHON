

nombre1=input('Ingresar primer nombre: ')
nombre2=input('Ingresar segundo nombre: ')

if len(nombre1)==len(nombre2):
    print('Los nombres son de igual longitud') 
elif len(nombre1)>len(nombre2):
    print('El nombre de mayor longitud es:',nombre1,"y la diferencia de caracteres es de:",len(nombre1)-len(nombre2))
else:
    print('El nombre de mayor longitud es:',nombre2,"y la diferencia de caracteres es de:",len(nombre2)-len(nombre1))
input('ENTER para terminar')