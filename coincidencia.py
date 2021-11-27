
nombre1 = input("Ingresa un nombre: ")
nombre2 = input("Ingresa un nombre: ")

primera_letra1 = nombre1[0].lower()
ultima_letra1 = nombre1[-1].lower()
primera_letra2 = nombre2[0].lower()
ultima_letra2 = nombre2[-1].lower()

if primera_letra1 == primera_letra2:
    print("Hay coincidencia")
elif ultima_letra1 == ultima_letra2:
    print("Hay coincidencia")
else:
    print("No hay coincidencia")
input('Enter para salir')