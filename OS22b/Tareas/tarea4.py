Problema = int(input("Que problema quieres resolver 1-7: "))

if Problema == 1:

    print("Te voy a pedir tres numero dame dos iguales y uno repetido")
    a = int(input("Dame un numero natural: "))
    b = int(input("Dame un numero natural: "))
    c = int(input("Dame un numero natural: "))
    lis = [a,b,c]

    print("El numero repetido es:",max(set(lis), key = lis.count ))

elif Problema == 2:
    
    año = int(input("Dame un año: "))

    if año % 4 != 0: 
        print("No es bisiesto -_-")
    elif año % 4 == 0 and año % 100 != 0:
        print("Es bisiesto ^w^!!!")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
        print("No es biciesto -_-")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	    print("Es bisiesto ^w^!!!")

elif Problema == 3:

    xp = float(input("Cual es la cantida de xp actual de tu personaje: "))
    xp_up = float(input("Cuanta xp se ocupa para subir de nivel: "))
    xp_monster = float(input("Cuanta xp te da el moustro que acabas de matar"))
    
    if xp + xp_monster == xp_up:
        print("Suuuuu puedes subir de nivel ^w^!!!")
    else:
        print("No puedes subir de nivel:")

elif Problema == 4:

    a = int(input("Dame un numero para a: "))
    b = int(input("Dame un numero para b: "))
    c = int(input("Dame un numero para c: "))

    if a >= b and a >= c:
        a = a*100
        if b >= c:
            b = b*10
            print(a+b+c)
        elif c >= b: 
            c = c*10
            print(a+c+b)
    elif b >= a and b >= c:
        b = b*100
        if a > c:
            a = a*10
            print(b+a+c)
        elif c > a: 
            c = c*10
            print(b+c+a)
    elif c >= a and c >= b:
        c = c*100
        if b > a:
            b = b*10
            print(c+b+a)
        elif a > b: 
            a = a*10    
            print(c+a+b)
    
elif Problema == 5:
    Carga = float(input("Cual es la carga maxima de tu personaje"))
    
    print()
elif Problema == 6:

    año = int (input("Dame un año"))
    mes = int(input("Dame el numero de mes"))

    if año % 4 != 0:
        bisiesto = "No es bisiesto"
    elif año % 4 == 0 and año % 100 != 0: 
        bisiesto = "bisiesto"
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
        bisiesto = "No bisiesto"
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
        bisiesto = "bisiesto"

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print("El mes tiene 31 dias")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print("El mes tiene 30 dias")
    elif mes == 2: 
        if bisiesto == "bisiesto":
            print("El mes tiene 29 dias")
        else:
            print("El mes tiene 28 dias")
    
elif Problema == 7:
    print()
else:
    print("El problema no existe XD")
