attemps = 0
print('3 attempts only :P')

while attemps < 3:
    password = input('\nEnter your password: ')
    if  password == 'Password': #Password Here
        print()
        print('Welcome!')
        print()
        print('Here is the list:')
        print('------')
        print('Place Holder')
        print('Place Holder')
        print('Place Holder')
        print('Place Holder')
        print('Place Holder')
        print('------')
        print('End.')
        break
    else:
        print('\nWrong password')
        attemps += 1
        continue
