print("=== PEDIR UN DOMICILIO ===")

hambre = input("¿Tienes hambre? (si/no): ")

if hambre == "si":
    print("Busca un restaurante o una app de domicilios.")
    restaurante = input("¿Qué restaurante o aplicacion elegiste?: ")
    
    print("Elige tu comida.")
    comida = input("¿Qué comida vas a pedir?: ")
    
    print("Verifica el precio y tu dirección.")
    direccion = input("Escribe tu dirección: ")
    
    pago = input("¿Tienes dinero o medio de pago? (si/no): ")
    if pago == "si":
        print("Realizando pedido...")
        print("Esperando entrega...")
        print("¡Tu pedido ha llegado!")
        
        correcto = input("¿Todo está bien con el pedido? (si/no): ")
        if correcto == "si":
            print("Disfruta tu comida ")
        else:
            print("Llama al restaurante para reportar el problema.")
        
        print("Califica el servicio y recicla los empaques. Gracias ")
    else:
        print("No puedes hacer el pedido sin medio de pago.")
else:
    print("Ok, tal vez después. Fin.")

