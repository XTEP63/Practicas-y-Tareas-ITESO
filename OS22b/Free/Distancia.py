from math import asin, cos, radians, sin, sqrt

x1 = float(input(""))
y1 = float(input(""))
x2 = float(input(""))
y2 = float(input(""))
r = 6371.01

x1 = radians(x1)
y1 = radians(y1)
x2 = radians(x2)
y2 = radians(y2)

d = 2*r*asin(sqrt((sin((x2-x1)/2))**2+(cos(x1)*cos(x2)*((sin((y2-y1)/2))**2))))

print(round(d))
