edad = int(input("¿Cuántos años tienes? "))

if edad < 0:
    print("EDAD INVALIDA")

elif edad < 5:
    print("SU ES ENTRADA GRATIS")
elif edad <=11:
    print("SU ENTRADA TIENE UN COSTO DE 5.000")
elif edad <=59:
    print(" SU ENTRADA TIENE UN COSTO DE 8.000")
else:
    print("El precio es $4,000 (descuento adulto mayor)")


