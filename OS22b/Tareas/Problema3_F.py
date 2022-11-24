cami=int(input())
for i in range (cami):
    p=int(input())
    ud=input()
    niv=0
    valle = 0
    for j in ud:
        if (j=="U"):
            niv+= 1
            if (niv==0):
                valle+=1
        else:
            niv-=1

    print(valle)