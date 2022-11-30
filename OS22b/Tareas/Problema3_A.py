ax1=int(input())
ay1=int(input())
ax2=int(input())
ay2=int(input())
bx1=int(input())
by1=int(input())
bx2=int(input())
by2=int(input())
o=0
if bx1>ax1 and bx1<ax2:
    if by1<ay1 and by1>ay2:
        if bx2>ax1 and bx2<ax2:
            if by2<ay1 and by2>ay2:
                o+=1
elif bx1<ax1 and bx2>ax2:
    if by1>ay1 and by2<ay2:
            o+=1

if o!=0:
    print(False)
else:
    print(True)