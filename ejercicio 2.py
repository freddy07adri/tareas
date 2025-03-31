while True:
    articulo = input("Ingrese el nombre del artículo: ")
    precio_unitario = float(input("Ingrese el precio unitario del artículo: "))
    cantidad = int(input("Ingrese la cantidad a comprar: "))
    
    subtotal = precio_unitario * cantidad
    iva = subtotal * 0.15
    descuento = 0
    
    if subtotal > 1000:
        descuento = subtotal * 0.12
    
    total = subtotal + iva - descuento
    
    print("\n--- FACTURA ---")
    print("Artículo: ",articulo,)
    print("Cantidad: ",cantidad,"cordobas")
    print("Precio unitario: ",precio_unitario, "Cordoba")
    print("Subtotal: ",subtotal, "Cordoba")
    print("IVA (15%): ",iva, "Cordoba")
    print("Descuento (12% si aplica): ",descuento,  "Cordoba")
    print("Total a pagar: ",total, "Cordoba")
    
    repetir = input("¿Quieres repetir el programa? (chi/ño): ")
    if repetir == "ño":
        print("El acabado")
        break

