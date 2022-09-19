number = int(input( "Dame un número: "))
i = 2
toggle = 0

if number%2 == 0:
    print("No es primo")
else:
    while i < number**0.5:
        if(number%i == 0):
            toggle = 1
            print ("No es primo ")
            break
        else:
            i = i+1
    if toggle == 0:
        print ("Es primo")

