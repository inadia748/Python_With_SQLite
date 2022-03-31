'''
Dictionary:
Dictionary in Python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types 
that hold only a single value as an element, 
Dictionary holds key:value pair. 
Key-value is provided in the dictionary to make it more optimized.

Note – Keys in a dictionary don’t allow Polymorphism.

'''

'''
Dictionary is an undordered data type. It has 
key-value pairs and it is enclosed by a curly braces.
The key is always unique.

'''


d = {
    'name': 'python',
    'fees': 8000,
    'duratiion': '2 months'
}

print(d)
print(type(d))

f = d['fees']
print(f)


for n in d:
    print(n, " : ", d[n])
