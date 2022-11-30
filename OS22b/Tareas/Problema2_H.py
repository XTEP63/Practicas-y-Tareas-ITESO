levels = int(input())
list = []
for i in range(levels):
    counter = str(i + 1)
    c= i+1
    list.append(counter)
    listWP = ''.join(list)
    list_reversed = list[::-1]
    list_reversed.pop(0)
    list_reversedWP = ''.join(list_reversed)
    if i > 0:
        print(listWP + list_reversedWP)
    else:
        print(listWP)