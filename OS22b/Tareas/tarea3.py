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

    #*Dos variables de tipo float
    #! x o y = 0

    x = float(input("Dame un numero para x: "))
    y = float(input("Dame un numero para y: "))

    if x == 0 or y == 0:
        print("El punto se encuetra en uno de los ejes ^w^!!!")
    else:
        print("El punto no esta en ninguno de los ejes -_-")

elif Problema == 8:

    #*Una varible de tipo enterp
    #! Pow(n,1/2) = 0 

    n = int(input("Dame un numnero para n: "))
    
    if n%(n**0.5) == 0:
        print("Tiene raiz cuadrada exacta ^w^!!!")
    else:
        print("No tiene Raiz cuadrada exacta -_-")

elif Problema == 9:

    #*Tres variables de tipo entero
    #! c^2 = a^2 + b^2 o b^2 = c^2 + b^2 o a^2 = c^2 + b^2

    A = float(input("Dame un numero para a: "))
    B = float(input("Dame un numero para b: "))
    C = float(input("Dame un numero para c: "))

    if C**2 == A**2 + B**2:
        print("Pueden fomar un triangulo rectangulo de la forma: c hipotenusa, a y b catetos ^w^!!!")
    elif B**2 == A**2 + C**2:
        print("Pueden fomar un triangulo rectangulo de la forma: b hipotenusa, a y c catetos ^w^!!!")
    elif A**2 == B**2 + C**2:
        print("Pueden fomar un triangulo rectangulo de la forma: a hipotenusa, b y c catetos ^w^!!!")
    else:
        print("No pueden formar un triangulo rectangulo -_-")

elif Problema == 10:

    #*Tres variables de tipo float 
    #! x^2 + y^2 <= r^2 

    x = float(input("Dame un numero para la cordenada x: "))
    y = float(input("Dame un numero para la cordenada y: "))
    r = float(input("Dame le radio de la circunferencia: "))

    if x**2 + y **2 <= r**2:
        print("El punto esta dentro de la circunferencia ^w^!!!")
    else:
        print("El punto no esta dentro de la circunferencia -_-")

elif Problema == 11:

    #*Una varible de tipo float
    #! n > o n = 0 o n < 0 

    n = float(input("Dame un numero real: "))

    if n > 0: 
        print("Es positivo ^w^!!!")
    elif n < 0: 
        print("Es negativo -_-")
    else:
        print("Es cero -_-")

elif Problema == 12:

    #*Una varible de tipo entero
    #! e > 17, e > 60

    e = int(input("Cual es tu edad"))

    if e < 18: 
        print("Eres menor de edad ^w^!!!")
    elif e < 60:
        print("Eres un adulto ^w^!!!")
    else:
        print("Eres de la tercera edad ^w^!!!")

elif Problema == 13:
    
    #*Tres varibles de tipo entero 
    #! a < b y a < c, b < a y b < c, c < a y c < b

    a = float(input("Dame un numero para a: "))
    b = float(input("Dame un numero para b: "))
    c = float(input("Dame un numero para c: "))

    if a < b and a < c:
        print("a es el menor ^w^!!!")
    elif b < a and b < c:
        print("b es el menor ^w^!!!")
    elif c < a and c < b: 
        print("c es el menor ^w^!!!")
        
elif Problema == 14:
    print()
elif Problema == 15:
    print()
else:

    print("El problema no existe XD")
    
