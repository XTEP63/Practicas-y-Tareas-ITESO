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
