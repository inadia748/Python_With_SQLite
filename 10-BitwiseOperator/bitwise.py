'''

&, AND, x & y.

|, OR, x | y.

^, XOR, x ^ y.


'''

x = 10
y = 8    

# binary of x
print(bin(x)) # 1010

#binary of y
print(bin(y)) #1000


print(x & y, bin(x & y)) # 8, 1000

print( x | y, bin(x | y)) # 10, 1010

print(x ^ y, bin(x ^ y)) # 2, 10

print(bin(2))


'''
x & y, when we print, we are getting the binary of x and y of & bitwise operator.

x | y, when we print, we are getting the binary of x or y of | bitwise operator.

x ^ y, when we print, we are getting the binary of x xor y of ^ bitwise operator.

'''