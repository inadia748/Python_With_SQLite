s = {10, 20, 30, 40}

print(s, type(s))


# iterate

for a in s:
    print(a)


list1 = [10,20,30,40]
set1 = set(list1)

print(set1)




#remove
set2 = {10,20,30,40,50}
set2.remove(20)
print(set2)

#set2.remove(99) # it will give an error since 99 is not present in the set 'set2'.
#print(set2)



# discard

set3 = {10,30, 40, 90, 50}
set3.discard(50)
print(set3)


# pop, it will randomly delete an element in a set. But for list, it will delete from the last element and it depends on the index.

set4 = {10, 20, 50, 90, 33, 439}
print(set4)
deletedItem = set4.pop()
print(deletedItem)
print(set4)


# clear

set5 = {10,30,50}
set5.clear()
print(set5)




# add, it will add new elements to the set

set6 = {10,20,30,89}
set6.add(60)
l = [95, 'abc', 100]
print(set6)


# update
l = [90,30, 89, 33, 40]
set6.update(l)
print(set6)

