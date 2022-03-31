'''
Functionf for Delete Element from List-
Del
Remove
Pop
Clear
'''

# del
# del deletes the element you want to remove from the list. It works on the indexes of the list
l = [20, 30, 50, 60]

print(l)

del l[1]

print(l)



# pop
# pop also deletes the element you want to remove from the list. It returns the deleted item from the list, whereas 'del' do not return the deleted item

p = [20, 30, 50, 60]
deletedItem = p.pop(2)
print('The deleted item from list p is', deletedItem)
print(p)




# remove
# remove also deleted the element you want to remove. It works on the values, you want to remove.


r = [20, 30, 50, 60]

r.remove(30)
print(r)



# clear
# clear removes the whole elements from the list. It gives you an empty list

c = [20, 30, 50, 60]
c.clear()
print(c)




# update

u = [20, 30, 40, 50]
u[0] = 90
print(u)


# insert

i = [20, 30, 40, 50]
i.insert(0, 10)
print(i)



# append
# you can append list, tuple and  dictionary

a = [20, 30, 40, 50]
a.append(60)
print(a)

a.append(['apple', 'banana']) # appending a list
print(a)



# extends

e = [20, 30, 40, 50]
o = 9
e.extend([60, 70, o])
print(e)


