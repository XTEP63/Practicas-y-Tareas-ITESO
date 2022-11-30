filas=int(input())
columnas=int(input())
x=int(input())
y=int(input())
movimientox=int(input())
movimientoy=int(input())
k=int(input())

for i in range(k):
    x+=movimientox
    y+=movimientoy
    if x>filas-1 or x<0:
        movimientox*=(-1)
        x+=movimientox
    if y>columnas-1 or y<0:
        movimientoy*=(-1)
        y+=movimientoy
print(str(x)+","+str(y))
    
    
    
    