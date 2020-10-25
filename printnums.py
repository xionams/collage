while True:
    try:
        x = int(input('number: '))
        if x > 0:
            z = x+1
            for i in range(0,z):
                print(i)
            break
        else:
            z = x
            for i in range(z,0):
                print(i)
            break
            
    except ValueError:
        print('must be an Number!')
            
