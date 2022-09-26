

while True:
    num = int(input("Dame un numero: "))
    while num > 9:
        num = sum(map(int, str(num)))
        print(num)
'''

#Estupidez de regalado 
num = 234567890
getOutfromJailCard=False
def GetOutOfJail(getOutFromJailCard):
    if getOutFromJailCard == True: return True
    else:
        return False

while not GetOutOfJail(getOutfromJailCard):
    num = sum(map(int, str(num)))
    if len(str(num))==1:
        getOutfromJailCard= True

print(num)

'''