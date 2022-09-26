
from __future__ import print_function
from json import detect_encoding
from sqlite3 import DataError

while True:
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

        print("Ahora tienes:",word[:num],"^w^")

    elif problema == 5:

        word = input("Dame una palabra: ")
        num = int(input("Dame un numero entre el 1 y " + str(len(word)) + ": "))
        word = word[::-1]

        print("Ahora tienes:",word[:num],"^w^")
        
    elif problema == 6:

        Curp = input("Dame tu CURP: ")
        
        print("Naciste en el año: " + Curp[4:6] + ", en el mes: " + Curp[6:8] + ", en el dia: " + Curp[8:10] + ", y tu sexo es: " + Curp[11])

    elif problema == 7: 

        date = input("Dame un afecha en el siguente formato dd/mm/aaaa: ")

        print("En fomao americano seria:",date[3:5]+"/"+date[:2]+"/"+date[6:],"^w^")

    elif problema == 8:

        num = input("Dame unn numero: ")
        num_rev = int(num[::-1])
        num = int(num)

        print("La suma con su espejo es:", num + num_rev,"^w^")

    elif problema == 9:

        dom = input("Dame una ficha de domino con el siguiente formato #:#, # son numero s del unos al 6: ")

        if dom[0] == dom[-1]:
            print("Es una mula ^w^")
        else:
            print("No es una mula -_-")

    elif problema == 10:

        word = input("Dame una frace: ")

        if word[0] == word[0].upper():
            if word[-1] == ".":
                print("Esta bien escrita ^w^")
            else:
                print("Le falta el punto final -_-")
        else: 
            print("Le falta inicar con mayuscula -_-")

    

