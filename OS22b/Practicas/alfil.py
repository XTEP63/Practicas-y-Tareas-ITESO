fil=int(input())
col=int(input())
positionx=int(input())
positiony=int(input())
movementx=int(input())
movementy=int(input())
movemts=int(input())

lista=[["" for j in range(fil)] for k in range(col)]

for i in range(movemts):
    
    if positionx + movementx in range(0,len(lista[0])):
        positionx += movementx
    else:
        positionx -= movementx
            
            
        
    if positiony + movementy <= len(lista) and positiony + movementy >= 0:
        positiony += movementy
    else: 
        movementy *= -1
        
print("("+str(positionx)+","+str(positiony)+")")
        
    
    
    
    