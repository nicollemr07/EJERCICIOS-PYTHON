usuario_correcto = "admin"
clave_correcta = "1234"
intentos = 0

while intentos < 3:
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if usuario == "" and clave == "":
        print("Campos vacíos. Este intento no cuenta.\n")
        continue

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        break
    else:
        print("Error: usuario o contraseña incorrectos.\n")
        intentos += 1

if intentos == 3:
    print(" Límite de intentos alcanzado.")