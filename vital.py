# Solicitar datos al usuario
edad = int(input("Ingrese su edad: "))

# Validar que la edad sea coherente
if edad < 0 or edad > 120:
    print("Edad no válida.")
else:
    nivel = input("¿Actualmente estudia, trabaja o ninguna? ").strip().lower()

    # Clasificación según las reglas
    if edad < 6:
        etapa = "Infante"
    elif 6 <= edad <= 17 and nivel == "estudia":
        etapa = "Estudiante escolar"
    elif 18 <= edad <= 25 and nivel == "estudia":
        etapa = "Universitario"
    elif edad > 25 and nivel == "trabaja":
        etapa = "Adulto activo"
    elif edad > 60 and nivel == "ninguna":
        etapa = "Adulto mayor jubilado"
    else:
        etapa = "No determinado"

    print(f"Clasificación: {etapa}")
