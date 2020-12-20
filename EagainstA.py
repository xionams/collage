def AvsE():
    sen = input('Enter a sentence: ')
    make = sen.split()
    counter_a = 0
    counter_e = 0
    
    for i in range(len(make)):
        new = make[i].lower()
        a = new.count("a")
        e = new.count("e")       
        if a > e: 
            counter_a+=1
        elif a < e:
            counter_e+=1

    if counter_a > counter_e:
        print("A is won the game",counter_a,'-',counter_e)
    elif counter_a < counter_e:
        print("E is won the game",counter_e,'-',counter_a)
    else:
        print('its a draw',counter_a,'-',counter_e)

AvsE()
