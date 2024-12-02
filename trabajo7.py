def evaluar_aprendiz():
    nom = input("Nombre del aprendiz: ")
    asig = input("Asignatura cursando: ")

    while True:
        try:
            # Pedir la calificación final
            calF = float(input("Nota de su examen final: "))
            
            # Validar que la calificación esté en el rango permitido
            if 1 <= calF <= 10:
                if calF >= 7:
                    print(f"El alumn@ {nom} en la asignatura {asig} ha aprobado con una calificación de {calF}.")
                else:
                    print(f"El alumn@ {nom} en la asignatura {asig} ha reprobado con una calificación de {calF}.")
                break  # Termina el bucle si la calificación es válida
            else:
                print("La calificación debe estar entre 1 y 10. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número válido.")

# Llamada a la función
evaluar_aprendiz()