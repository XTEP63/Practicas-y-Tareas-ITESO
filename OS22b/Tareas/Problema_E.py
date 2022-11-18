datos=input()

y= datos.split(" ")

alturam=float(y[0])
distpollo=float(y[1])
velocipollo=float(y[2])
velocihorizo=float(y[3])

tiempo=(alturam/((1/2)*9.81))**(1/2)

r=(distpollo+(tiempo*(velocihorizo-velocipollo)))/velocipollo

f=3

for i in range(len(str(r))):
    if str(r)[i]!=".":
        f+=1
    else:
        break
if int(str(r)[f])>5 and r>0:
    r+=0.01
if int(str(r)[f])>5 and r<0:
    r-=0.01
print(str(r)[0:f])