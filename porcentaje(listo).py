from os import system
import time
def porcentajes():
    print("============")
    a= int(input("Ingresar el precio del producto: "))
    print("\n\n")
    b= int(input("Ingresar el descuento para aplicar: "))
    
    if b > 100:
        system('cls')
        print("El descuento no puede ser mas del 100%")
        time.sleep(1)
        b= int(input("Ingresar el descuento: ")) 

    c = int(a * b / 100)
    precio= a-c
    system('cls')
    print("============")
    print("El precio del producto con un ",b, " de descuento es de ",precio, "pesos")
    print("============")
    
porcentajes()
        
        