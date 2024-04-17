from time import sleep

n1 = float(input('Enter the 1st number: '))
n2 = float(input('Enter the 2nd number: '))

menu = 0

while menu != 5:
    print('''\033[0;35m[1] ADD
[2] MULTIPLY
[3] LARGEST NUMBER
[4] CHOOSE NEW NUMBERS
[5] EXIT  \033[m''')
    sleep(0.6)
    menu = int(input('CHOSEN OPTION: '))

    if menu == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
        sleep(1)
        print('\033[0;31mReturning... \033[m')
        sleep(0.7)
    
    elif menu == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
        sleep(1)
        print('\033[0;31mReturning... \033[m')
        sleep(0.7)

    elif menu == 3:
        if n1 > n2:
            print('The largest number is: {}'.format(n1))
        elif n1 < n2:
            print('The largest number is: {}'.format(n2))
        else:
            print('The two numbers have the same value!')
        sleep(1)
        print('\033[0;31mReturning... \033[m')
        sleep(0.7)
    
    elif menu == 4:
        n1 = float(input('Enter 1st number: '))
        n2 = float(input('Enter 2nd number: '))
        sleep(0.5)
        print('\033[0;31mReturning... \033[m')
        sleep(0.7)

    elif menu != [1, 2, 3, 4, 5]:
        print('\033[0;31mChoose a valid option.')
        sleep(0.5)
        print('Returning... \033[m')
        sleep(0.7)
