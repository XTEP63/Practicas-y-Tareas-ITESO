n=int(input("Hatsa que numero queries calcular la secuncia de Fibonacci: "))

first=0
second=1
sum=0
count=1
print("La secuencia de Fibonacci: ")
while(count<=n):    
  print(sum)
  count+=1
  first=second
  second=sum
  sum=first+second