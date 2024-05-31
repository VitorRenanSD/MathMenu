from time import sleep

n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))

while True:
    print('''\033[0;35m   [1] SOMAR
   [2] MULTIPLICAR
   [3] MAIOR
   [4] NOVOS NUMEROS
   [5] SAIR DO PROGRAMA  \033[m''')
    sleep(0.4)
    menu = int(input('OPÇÃO DESEJADA: '))

    if menu == 1:
        print(f'{n1} + {n2} = {n1+n2}')
        sleep(1)
        print('\033[0;31mRetornando... \033[m')
        sleep(0.7)
    
    elif menu == 2:
        print(f'{n1} x {n2} = {n1*n2}')
        sleep(1)
        print('\033[0;31mRetornando... \033[m')
        sleep(0.7)

    elif menu == 3:
        if n1 > n2:
            print(f'O maior número entre eles é: {n1}')
        elif n1 < n2:
            print(f'O maior número entre eles é: {n2}')
        else:
            print('Os dois são iguais!')
        sleep(1)
        print('\033[0;31mRetornando... \033[m')
        sleep(0.7)
    
    elif menu == 4:
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
        sleep(0.5)
        print('\033[0;31mRetornando... \033[m')
        sleep(0.7)
    
    elif menu == 5:
        break
        
    elif menu != [1, 2, 3, 4, 5]:
        print('\033[0;31mDigite uma opção válida.')
        sleep(0.5)
        print('Retornando... \033[m')
        sleep(0.7)
