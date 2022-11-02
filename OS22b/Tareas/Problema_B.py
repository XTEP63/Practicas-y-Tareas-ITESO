
Num_Alumnos = int(input())

def Rounded(Calificacion):
    return ((Calificacion%5)-5)*-1

for i in range(Num_Alumnos):
    Calificacion = int(input())
    
    if Calificacion < 38:
        print(Calificacion)
    elif Rounded(Calificacion) < 3:
        print(Calificacion + Rounded(Calificacion))
    else:
        print(Calificacion)
        



