#programa hecho para un amigo.
def verificacion(passwd):
    simbolos=['#','$','@']
    val = True

    if len(passwd) < 6:
        print("La contrasena debe tener sobre 6 caracteres.")
        val = False

    if len(passwd) > 16:
        print("La contrasena debe tener menos de 16 caracteres.")
        val = False

    if not any(x.isdigit() for x in passwd):
        print("La contrasena debe por lo menos un numero")
        val = False

    if not any(x.isupper() for x in passwd):
        print("La contrasena debe por lo menos una letra en mayusculas")
        val = False

    if not any(x.islower() for x in passwd):
        print("La contrasena debe por lo menos una letra en minusculas")
        val = False

    if not any(x in simbolos for x in passwd):
        print("La contrasena tener por lo menos uno de los simbolos especiales ('#','$','@'")
    
    if val:
        return val


def main():

    passwd = input('ingresar:')
    if (verificacion(passwd)):
        print('Correcto')
    else:
        print('Incorrecto')

if __name__ == '__main__':
    main()

    