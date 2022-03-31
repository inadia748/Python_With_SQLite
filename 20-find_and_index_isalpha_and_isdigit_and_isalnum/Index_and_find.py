w = 'Welcome'

print(w.find('e')) # gives the index of 'e'. It finds where it finds first.

print(w.find('e', 2)) # gives the index of 'e'. It will start searching from the index 2.

print(w.find('z')) # -1, because 'z' is not present.

print(w.find('z', 2)) # -1, it will start searching from index 2. 'z' is not present that is -1


print(w.index('c')) # gives the index number of a character, you want.

print(w.index('z')) # you get an error in the output


'''
Difference between 'find' and 'index' is that 
'find' will give -1, if the character you are searching for is not present
whereas 'index' will give an error if the character you are searching for is not present.

'''