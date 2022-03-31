'''
Tuple:
A tuple in Python is similar to a list. 
The difference between the two is that we cannot change the elements of a tuple once it is assigned 
whereas we can change the elements of a list.
You cannot update or delete or insert in a tuple, which you can do in a list
'''


'''
Tuple:
It is an ordered data type
It is enclosed by a parenthesis ()
It is immutable

'''



t = (10, 20, 30, 40, 50, 10, 99, 10)

print(t)
print(type(t))

print(t[3])

# Accesing the index number of a tuple
g = t[3]
print(g)


# iterating through a tuple, we use 'for loop' to iterate through each item in a tuple

l = len(t)

print(l)

# One way of iterating a tuple
for a in range(l):
    print(a, ",", t[a])

# Another way of iterating a tuple
for a in t:
    print(a)





'''
Tuple Functions:

min()
max()
count()
index()
sum()

'''

print('\n')
minimum = min(t)
print(minimum)

maximum = max(t)
print(maximum)

c = t.count(10) # count is used to see how many times 10 is appearing in tuple 't'.
print(c)

i = t.index(50) # index is used to get the index number of an item. Here, we are finding out the index number of 50 in tuple t.
print(i)


s = sum(t) # sum is used to find the sum of all the items in a tuple, t.
print(s)


