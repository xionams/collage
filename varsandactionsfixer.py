def Vars():
    a = input('Sentence: ')
    make = a.split()
    for i in range(len(make)):
        t = make[i]
        new_t = t[-3:-1]+t[-1]
        if t[-1] == 'e':
            t = make[i]+'d'
            print(i+1, make[i],t)            
        elif new_t == 'eep':
            t = make[i].replace('eep','ept')
            print(i+1,make[i],t)
        else:
            t = make[i]+'ed'
            print(i+1, make[i],t)
Vars()
