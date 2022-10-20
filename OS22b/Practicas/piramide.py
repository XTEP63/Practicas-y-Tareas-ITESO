n=int(input())
li=[""]*n
for i in range(n):
    tex=input()
    li[i]=tex.split(" ")
for i in range(len(li)-1):
    x=n-i-2
    for a in range(len(li[x])):
        val1=int(li[x][a])+int(li[x+1][a])
        val2=int(li[x][a])+int(li[x+1][a+1])
        if(val1>=val2):
            li[x][a]=val1
        else:
            li[x][a]=val2
print(li[0][0])