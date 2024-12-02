def impares(inicio, fin):
    for numero in range(inicio, fin + 1):
        if numero % 2 != 0:
            print(numero)

inicio = int(input("Inicio de conteo: "))
fin = int(input("Fin del conteo: "))

if inicio > fin:
    print("El número con el que inicia debe ser menor al número con el que finaliza.")
else:
    impares(inicio, fin)