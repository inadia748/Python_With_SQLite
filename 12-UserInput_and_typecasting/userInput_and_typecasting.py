'''
input
int
float
eval, it can work int, float and binary. You do not need to put 'int' or 'float' to convert a data

'''

a = input('Enter any value: ')
print(a, type(a))

b = int(input('Enter a value: '))
print(b, type(b))

c = float(input('Enter a vlaue: '))
print(c, type(c))

print(c + b)

#0b1010 is a binary of 10
x = eval(input('Enter a value of x: ')) # 10 or 0b1010
y = eval(input('Enter a value of y: ')) # 20 

print(x + y) # 30


