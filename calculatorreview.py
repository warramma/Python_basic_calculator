print('Welcome to the basic calculator :) Enter any two numbers to perform the four basic operations:')
firstNum = float(input('Enter your first number: '))
secondNum = float(input('Enter your second number: '))

sum = firstNum + secondNum
difference = firstNum - secondNum
product = firstNum * secondNum
if firstNum !=0 and secondNum == 0:
    quotient = 'undefined'
else:
    quotient = firstNum / secondNum

print(str(firstNum) + ' + ' + str(secondNum) + " = " + str(sum))
print(str(firstNum) + ' - ' + str(secondNum) + " = " + str(difference))
print(str(firstNum) + ' x ' + str(secondNum) + " = " + str(product))
print(str(firstNum) + ' / ' + str(secondNum) + " = " + str(quotient))