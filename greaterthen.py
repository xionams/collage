while True:
    x = int(input('(x) value: '))
    y = int(input('(y) value: '))

    try:
        if x > y:
            print(x,'>',y)
            break
        if x < y:
            print(y,'>',x)
            break
        if x == y:
            print(x,'==',y)
            break            
    except ValueError:
        print('Must be an Int number!\n')
