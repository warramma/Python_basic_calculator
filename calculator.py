#5/13/2024
#Basic calculator using Python

print('Welcome! I am a basic calculator.')
print('Enter any two numbers and see the results!')

first_number = float(input('First number: '))
second_number = float(input('Second number: '))
sum = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
quotient = first_number / second_number

print(str(first_number) + ' + ' + str(second_number) + ' = ' + str(sum))
print(str(first_number) + ' - ' + str(second_number) + ' = ' + str(difference))
print(str(first_number) + ' x ' + str(second_number) + ' = ' + str(product))
print(str(first_number) + ' / ' + str(second_number) + ' = ' + str(quotient))