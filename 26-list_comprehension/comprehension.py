'''
List comprehension is an elegant way to define and create list based on existing list

List comprehension is generally more compact and faster than normal functions and loops for
creating list.
'''

l = []

for a in range(1,101):
    print(a)

print('\n')

for b in range(1, 101, 2):
    print(b)



# list comprehension
print('\n')
for a in range(1, 101):
    l.append(a)

print(l)

print('\n')

n = [m for m in range(1,101)]

print('n = ',n)


# list comprehension can be used for filtering

f = [h for h in range(1, 101) if (h%2==0)]

print('f = ', f)




# list comprehension example

print('\n')
s = 'hello'

d = [g for g in s]

print('d= ', d)