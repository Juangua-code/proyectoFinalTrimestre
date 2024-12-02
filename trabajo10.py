def calcular_pago():
    valor = float(input("Digite cantidad a pagar: "))
    if valor > 20000:
        print("Descuento aplicado. Total a pagar: $", valor * 0.8)
    else:
        print("No se aplica descuento. Total a pagar: $", valor)

# Llamar la función
calcular_pago()