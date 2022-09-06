Problema = int(input("Que problema quieres resolver 1 o 2:"))

if Problema == 1:

    altura = float(input("introduce tu altura en mts:"))
    peso = float(input("introduce tu peso en kg:"))

    imc = peso / altura**2

    if imc> 18.4:
        if imc> 24.9:
            if imc> 29.9:
                print("IMC Obesidad")
            else:
                print("IMC Sobrepeso")
        else:
            print("IMC Normal")
    else :
        print("IMC Bajo")

elif Problema == 2:
    X = float(input("Introduce la cordenada en x:"))
    Y = float(input("Introduce la cordenada en y:"))

    Radio = (X**2+Y**2)**0.5

    if Radio <=1:
        print("Seccion A")
    elif Radio <=2:
        print("Seccion B")
    elif Radio <=3:
        print("Seccion C")
    elif Radio <=4:
        print("Seccion D")
    elif Radio <=5:
        print("Seccion E")
    elif Radio <=6:
        print("Seccion F")
    else:
        print("Fuera del area xd")

else:
    print("El problema no existe")
