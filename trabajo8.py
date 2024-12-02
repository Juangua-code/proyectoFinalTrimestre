def revision_jubilacion():
    edad = int(input("¿Cuántos años tiene? "))
    sexo = input("Digite su sexo (Masculino o Femenino): ").lower()

    if sexo in ["masculino", "hombre", "m"]:
        if edad >= 63:
            print("Usted puede jubilarse.")
        else:
            print("Usted aún no puede jubilarse.")
    elif sexo in ["femenino", "mujer", "f"]:
        if edad >= 54:
            print("Usted puede jubilarse.")
        else:
            print("Usted aún no puede jubilarse.")
    else:
        print("Sexo no válido. Por favor, ingrese Masculino o Femenino.")


revision_jubilacion()