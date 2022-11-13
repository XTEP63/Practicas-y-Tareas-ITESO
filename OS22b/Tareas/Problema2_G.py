
lis_contr = []
contr = ""
while contr != "end":
    contr = input()
    lis_contr.append(contr)
    
dup = {x for x in lis_contr  if lis_contr.count(x) > 1}
for i in dup:
    print(i)    