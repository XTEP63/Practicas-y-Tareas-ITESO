import ipaddress

red = input("IP: ")
mac = input("mascara: ")
p = bin(int(ipaddress.IPv4Address(red)))
m = bin(int(ipaddress.IPv4Address(mac)))
p = p[2:]
m = m[2:]
print("Ip:",p)
print("Mascara:",m)

Proced_and = ""
for i in range(len(p)):
    if p[i] == "0" or m[i] == "0":
        Proced_and = Proced_and + "0"
    else:
        Proced_and = Proced_and + "1"
print("Proceso Y:",Proced_and)


