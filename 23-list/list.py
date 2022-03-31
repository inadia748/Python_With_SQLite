# list is mutable. It can store integers, strings, floats etc.
# list has indexing element for each element.

# https://www.programiz.com/python-programming/list


grocery = ['Harpic', 'vimbar', 'deodrant', 'eggplant', 'chocolatbar']
print(grocery[2])
print(grocery)

l = [10, 30, 40, 50, 'hello']

print(l)
print(l, type(l))
print(l[3], l[4])




# Lst[ Initial : End(excluded) : IndexJump ] for list slicing.

print(l[0:2])

print(l[0:3])

print(l[1:])
print(l[3:])

print(l)
print(l[0::2])

print(l[-1::-1])
print(l[-1:-3:-1])

print(l[-1::-2])



# Initialize list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# Show original list
print("\nOriginal List:\n", List)
 
print("\nSliced Lists: ")
 
# Display sliced list
print(List[3:9:2])
 
# Display sliced list
print(List[::2])
 
# Display sliced list
print(List[::])