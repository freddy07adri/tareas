while True:
    numero = input("Ingrese un número de tres cifras: ")
    
    if len(numero) != 3 or not numero.isdigit():
        print("ingrese un número válido de tres cifras.")
        continue
    
    if numero == numero[::-1]:
        print("El número ",numero," es igual al revés.")
    else:
        print("El número ",numero, "no es igual.")
    
    repetir = input("¿Quieres probar otro número? (chi/ño): ").strip().lower()
    if repetir == "ño":
        print("el acabado.")
        break
