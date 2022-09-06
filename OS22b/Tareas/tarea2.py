from unicodedata import numeric


Problema = int(input("Cual problema quieres ver del 1-15: "))

if Problema ==  1:

    #*Una variable de tipo entero y una para guardar valores
    Edad = int(input("Cual es tu edad: "))
    Edad_10 = Edad + 10

    print(Edad_10,"Sera tu edad dentro de 10 años")

elif Problema == 2:

    #*Una variable de tipo entero y una para guardar valores
    Numero = int(input("Dame un numero entero: "))
    Numero_Next = Numero + 1

    print(Numero_Next,"Es el siguiente numero entero")

elif Problema == 3:

    #*Una variable de numero entero y dos para guardar valores
    Numero = int(input("Dame un numero entero: "))
    Numero2_Duble = Numero*2
    Numero2_Half = Numero/2

    print("El doble del numero es:",Numero2_Duble,"y la mitad es:", Numero2_Half)

elif Problema == 4:

    #*Dos variables de numero entero y 4 para guardar valores
    Entero1 = int(input("Dame un numero entero: "))
    Entero2 = int(input("Dame otro numero entero: "))
    mult = Entero1*Entero2
    suma = Entero1+Entero2
    rest = Entero1-Entero2
    div = Entero1/Entero2

    print("La suma de los dos es:",suma,"El de su resta:",rest,"El de su multiplicacion:",mult,"El de su diision:",div)

elif Problema == 5:

    #*Una variable de tipo entero y una para guardar datos
    Num_mas10 = int(input("Dame un numero entero mayor a 10: "))
    Decenas = Num_mas10//10

    print("El numero tiene:",Decenas,"decenas")

elif Problema == 6:

    #*Una variable de tipo entero y una para guardar datos
    Numero = int(input("Dame un numero entero: "))
    Centenas = (Numero%1000)//100

    print("El numero tiene:",Centenas,"centenas como digito")

elif Problema == 7:

    #*Una variable de tipo entero y una para guardar datos
    Numero = int(input("Dame un numero entero: "))
    Num_par = (Numero+2)-(Numero%2)

    print(Num_par)

elif Problema == 8:

    #*Una variable de tipo str
    palabra = input("Dame una palabra: ")

    print("("+ palabra +")")

elif Problema == 9:

    #*Dos variables de tipo str 
    palabra = input("Dame una palabra: ")
    palabra2 = input("Dame otra palabra: ")

    print("La concatenacion es:",palabra+palabra2)

elif Problema == 10:

    #*Una variable de tipo entero y tres para guardar valores
    Numero = int(input("Dame un numero natural entre 100 y 999: "))
    Centenas = Numero//100
    Decenas = (Numero%100)//10
    Unidades = (Numero%10)%10
    
    print("Las unidades son:",Unidades,"Las decenas son:",Decenas,"Las centenas son:",Centenas)

elif Problema == 11:

    #*Una varaible de tipo str y dos para guardar datos 
    Palabra = input("Dame una palabra: ")
    palabra_Up = Palabra.upper()
    palabra_Low = Palabra.lower()

    print("En mayuscula", palabra_Up, "En minusculas",palabra_Low)

elif Problema == 12:

    #*Una varible de tipo entero y otra de tipo str y otra para guardar datos 
    Numero = int(input("Dame un numero entero: "))
    Palabra = input("Dame una palabra: ")
    Cadena = Palabra*Numero

    print("La cadena es:",Cadena)

elif Problema == 13:

    #*Una varibale de tipo entero y otra para guardar datos 
    Numero = int(input("Dame un numero entero: "))
    Raiz_2 = Numero**0.5

    print("La raiz del numero es:", Raiz_2)

elif Problema == 14:

    #*Tres varaibles de tipo entero y otra para la formula
    a = int(input("Dame un numero entero: "))
    b = int(input("Dame otro numero entero: "))
    c = int(input("Dame otro numero entero mas: "))
    formula =(-b+(((b**2)-4*a*c)**0.5))/(2*a)
    formula_2 =(-b-(((b**2)-4*a*c)**0.5))/(2*a)

    print("x1:",formula)
    print("x2:",formula_2)

elif Problema == 15:

    #*cuatro varibles de tipo float 
    x1 = float(input("Dame la cordenada de x1: ")) 
    x2 = float(input("Dame la cordenada de x2: "))
    y1 = float(input("Dame la cordenada de y1: "))
    y2 = float(input("Dame la cordenada de y2: "))
    Distacia = (((x2-x1)**2)+((y2-y1)**2))**0.5
    punto_mx = ((x1+x2)/2)
    punto_my = ((y1+y2)/2)
    print("La dsitancia entre los dos punto es:",Distacia,"y el punto medio es:","(",punto_mx,",",punto_my,")")
else:
    print("No existe el problema XD")