from re import A


Problema = int(input("Que problema quieres resolver 1-15: "))

if Problema == 1:

    #*Dos variable de tipo Float
    #! (a) es mayor a (b) 

    a = float(input("Dame un numero entero: "))
    b = float(input("Dame otro numero entero: "))

    if a > b: 
        print("Estan en orden acendente ^w^!!!")
    else:
        print("No estan en orden acendente -_-")

elif Problema == 2:

    #*Una varible de tipo entero 
    #! EL modulo 9 de n es = 0

    n = int(input("Dame un numeor natural: "))

    if n%9 == 0:
        print("Es divisible entre nueve ^w^!!!")
    else:
        print("No es divisible entre nueve -_-")

elif Problema == 3:

    #*Dos varibles de tipo entero 
    #! n modulo de a es = 0 

    a = int(input("Dame un numero entero a: "))
    n = int(input("Dame otro numero entero n: "))

    if n%a == 0:
        print("n es multiplo de a ^w^!!!")
    else:
        print("n no es multiplo de a -_-")
    
elif Problema == 4:

    #*Tres varibles de tipo float
    #! si b^2-4ac >= 0 

    print("Dame los valores de a, b, c para la funcion ax^2+bx+c")
    a = float(input("Dame un numero para a: "))
    b = float(input("Dame un numero para b: "))
    c = float(input("Dame un numero para c: "))

    if (b**2)-(4*a*c) >= 0:
        print("Tiene soluciones reales ^w^!!!")
    else:
        print("No tiene soluciones reales -_-")

elif Problema == 5:

    #*Tres varibles de tipo flotante 
    #! si a > b > c 

    a = float(input("Dame un numero para a: "))
    b = float(input("Dame un numero para b: "))
    c = float(input("Dame un numero para c: "))

    if a > b and b > c: 
        print("Estan ordenados de manera estrictamente decendente ^w^!!!")
    else:
        print("No estan ordenadados ede manera estrictamamente decendente -_-")

elif Problema == 6:

    #*Una varible de tipo float
    #! n%2 = 0 o 1

    n = float(input("Dame un numero: "))
    
    if n%2 == 0:
        print("Es un numero par ^w^!!!")
    else:
        print("No es un numero par -_-")

elif Problema == 7:
    print()
elif Problema == 8:
    print()
elif Problema == 9:
    print()
elif Problema == 10:
    print()
elif Problema == 11:
    print()
elif Problema == 12:
    print()
elif Problema == 13:
    print()
elif Problema == 14:
    print()
elif Problema == 15:
    print()
else:

    print("El problema no existe XD")
    
