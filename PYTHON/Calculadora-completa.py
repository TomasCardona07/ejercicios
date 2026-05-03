print('welcome to our calculator')
print('choose operation')
print("""[+] for plus
[-] for subtract
[X] for multiplication
[%] for division""")
operation = str(input('choose=')).lower().strip()
while operation != 'x' and operation != '-' and operation != '+' and operation != '%':
    print('incorrect, please input the operation again')
    operation = str(input()).lower().strip()
if operation == '+':
    print('input how numbers do you want to do')
    print('number most be in 1-5')
    numbersPlus = int(input())
    while numbersPlus <= 0 or numbersPlus>5:
        if numbersPlus <= 0:
            print('number most be positive')
        else:
            print('number do not be bigger than 5')
        numbersPlus = int(input())
    contadorPlus = 0
    for contador in range(1,numbersPlus+1):
        print(f'input the {contador} number for to realize the operation')
        num = int(input())
        while num < 0:
            print(f'the number can not be negative, input the number {contador} again')
            num = int(input())
        contadorPlus = contadorPlus + num
    print(f'the result of operation is:{contadorPlus}')
elif operation == '-':
    print('input how numbers do you want to do')
    print('number most be in 1-5')
    numbersMinus = int(input())
    while numbersMinus <= 0 or numbersMinus>5:
        if numbersMinus <= 0:
            print('number most be positive')
        else:
            print('number do not be bigger than 5')
        numbersMinus = int(input())
    contadorSubtract = 0
    for contador in range(1,numbersMinus+1):
        print(f'input the {contador} number for to realize the operation')
        num = int(input())
        while num < 0:
            print(f'the number can not be negative, input the number {contador} again')
            num = int(input())
        if contador == 1:
            contadorSubtract = num
        else:
            contadorSubtract = contadorSubtract - num
    print(f'the result of operation is:{contadorSubtract}')
elif operation == 'x':
    print('input how numbers do you want to do')
    print('number most be in 1-5')
    numbersMulti = int(input())
    while numbersMulti <= 0 or numbersMulti>5:
        if numbersMulti <= 0:
            print('number most be positive')
        else:
            print('number do not be bigger than 5')
        numbersMulti = int(input())
    contadorMulti = 0
    for contador in range(1,numbersMulti+1):
        print(f'input the {contador} number for to realize the operation')
        num = int(input())
        while num < 0:
            print(f'the number can not be negative, input the number {contador} again')
            num = int(input())
        contadorMulti = contadorMulti * num
    print(f'the result of operation is:{contadorMulti}')
elif operation == '%':
    print('input how numbers do you want to do')
    print('number most be in 1-5')
    numbersDiv = int(input())
    while numbersDiv  <= 0 or numbersDiv >5:
        if numbersDiv <= 0:
            print('number most be positive')
        else:
            print('number do not be bigger than 5')
        numbersDiv = int(input())
    contadorDiv = 0
    for contador in range(1,numbersDiv+1):
        print(f'input the {contador} number for to realize the operation')
        num = int(input())
        while num < 0 or num==0:
            if num<0:
                print(f'the number can not be negative, input the number {contador} again')
                num = int(input())
            else:
                print(f'number can not divide by 0, input number {contador} again')
                num = int(input())
        contadorDiv = contadorDiv * num
    print(f'the result of operation is:{contadorDiv}')