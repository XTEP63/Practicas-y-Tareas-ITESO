while True:
    
    num1 = int(input())
    if num1 == 0:
        break  
    
    num2 = int(input())
    
    if (num1 % num2) == 0:
        print("Es posible.")
    else:
        print("No es posible.")