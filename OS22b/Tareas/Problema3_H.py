import re

n = int(input())

for i in range(n):
    texto = input()
    patron = r'\([^)]+\)'
    resultado = re.sub(patron,'', texto)
    resultado = re.sub(r'\s+',' ', resultado)
    print(resultado)