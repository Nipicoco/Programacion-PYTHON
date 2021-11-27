from os import system as ñ
import time


def aplicacionmat():    
    time.sleep(0.5)
    
    def esperar():
        ñ('cls')
        time.sleep(0.5)

    def salir():
        print("Saliendo de la aplicacion!")
        time.sleep(1)
        exit(0)

    def opciones():
        ñ('cls')
        print("Bienvenido a la aplicacion matematica las opciones son las siguientes: \n1,Calcular N-Esimo termino \n2.Calcular Binomio \n3.Calcular Secuencia de Fibonacci \n4.Salir de la aplicacion")
        opcion=int(input("Ingrese su opcion: "))
        if opcion==1:
            esperar()
            enesimo()
        elif opcion==2:
            esperar()
            binomio()
        elif opcion==3:
            esperar()
            recursion()
        elif opcion==4:
            salir()
        else:
            print("Opcion invalida!")
            esperar()
            return(opciones())
        
        
    def opciones2():
        
        print("============")
        op=int(input("1. Salir\n2. Volver al menu\n3. Volver a la calculadora enesima\n4. Calculadora de binomio\n5. Secuencia de fibonacci\nIngresar opcion: "))
        while op>=4 or op<=0:
            esperar()
            opciones2()
        if op == 1:
            salir()
        elif op == 2:
            esperar()
            return(aplicacionmat())
        elif op == 3:
            esperar()
            return(enesimo())
        elif op == 4:
            esperar()
            return(binomio())
        elif op == 5:
            esperar()
            return(recursion())

    
            

    def enesimo():
        
        print("Programa para calcular el Enesimo termino de una sucesion.")
        
        lenn=int(input("\ningrese el total de digitos de la sucesion: "))
        while lenn<=1:
            lenn=int(input("\ningrese el total de digitos de la sucesion: "))
        secuencia=[]
        print("============")
        print("Recoleccion de numeros para la sucesion")
        print("============")
        i=0

        while i<lenn:
            print("ingrese el digito",i + 1,":")
            a=int(input())
            i+=1
            secuencia.append(a)
        print("============")
        print("la secuencia ingresada es ",secuencia)
        print("============")
        

        pos=int(input("\nCual es la n-esima posicion a calcular?\n"))
        a=secuencia[1]-secuencia[0]
        b=secuencia[0]-a
        ñ('cls')
        n= (a*pos)+b
        
        print("\nLa posicion de la secuencia cae en: ",n)
        opciones2()


    def binomio():   

        X=int(input("Ingresar valor de X: "))
        Y=int(input("Ingresar valor de Y: "))
        n=int(input("Ingresar valor de n: "))
        def series(X, Y, n):

            ñ('cls')  
            print("\nEl valor es:")
            termino = pow(X, n)
            print(termino, end = " ")
            
            
            for i in range(1, n+1):
            
                    
                    # Encuentra el término actual con términos anteriores
                    # Aumentamos la potencia de X en 1, la disminuimos.
                    # Potencia de A multiplicada por 1 y calcule nCi con
                    # el término anterior multiplicando al anterior
                    # termino con (n - i + 1) / i
                termino = int(termino * Y * (n - i + 1)/(i * X))
            
                print(termino, end = " ")
            print("\n")    
        series(X, Y, n)
        opciones2()
    def recursion():
        
        n=int(input("Ingrese el valor de 'n': "))
        n1=0
        n2=1
        sum=0
        cont=1
        print("Secuencia de Fibonacci de", n, "Numeros:")
        while(cont<=n):
          print(sum)
          cont+=1
          n1=n2
          n2=sum
          sum=n1+n2
        opciones2()
    opciones() 
aplicacionmat()
