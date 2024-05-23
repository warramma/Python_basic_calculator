#5-23-24
#improved calculator, can choose basic operator

print('Welcome to your new and improved calculator! \nYou may now choose what operation you would like me to perform!!!')

sentinel = 'Y'

while(sentinel.lower() == 'y'):
    num1 = float(input('Enter your first number: '))
    op = input('Enter + - / or x for your desired operation: ')
    num2 = float(input('Enter your second number: '))

    print(str(num1) + ' ' +  op + ' '+ str(num2) + ' is: ')

    if(op == '+'):
        print(num1+num2)
    elif(op == '-'):
        print(num1 - num2)
    elif(op == '/'):
        if(not(num1==0) and num2 == 0):
            print('This operation cannot be completed :)')
        else:
            print(num1 / num2)
    elif(op.lower() == 'x'):
        print(num1 * num2)
    else:
        print('Please enter one of the four operations :)')
    
    sentinel = input('Enter Y to continue using the calculator and N to stop: ')

print('Thank you for using the calculator :)')