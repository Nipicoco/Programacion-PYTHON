


def sorteado():
    def calculos():
        desco=str(input("\nIngresar el orden\n1. Desc\n2. Asc\nIngresar opcion textual o numerica: "))
        desco=desco.lower()
        if desco=="desc":
            return print(sorted(a, reverse=True))
        elif desco=="1":
            return print(sorted(a, reverse=True))
        elif desco=="asc":
            return print(sorted(a, reverse=False))
        elif desco=="2":
            return print(sorted(a, reverse=False))
        else:
            return desco
    n = int(input("Ingresar cantidad de elementos : "))
 

    a = list(map(int,input("\nIngresar los numeros separados con un espacio : ").strip().split()))[:n]
     
    print("La lista queda de la siguiente forma: ",a) 
    calculos()
    
sorteado()

