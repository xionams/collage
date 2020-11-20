def salary():
    name = input('enter your name: ')
    rate = int(input('enter your rate: '))
    hours = float(input('enter your hour per day: '))
    days = int(input('enter how much days you work this month: '))
    r = hours*rate*days
    b = days*20
    print(name, "your monthly salary is:", r+b," NIS")
salary()
