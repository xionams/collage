# get x and print 3x
def three():
    x = int(input("type num here: "))
    print(x+x+x)
    return three()
three()
