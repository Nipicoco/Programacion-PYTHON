

numero1=int(input("Ingresar primer numero: "))
numero2=int(input("Ingresar segundo numero: "))
mini=min(numero1,numero2)
mayor=max(numero1,numero2)
if numero1==numero2:
    print("El numero menor es:",mini)
else:
    print('El numero menor es:',mini)
numero3=int(input('Ingresar tercer numero: '))
multip=(numero3*mini)
print("Si mutiplicamos el tercer numero con el menor seria:",multip)
if multip>mayor:
    print('El numero resultado de la multiplicacion es mayor que el numero mas grande de la primera comparacion')
else:
    print('El numero resultado de la multiplicacion es menor que el numero mas grande de la primera comparacion')
input('Enter para salir')