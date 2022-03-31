print('''
+ Add
- Subtract
* Multiply
/ Divide
''')


num1 = int(input('Enter value1: '))
num2 = int(input('Enter value2: '))

opr=input('Enter your chosen operator: ')

if opr == '+':
    print(num1 + num2)
elif opr == '-':
    print(num1 - num2)
elif opr == '*':
    print(num1 * num2)
elif opr == '/':
    print(num1 / num2)
else:
    print('You have entered another operator, the operator must be *, -, +, /')



