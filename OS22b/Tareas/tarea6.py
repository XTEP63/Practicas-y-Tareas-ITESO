from ast import Break
from asyncio.windows_events import INFINITE


while True:
    while True:

        try:
            problema = int(input("Dame un numero de problema entre 1-10: "))
        except ValueError:
            print("Debes escribir un número -_-")
            continue

        if problema == 22:
            exit()
        elif problema < 1 or problema > 10:
            print("Ese problema no existe -_-")
            continue
        else:
            break

    if problema == 1:
        
        while True:
            print("Dabes de ser mayor de edad")
            try:
                edad = int(input("Cual es tu edad: "))
            except ValueError:
                print("Debes escribir un número -_-")
                continue

            if edad < 18:
                print("No eres mayor de edad -_-")
                continue
            else:
                break
        print("Eres mayor de edad, tienes:",edad,"años ^w^")

    elif problema == 2:

        while True:
            
            try:
                num = int(input("Dame un numero positvo: "))
            except ValueError:
                print("Debes escribir un número -_-")
                continue

            if num < 0:
                print("No es positivo -_-")
                continue
            else:
                break
        print("Eres mayor de edad ^w^")

    elif problema == 3:

        while True:
            
            try:
                num = int(input("Dame un numero par y multiplo de 3: "))
            except ValueError:
                print("Debes escribir un número -_-")
                continue

            if num % 2 != 0 and num % 3 == 0:
                    print("El numero no es par -_-")
                    continue
            elif num % 2 == 0 and num % 3 != 0:
                    print("El numero no es multiplo de 3 -_-")
                    continue
            elif num % 2 != 0 and num % 3 != 0:
                    print("El numero no es ni par ni multiplo de 3 -_-")
                    continue
            else:
                break
        print("Es multiplo de 3 y es par ^w^")

    elif problema == 4:

        while True:

            print("Dame tu edad y la de tu amigo")
            try:
                edad = int(input("Cual es tu edad: "))
                edad_amigo = int(input("Cual es la edad de tu amigo: "))
            except ValueError:
                print("Debes escribir un número -_-")
                continue

            if edad < 18 and edad_amigo >= 18:
                print("No eres mayor de edad -_-")
                continue
            elif edad >= 18 and edad_amigo < 18:
                print("Tu amigo no es mayor de edad -_-")
                continue
            elif edad < 18 and edad_amigo < 18:
                print("Ninguno es mayor de edad -_-")
                continue
            else:
                break
        print("Son mayores de edad, tienen:",edad,"años",edad_amigo,"años ^w^")

    elif problema == 5:

        while True:
            print("Dame tres numero consecutivos acendentes")
            try:
                num1 = int(input("Cual es el primer numero: "))
                num2 = int(input("Cual es el segundo numero: "))
                num3 = int(input("Cual es el tercer numero: "))
            except ValueError:
                print("Debes escribir un número -_-")
                continue

            if num1 < num2 or num2 < num3:
                print("No son acendentes -_-")
                continue
            elif num2 != num1 + 1 or num3 != num2 + 1:
                print("No son consecutivos -_-")
                continue
            else:
                break
        print("Son numero consecutivos acendentes ^w^")
        
    elif problema == 6:

        while True:
            print("Alguno debe de ser mayor de edad")
            try:
                edad = int(input("Cual es tu edad: "))
                edad_a1 = int(input("Cual es su edad: "))
                edad_a2 = int(input("Cual es su edad: "))
            except ValueError:
                print("Debes escribir un número -_-")
                continue

            if edad >17 or edad_a1 > 17 or edad_a2 > 17:
                break
            else:
                print("Ninguno es mayor de edad")
                continue
        print("Alguno es mayor de edad ^w^")

    elif problema == 7: 

        while True:
            print("Dame tres numeros acendentes")
            try:
                num1 = int(input("Cual es el primer numero: "))
            except ValueError:
                print("Debes escribir un número -_-")
                continue
            
            while True:
                try:
                    num2 = int(input("Cual es el segundo numero: "))
                except ValueError:
                    print("Debes escribir un número -_-")
                    continue

                if num2 <= num1:
                    print("No son acendentes -_-")
                    continue
                else:
                    while True:
                        try:
                            num3 = int(input("Cual es el tercer numero: "))
                        except ValueError:
                            print("Debes escribir un número -_-")
                            continue
                        
                        if num3 <= num2:
                            print("No son acendentes -_-")
                            continue
                        else:
                            break
                break
            break
        print("Son numero consecutivos acendentes ^w^")
        print()
    elif problema == 8:

        print()

    elif problema == 9:

        print()

    elif problema == 10:

        print()

    
    

