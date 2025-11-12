try:
    monto = float(input("Ingrese el valor total de la compra: "))
except ValueError:
    print("Error: monto inválido.")
    exit()

membresia = input("Tipo de membresía (activa/temporal/ninguna): ").lower().strip()

if monto < 0:
    print("Error: el monto no puede ser negativo.")
elif monto >= 100000 and membresia == "activa":
    print("Cliente Premium.")
elif (50000 <= monto < 100000) or membresia == "temporal":
    print("Cliente Frecuente.")
else:
    print("Cliente Regular.")