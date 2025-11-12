
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a > 0 and b > 0 and c > 0:
    print("Los tres son positivos.")
elif a < 0 or b < 0 or c < 0:
    print("Al menos uno es negativo.")
elif ((a == 0) + (b == 0) + (c == 0)) == 1:
    print("Exactamente uno es cero.")
else:
    print("Otra combinación.")