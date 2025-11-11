print("------TIENDA NICOLLE-------")
def pedir_float(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido. Por favor, ingresa un número decimal válido.")

def pedir_int(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Valor inválido. Por favor, ingresa un número entero válido.")


nombre = input("Ingresa el nombre del producto: ")
precio = pedir_float("Ingresa el precio del producto: ")
cantidad = pedir_int("Ingresa la cantidad disponible: ")


print("--- Inventario ---")
print(f"Nombre del producto: {nombre}")
print(f"Precio: ${precio:.2f}")
print(f"Cantidad: {cantidad}")