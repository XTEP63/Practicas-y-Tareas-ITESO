from ntpath import join
from re import A, I


Name = input("Escribe tu nombre: ")                 #Tipo de dato: Cadena de Caracteres 
lastname = input("Escribe tus apellidos:")          #Tipo de dato: Cadena de Caracteres
Age = int(input("Cual es tu edad:"))                #Tipo de dato: Entero
Expediente = int(input("Cual es tu expediente:"))   #Tipo de dato: Entero 
OringCity = input("Cual es tu ciudad de origen:")   #Tipo de dato: Cadena de Caracteres
Foring = input("Eres foraneo, si o no:")            #Tipo de dato: Cadena de Caracteres
PostalCode = input("Codigo postal:")                #Tipo de dato: Cadena de Caracteres
Hight = float(input("Cual es tu altura:"))          #Tipo de dato: Decimal 
Weight = float(input("Cual es tu peso:"))           #Tipo de dato: Decimal 
Carrera = input("Cual es tu carrera:")              #Tipo de dato: Cadena de Caracteres

for l in [Name,lastname,Age,Expediente,OringCity,Foring,PostalCode,Hight,Weight,Carrera]:
    print(l)

print(Name,lastname)
print(Expediente,Carrera)

if(Foring=="si"):
    print(OringCity,"Es foraneo")
else:
    print(OringCity,"No es forraneo")


print(str(Hight)+"mts",str(Weight)+"kg")