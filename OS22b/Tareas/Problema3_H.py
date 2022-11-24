repeats=int(input())
for a in range(repeats):
    oracion=input()
    string = ""
    dentroDeParentesis = 0
    for n in range(len(oracion)):
        if oracion[n] == "(":
            dentroDeParentesis += 1
        elif oracion[n] == ")":
            dentroDeParentesis -= 1
        if(dentroDeParentesis==0 and oracion[n]!=")"):
            string+=oracion[n]
    print(string)