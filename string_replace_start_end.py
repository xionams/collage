def replace():
    a = input('Input StringValue: ')
    print('The Original StringValue is: ',a)
    print('The Request StringValue is:',a[-1]+a[1:-1]+a[0])
    print('The First letter:',a[0],'is Replaced by The Last Letter:',a[-1])
replace()
