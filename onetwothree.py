# get x and check if x == 0
while True:
    try:
        x = int(input("type num here: "))
        if x == 0:
            # if true print 1,2,3 else print just x and ask again.
            for x in range(1,4):
                print(x)
            break    
        else:
            print(x, 'is not 0')
        
    except ValueError:
        print('value only could be number')

