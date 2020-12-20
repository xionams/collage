def UpperLower():
    a = input('Some English String: ')
    b = a.capitalize()

    for i in range(len(b)):
        
        if i%2 == 0: # if positive
            make = b[i].upper()
            print(make,end='')
        else: 
            make = b[i].lower()
            print(make,end='')

UpperLower()
