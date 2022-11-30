cicle = 1
while cicle != 0:
    total=int(input())
    if total==0:
        break
    base = int(input())
    list = []
    final = 1
    list.append(1)
    list.append(1)
    while final<total:
        final = final*base
        list.append(final)
        list.append(final)
    for i in range(len(list)-1,0,-1):
        if list[i]<=total:
            total-=list[i]
    if total==0 or total==1:
        print("Es posible.")

    else:
        print("No es posible.")