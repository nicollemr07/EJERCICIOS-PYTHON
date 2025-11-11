edad = int(input("Ingresa tu edad: "))
print("Selecciona tu género:")
print("1. Femenino")
print("2. Masculino")
print("3. Barbie")

opcion = input("Ingresa el número correspondiente a tu género: ")

if opcion == "1":
    genero = "Femenino"
elif opcion == "2":
    genero = "Masculino"
elif opcion == "3":
    genero = "Barbie"
else:
    genero = "No especificado"


if edad >= 18:
    print(f"Eres mayor de edad y tu género es {genero}.")
else:
    print(f"No eres mayor de edad y tu género es {genero}.")