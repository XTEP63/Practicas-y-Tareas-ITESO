import ipaddress

def IPAddress(IP:str):
    return "Private" if ipaddress.ip_address(IP).is_private else "Public"

red = input("IP: ")
mac = input("mascara: ")
separador = "."
lista_red = red.split(separador)
lista_red = [int(x) for x in lista_red]
b = input("Ip b: ")
p = bin(int(ipaddress.IPv4Address(red)))
m = bin(int(ipaddress.IPv4Address(mac)))
p = p[2:]
m = m[2:]
print("Ip:",p)
print("Mascara:",m)
print(IPAddress(red))

Proced_and = ""
for i in range(len(p)):
    if p[i] == "0" or m[i] == "0":
        Proced_and = Proced_and + "0"
    else:
        Proced_and = Proced_and + "1"
print("Proceso Y:",Proced_and)

print("Domino brocast:",ipaddress.IPv4Network(b,strict=False).broadcast_address)

if lista_red[0] <= 127:
    Clase = "Clase A"
    I_red = str(lista_red[0]) 
    host = str(lista_red[-1]) + "." + str(lista_red[-2]) + "." + str(lista_red[-3])
    masca = "255.0.0.0"
elif lista_red[0] <= 191:
    Clase = "Clase B"
    I_red = str(lista_red[0]) + "." + str(lista_red[1])
    host = str(lista_red[-1]) + "." + str(lista_red[-2])
    masca = "255.255.0.0"
elif lista_red[0] <= 223:
    Clase = "Clase C"
    I_red = str(lista_red[0]) + "." + str(lista_red[1]) + "." + str(lista_red[2])
    host = str(lista_red[-1])
    masca = "255.255.255.0"

print(Clase)
print("ID de red:",I_red)
print("Host:", host)
print("Mascara:", masca)

#* clase A 0-127 8 bits de red 24 host
#* clase B 128-191 16bits de red 16 host
#* clase c 192-223 24bits de red 8 host 
