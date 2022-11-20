from statistics import mode

n_digits = int(input())
digits = input().split(" ")
digits.sort()
answer = mode(digits)
print(answer)