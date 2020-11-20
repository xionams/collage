value1 = int(input("your month: "))
value2 = int(input("this month: "))

print((value1-value2)*0.12)
i = 12-value2+value1

if i > 12:
    print(i-12)

else:
    print(i)



