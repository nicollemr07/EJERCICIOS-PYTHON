nombres = []
repetido = False

while True:
    nombre = input("Ingrese un nombre (FIN para terminar): ").strip()

    if nombre.upper() == "FIN":
        break

    if nombre == "":
        print("Entrada vacía ignorada.")
        continue

    if nombre in nombres:
        repetido = True

    nombres.append(nombre)

print("\n--- RESULTADOS ---")
print("Total de nombres ingresados:", len(nombres))

if repetido:
    print("Hubo nombres repetidos.")
else:
    print("No hubo nombres repetidos.")