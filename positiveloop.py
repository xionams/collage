number = int(input('num: '))
for i in range(0,number+1):
    if i % 2 == 0:
        print(i)
    
gen = sum(i for i in range(0,number+1) if i % 2 == 0)
print('the sum is :',gen)
