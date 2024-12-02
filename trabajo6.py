def convertir_dolares_a_pesos(dolares):

  tasa_cambio = 3.934  # Tasa de cambio fija
  pesos = dolares * tasa_cambio
  return pesos

if __name__ == "__main__":
  while True:
    try:
      dolares = float(input("Ingrese la cantidad de dólares a convertir: "))
      pesos = convertir_dolares_a_pesos(dolares)
      print(f"{dolares} dólares equivalen a {pesos} pesos colombianos.")
      continuar = input("¿Desea realizar otra conversión? (si/no): ")
      if continuar.lower() != 'si':
        break
    except ValueError:
      print("Por favor, ingrese un valor numérico válido.")