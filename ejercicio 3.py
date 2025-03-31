while True:
    articulo = input("Ingrese el nombre del artículo: ")
    precio_por_docena = float(input("Ingrese el precio por docena del artículo: "))
    cantidad_docenas = int(input("Ingrese la cantidad de docenas a comprar: "))
    
    subtotal = precio_por_docena * cantidad_docenas
    
    if cantidad_docenas > 3:
        descuento = subtotal * 0.15
        unidades_obsequio = cantidad_docenas - 3
    else:
        descuento = subtotal * 0.10
        unidades_obsequio = 0
    
    total_a_pagar = subtotal - descuento
