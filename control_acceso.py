restringidos = ["Ana", "Luis", "Marcos"]

usuario = input("Ingrese nombre de usuario: ")
codigo = input("Ingrese código numérico: ")

if not codigo.isdigit():
    print("Error: el código debe ser numérico.")
else:
    codigo = int(codigo)

    if usuario in restringidos:
        print("Acceso denegado: usuario restringido.")
    elif (codigo % 2 == 0) or (codigo % 10 == 7):
        print("Acceso permitido.")
    else:
        print("Acceso denegado: el código no cumple las condiciones.")