from os import system as p
import time
import math #libreria que usaremos.


def aplicacionmat():    
    time.sleep(0.5)
    
    def esperar():
        p('cls')
        time.sleep(0.5)

    def salir():
        print("Saliendo de la aplicacion!")
        time.sleep(1)
        print("La aplicación se a cerrado correctamente!")
        exit(0)

    def opciones():
        p('cls')
        print("Bienvenido a la aplicacion matematica para calcular la altura, las opciones son las siguientes: \n1.) Calcular Altura. \n2.) Salir de la aplicacion")
        opcion=int(input("Ingrese su opcion: "))
        if opcion==1:
            esperar()
            altura()
        elif opcion==2:
            salir()
        else:
            print("Opcion invalida!")
            esperar()
            opciones()
        
        
    def opciones2():
        
        print("============")
        op=int(input("1. Salir\n2. Volver al menu \nIngresar opcion: "))
        while op>=3 or op<=0:
            
            print("OPCION INCORRECTA!  Volviendo a las opciones!")
            time.sleep(1.5)
            p('cls')
            opciones2()
        if op == 1:
            salir()
        elif op == 2:
            esperar()
            aplicacionmat()
        elif op == 3:
            esperar()
            altura()
            

    def altura():
        
        print("Programa para calcular la altura de un objeto.")
        sombra = float(input("Distancia: "))
        alfa = int(input("Angulo: "))
        alfa = math.radians(alfa)
        h = sombra*math.tan(alfa)
        print("La altura es: ", round(h, 1), "metros")
        
 
        opciones2()
        opciones2()
    opciones() 
aplicacionmat()



