n = int(input())
case = 'Case #'
for i in range(n):
    Counter = str(i+1)
    caso = case + Counter + ': '
    text = input().split(" ")
    tl = text[::-1]
    print(caso + (' '.join(tl)))