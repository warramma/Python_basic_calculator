#review basic calculator, just to code something

#OBJECTIVE - make a calculator that runs the four basic operations AND modulo AND exponent
# --choose your operator
# --type in like you would a regular calculator
# operator overload?
# ....how would i do that in C++?   





print('You have opened the calculator...')
print('You have six options:')
print('+    -   x   /   ^   %')
sentinel = 'Y'
#result = 0

while (sentinel.lower()=='y'):
    num1 = float(input('Enter a number: '))
    op = input('operator: ')
    num2 = float(input('Next number: '))
    if(op=='+'):
        #sum
        print(num1 + num2)
    elif(op == '-'):
        #difference
        print(num1-num2)
    elif(op.lower() == 'x'):
        #product
        print(num1 * num2)
    elif(op == '/'):
        #quotient
        if(num1 > 0 and num2 == 0):
            print('invalid input')
        else: 
            print(num1 / num2)
    elif(op == '^'):
        #power
        print(num1 * num2)
    elif(op == '%'):
        #modulo
        print(num1 % num2)
    sentinel = input('enter N to stop, Y to continue: ')

print('have a nice day :)')
    
