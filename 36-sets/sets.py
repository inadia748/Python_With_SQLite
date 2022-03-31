'''
Sets:

A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

However, a set itself is mutable. We can add or remove items from it.

Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.


'''

'''
Set is unordered, unindexed and encloses by curly braces {}.

'''

'''
Functions of Set:

set()
add()
pop()
remove()
update()
clear()
discard()

'''




# converting list to set

l = [10, 20, 30]
s = set(l)

print(l, type(l))
print(s, type(s))


# converting tuple to set

t = (1, 30, 9)
s = set(t)

print(t, type(t))
print(s, type(s))


# add

s2 = {10, 20, 30}
s2.add(40)
print(s2, type(s2))


# pop, set does not have index. pop() will randomly delete any item in the set.

s3 = {10, 99, 50, 75}
print(s3, type(s3))
s3.pop()
print(s3)



# remove

s4 = {10, 500, 89, 30}
print(s4)
s4.remove(500)
print(s4)



# discard

s4.discard(89)
print(s4)



# clear

s5 = {3,10,7,5}
s5.clear()
print(s5)


# update, you are adding list to a set

set2 = {1, 0, 5}
list2 = [30,40, 90]
tuple2 = (33)

print(set2)

set2.update(list2)

print(set2)





