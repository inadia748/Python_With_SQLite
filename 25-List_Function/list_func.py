'''
Function for Delete Element from List-
del
pop()
remove()
clear()

'''

l = [20, 30, 50, 60]

print(l)

# del works on index:

del l[1]
print(l)


# difference between del and 'pop' is pop returns the deleted item while 'del' does not return the deleted item.

print('\n')
l2 = [20, 30, 50, 60, 70]

print(l2)

deletedItem = l2.pop(2)
print('The deleted item from the list is ', deletedItem)

print(l2)


print('\n')
# 'remove' works on the item you want to remove

l3 = [20, 30, 50, 900, 2]

print(l3)

l3.remove(900)

print(l3)



# 'clear' just empties the entire list, it means it removes all the items from the list
print('\n')
l4 = [10, 35, 100, 50, 90, 19, 25]
print(l4)
l4.clear()
print(l4)







'''
Update Element from the List-
l = [20, 30, 40, 50]
l[0] = 10
print(l)

'''
print('\n')
li = [20,30, 50, 60]
print(li)
li[0] = 90  # Updating the 0th element in the list from 20 to 90

print(li)







'''
Function for Update Element from List-
insert()
append()
extends()

'''

print('\n')

# insert('position', 'value')

li2 = [20, 30, 50, 60, 90]
print(li2)
li2.insert(0, 90) # inserting 90 in the '0th position'
print(li2)

li2.append(120)
print(li2)

al = [53, 93]
li2.append(al)
li2.append(20)
print(li2)

li2.extend([53,93])
print(li2)