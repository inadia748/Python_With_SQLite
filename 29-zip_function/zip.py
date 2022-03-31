# zip function
# zip function is used to iterate over 2+ lists at the same time.

'''
The zip() function takes iterables (can be zero or more), 
aggregates them in a tuple, and returns it.

'''

l1 = [10, 20, 40, 50] # 4 items in l1
l2 = [3, 4, 77, 88]   # 4 items in l2

for a, b in zip(l1,l2):
    print(a,b) # in zip, it will print the output parallely

print('\n')

t = len(l1)

for h in range(t):
    print(h," #### ",  l1[h], "####", l2[h])



    






l3 = [1, 5, 83, 9, 1000] # 5 items in l3
l4 = [33, 25, 85, 99, 3, 75] # 6 items in l4


'''
When you use zip function to iterate on l3 and l4, 
it will give the output parallely. l3 has 5 items,
while, l4 has 6 items. So, It will parallely give 
5 items each from l3 and l4. It wil ignore the 5th index
from l4 lists. 

In simple words, indexes from 0 to 4 of l3 list and 
indexes from 0 to 4 of l4 list will be printed parallely, ignoring the 
5th index of l4 list.

'''
print('\n')
for c, d in zip(l3, l4):
    print(c, d)
