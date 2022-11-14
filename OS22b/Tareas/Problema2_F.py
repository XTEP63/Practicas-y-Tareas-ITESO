"""
n = int(input())

for i in range (n):
    m_n = input()
    lis_m_n = m_n.split(" ")
    lis_m_n = [int(x) for x in lis_m_n]
    secuencias = lis_m_n[0]
    lon = lis_m_n[1]
    lista_secuecias = []
    for j in range(secuencias):
        Secuencia = input()
        lista_secuecias.append(Secuencia)
    for k in range(secuencias-1):
        if lista_secuecias[k] < lista_secuecias[k+1]:
            minimo = lista_secuecias[k]
        else:
            minimo = lista_secuecias[k+1]
    print(minimo)
"""
repet=int(input())
for i in range(repet):
    entr=input()
    en=entr.split(" ")
    cadenas=int(en[0])
    longitud=int(en[-1])
    cad=[]
    cf=[]
    cfinal=""
    for c in range(cadenas):
        cad.append(input())
    for s in range(longitud):
        l=[]
        for g in range(cadenas):
            l.append(cad[g][s])
        A=l.count("A")
        C=l.count("C")
        G=l.count("G")
        T=l.count("T")
        if A>=C and A>=G and A>=T:
            cf.append("A")
        if C>A and C>=G and C>=T:
            cf.append("C")
        if G>A and G>C and G>=T:
            cf.append("G")
        if T>A and T>G and T>C:
            cf.append("T")
    for Z in range(len(cf)):
        cfinal=cfinal+cf[Z]
    print(cfinal)