n = int(input())

for i in range(n):
    nuemros = input()
    lis_nums = nuemros.split(" ")
    lis_nums = [int(x) for x in lis_nums]
    num1 = lis_nums[0]
    num2 = lis_nums[1]
    num3 = lis_nums[2]
    num4 = lis_nums[3]
    num5 = lis_nums[4]
    
    
    if (num1 * num2 + num3 - num4) == num5:
        print("("+str(num1)+"*"+str(num2)+")"+"+"+str(num3)+"-"+str(num4)+"="+str(num5))
    elif (num1 * num2 - num3 + num4) == num5:
        print("("+str(num1)+"*"+str(num2)+")"+"-"+str(num3)+"+"+str(num4)+"="+str(num5))
    elif (num1 + num2 * num3 - num4) == num5:
        print(str(num1)+"+"+"("+str(num2)+"*"+str(num3)+")"+"-"+str(num4)+"="+str(num5))
    elif (num1 - num2 * num3 + num4) == num5:
        print(str(num1)+"-"+"("+str(num2)+"*"+str(num3)+")"+"+"+str(num4)+"="+str(num5))
    elif (num1 + num2 - num3 * num4) == num5:
        print(str(num1)+"+"+str(num2)+"-"+"("+str(num3)+"*"+str(num4)+")"+"="+str(num5))
    elif (num1 - num2 + num3 * num4) == num5:
        print(str(num1)+"-"+str(num2)+"+"+"("+str(num3)+"*"+str(num4)+")"+"="+str(num5))