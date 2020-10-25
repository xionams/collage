while True:
    try:
        x = int(input("num? :"))
        if x > 0:
            print(x)
            break
        else:
            print(x-x-x)
            break
    except ValueError:
        print('num! is a shortcut of number! this value must be an integer')
