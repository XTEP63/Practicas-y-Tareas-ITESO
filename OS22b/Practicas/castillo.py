WallLength = float(input())

wallWidth = float(input())

r1 = float(input())

r2 = float(input())

x = float(input())
if(x < 0):
    x = x * -1
y = float(input())
if(y < 0):
    y = y * -1

if((x-(WallLength/2))**2 + (y-(WallLength/2))**2 < r1**2):
    print("Sobre las torres.")
elif((x-(WallLength/2))**2 + (y-(WallLength/2))**2 < r2**2):
    print("Sobre las paredes.")
elif((WallLength/2)-(wallWidth/2) <= x <= (WallLength/2)+(wallWidth/2) and 0 <= y <= (WallLength/2)):
    print("Sobre las paredes.")
elif((WallLength/2)-(wallWidth/2) <= y <= (WallLength/2)+(wallWidth/2) and 0 <= x <= (WallLength/2)):
    print("Sobre las paredes.")
elif(x <= (WallLength/2)-(wallWidth/2) and y <= (WallLength/2)-(wallWidth/2)):
    print("Dentro del castillo.")
else:
    print("Fuera del castillo.")
    