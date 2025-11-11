sabores = {
    "chocolate": 4000,
    "vainilla": 3500
}


sabor = input("Ingrese el sabor del helado (chocolate o vainilla): ")


if sabor not in sabores:
    print("Sabor no disponible.")
else:
    
    topping = input("¿Desea agregar topping por $1.000? (sí/no): ")

    
    total = sabores[sabor]
    if topping in ["sí", "si", "s"]:
        total += 1000

    print(f"El total a pagar es: ${total:,}".replace(",", "."))
