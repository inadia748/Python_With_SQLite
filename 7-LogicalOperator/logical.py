'''
When you have more than 1 condition, you use logical operator.

and, Return True if both statements are true, x < 5 and x < 10.

or, Return True if one of the statements is true, x < 5 or x < 10.

not, Reverse the result, returns False if the result is true,  not(x < 5 and x < 10)


'''


x = 10
y = 20

print(x == 10 and x < y)

print(x == 10 and x < y and x == y)

print(x != 10 or x < y or x == y)

print(x != 10)

print(not x != 10)