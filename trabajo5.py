def calcular_promedio(notas):

  return sum(notas) / len(notas)

def determinar_aprobacion(promedio):

  if promedio >= 4.5:
    print("Aprobado")
  else:
    print("Reprobado") 

if __name__ == "__main__": #Este bloque de código se ejecuta solo si el archivo se ejecuta directamente, no si se importa como módulo.
  cantidad_notas = int(input("Ingrese la cantidad de notas: "))
  notas = []

  i = 1
  while i <= cantidad_notas:
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota) #Agrega la nota ingresada a la lista
    i += 1

  promedio = calcular_promedio(notas)
  resultado = determinar_aprobacion(promedio)

  print(f"El promedio del estudiante es: {promedio:.2f}")
  print(f"El estudiante está: {resultado}")