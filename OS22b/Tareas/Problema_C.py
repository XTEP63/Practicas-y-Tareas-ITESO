while True:
    try:
        num_1 = input()
    except :
        break
    
    if num_1 == "0" or num_1 == "":
        break
    num_1 = int(num_1)
    num_2 = int(input())   
    
    if num_1 + num_2 > 100:
        print("")
    elif (num_1 + num_2) % 2 == 0:
        print("pacusticos")
    else:
        print("impacusticos")
        
        
        

