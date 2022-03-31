'''
Different methods of list are:
1. count
2. max
3. min
4. sort
5. reverse
6. index
'''




# count

l = [10, 20, 30, 50, 10, 20, 20]

# we are counting how many times '10' has appeared in list l.

c = l.count(10)

print('The number of elements in a list l is: ', len(l))
print('The number of "10" appearing in list l is: ', c)
print('The number of "20" appearing in the list l is: ', l.count(20))



# max
print('\n')
m = max(l)
print('The maximum value appearing in the list l is: ', m )

a = ['Hello', 'World']
print('The maximum value in list a: ', max(a)) # the maximun is calculated on the basis of ASCII value in alphabets.


# min

print('\n')
minimum = min(l)
print('The minimum in list l: ', minimum)
print('The minimum in list a: ', min(a))




# sort
# It will be in ascending order by default
print('\n')
li = [10, 2, 5, 7, 9, 10]
print('The list in li before sorting: ', li)
li.sort() # the list will be sorted in ascending order. It will bring changes to the list. The change is permanent.
print('The list after sorting: ', li)


# revere
# It will reverse the list

li2 = [2, 5, 68, 90, 10, 8]
al = ['Al', 'Zerox', 'Banana', 'Tarot']

print('\n The list in l2 is: ', li2)
li2.reverse() # reverse method is used and the change will be permanent in the list l2.
print('\n The reverse of li2 is: ', li2)

print('The list in al is: ', al)
al.reverse()
print('The reverse in list al: ', al)



# index
# it will give the index of the items in a list

l3 = ['Jameson', 'Nadia', 'Ali']
print('\n', l3)
i = l3.index('Nadia')
i2 = l3.index('Ali')
print('The index of "Nadia" in list l3 is :', i)
print('The index of "Ali" in list l3 is :', i2)


