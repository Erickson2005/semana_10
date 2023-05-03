total_compra = 0

while True:
    monto_compra = float(input("Ingrese el monto de la compra: "))
    
    if monto_compra < 0:
        print("Monto inválido. La compra no se procesará.")
        continue
    
    if monto_compra > 500 and monto_compra <= 1000:
        monto_compra *= 0.95
        print("Se aplicó un descuento del 5%.")
    elif monto_compra > 1000:
        monto_compra *= 0.90
        print("Se aplicó un descuento del 10%.")
    
    total_compra += monto_compra
    
    respuesta = input("¿Desea ingresar otra compra? (s/n): ")
    
    if respuesta.lower() != 's':
        break
        
print("El total de la compra es de ${:.2f}".format(total_compra))