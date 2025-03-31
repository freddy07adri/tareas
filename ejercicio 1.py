while True:
    tipo = input("Tipo de vehículo (bici/moto/carro/camion): ")
    
    if tipo == "bici":
        importe = 100
    elif tipo in ["moto", "carro"]:
        km = int(input("Kilómetros recorridos: "))
        importe = km * 30
    elif tipo == "camion":
        km = int(input("Kilómetros recorridos: "))
        toneladas = int(input("Toneladas del camión: "))
        importe = (km * 30) + (toneladas * 25)
    else:
        print("Esa porra no existe. Intenta de nuevo.")
        continue
    
    print("Importe a pagar:", importe, "córdobas")
    repetir = input("¿Quieres calcular otro importe? (chi/ño): ")
    if repetir != "chi":
        break

