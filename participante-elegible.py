
edad = int(input("Ingrese su edad: "))
licencia = input("¿Tiene licencia de conducción vigente? (sí/no): ").strip().lower()
vehiculo = input("¿Posee vehículo propio o tiene préstamo autorizado? (sí/no): ").strip().lower()

if edad >= 18 and licencia in ["si", "sí"] and vehiculo in ["si", "sí"]:
    print("Apto para participar en la competencia.")
else:
    print("No apto para participar en la competencia.")


