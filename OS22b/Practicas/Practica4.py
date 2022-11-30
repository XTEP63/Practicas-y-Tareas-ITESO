while True:

    try:
        edad = int(input("Escribe tu edad: "))
    except ValueError:
        print("Debes escribir un número -_-.")
        continue

    if edad < 0 or edad > 110:
        print("Debes escribir un número positivo o menor a 110 -_-.")
        continue
    else:
        break

print("Si cumples con los parámetros")
