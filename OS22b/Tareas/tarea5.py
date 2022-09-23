
while True:

    try:
        problema = int(input("Dame un numero de problema entre 1-10: "))
    except ValueError:
        print("Debes escribir un número -_-")
        continue

    if problema < 1 or problema > 10:
        print("Ese problema no existe -_-")
        continue
    else:
        break

if problema == 1:

    nombre = input("Cual es tu nombre: ")

    print("Tiene",len(nombre),"caracteres ^w^")

elif problema == 2:

    num = int(input("Dame un numero: "))

    print("Tiene",len(str(num)),"digitos ^w^")

elif problema == 3:

    word = input("Dame una palabra: ")
    ln = int(input("Dame el numero de caracter que quieres: "))

    print("Tu caracter es:",word[ln-1],"^w^")

elif problema == 4:

    word = input("Dame una palabra: ")
    num = int(input("Dame un numero entre el 1 y " + str(len(word))+ ": "))

    print("Ahora tienes:",word[:num],"^w^" )

elif problema == 5:

    word = input("Dame una palabra: ")
    num = int(input("Dame un numero entre el 1 y " + str(len(word)) + ": "))
    word = word[::-1]
    print("Ahora tienes:",word[:num])
    