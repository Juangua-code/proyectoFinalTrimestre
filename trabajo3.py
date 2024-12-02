def mostrar_numeros():
    suma_linea = 0
    for i in range(1, 31):
        print(i,end= "  ")
        suma_linea += i
        if i % 7 == 0:
            print(f"Suma de la linea anterior: {suma_linea}")
            print("\n****")
            suma_linea = 0
    if suma_linea > 0:
        print(f"\nSuma de la ultima linea: {suma_linea}")

# Ejecutar la función
mostrar_numeros()