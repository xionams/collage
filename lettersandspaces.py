def add():
    m = 0 
    space = " "
    a = input('Input StringValue:')
    t = len(a) 
    for i in range(t):
        m=m+1
        print(a[i],end=space*m)
add()
