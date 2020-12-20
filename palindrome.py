def Palindrome():
    data = input('Enter a word or a sentence: ')
    data = data.lower()
    make_data = data.split() # dic of words
    
    for i in range(1):
        new_data = data.replace(" ","")
        if new_data[::-1] == new_data:
            print('Cool - this is a palindrome!')
        else:
            print('Sorry - not a palindrome.')    
    
Palindrome()
