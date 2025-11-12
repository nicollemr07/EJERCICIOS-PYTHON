si = 0
no = 0

while True:
    try:
        edad = int(input("Ingrese su edad (0 para salir): "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if edad <= 0:
        break

    respuesta = input("¿Te gusta programar? (sí/no): ").strip().lower()

    if respuesta in ["si", "sí"]:
        si += 1
    elif respuesta == "no":
        no += 1
    else:
        print("Respuesta no válida, no se contabiliza.")
        continue

print("\n--- RESULTADOS ---")
print(f"Respuestas afirmativas: {si}")
print(f"Respuestas negativas: {no}")