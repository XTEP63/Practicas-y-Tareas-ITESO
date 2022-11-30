casos = int(input())
separador = " "

def LoS_Sq (LoShu):
    LoShu = [int(x) for x in LoShu]
    Lo_num = []
    fil_1 = sum(LoShu[0:3])
    fil_2 = sum(LoShu[3:6])
    fil_3 = sum(LoShu[6:])
    col_1 = LoShu[0]+LoShu[3]+LoShu[6]
    col_2 = LoShu[1]+LoShu[4]+LoShu[7]
    col_3 = LoShu[2]+LoShu[5]+LoShu[8]
    dig_1 = LoShu[0]+LoShu[4]+LoShu[8]
    dig_2 = LoShu[6]+LoShu[4]+LoShu[2]
    
    Lo_num.append(fil_1)
    Lo_num.append(fil_2)
    Lo_num.append(fil_3)
    Lo_num.append(col_1)
    Lo_num.append(col_2)
    Lo_num.append(col_3)
    Lo_num.append(dig_1)
    Lo_num.append(dig_2)
    return Lo_num.count(15)
    
for i in range(casos):
    Cuadrado = input()
    LoShu = Cuadrado.split(separador)
    if LoS_Sq(LoShu) == 8:
        print("True")
    else:
        print("False")
            
    