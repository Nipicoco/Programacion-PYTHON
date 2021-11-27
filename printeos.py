
print('La lista de candidatos es: \n1)Emilia Hajimeru\n2)Martin Completos\n3)Armando Casas\n4)Ignacio Montero\n5)Ricardo Milos')

numeroc=input("Ingresar el numero de candidato elegido: ")
c1="El numero elegido corresponde al candidato \"Emilia Hajimeru\" de color gris"
c2="El numero elegido corresponde al candidato \"Martin Completos\" de color verde"
c3="El numero elegido corresponde al candidato \"Armando Casas\" de color azul"
c4="El numero elegido corresponde al candidato \"Ignacio Montero\" de color rojo"
c5="El numero elegido corresponde al candidato \"Ricardo Milos\" de color amarillo"
####
if numeroc=="1":
    print(c1)
elif numeroc=="2":
    print(c2)
elif numeroc=="3":
    print(c3)
elif numeroc=="4":
    print(c4)
elif numeroc=="5":
    print(c5)
else:
    print('No se ha ingresado ningun numero o el numero ingresada es incorrecto')
input('Presionar enter para terminar')