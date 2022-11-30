levels = int(input())
N = int(input())

for i in range(N):
    S = str(input())
    S_upper = S.upper()
    val1 = S_upper.count('A')
    val2 = S_upper.count('E')
    val3 = S_upper.count('I')
    val4 = S_upper.count('O')
    Val5 = S_upper.count('U')
    P = val4 + val3 + val2 +val1 +Val5
    print(val1,val2,val3,val4,Val5)