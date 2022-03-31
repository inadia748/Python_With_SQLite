'''

Data Types List are of two types are Numberic and Sequence and Dictionary and Set.

Numeric types are
- Integers
- Float
- Complex Numbers


Sequence types are
- String
- List
- Tuple

Dictionary

Set


'''



'''

Mutable and Immutable Data Types

mutable object can change its state or contents and immutable objects cannot.

Mutable Data Types:
- List
- Dictionary
- byte array

Immutable Data Types:
- Int
- Float
- Complex
- String
- Tuple
- Set


'''



a = 5
print(a, 'is of type', type(a))

a = 2.0
print(a, 'is of type', type(a))

a = 1 + 2j
print(a, 'is of type', type(a))




'''
A string is a collection of one or more characters put ina single quote,
double quote or triple quote.

'''


# Multiline strings can be denoted using triple quotes, ''' or " " ".


# s = "This a string" print(s)
# s = """  A multiline string """ print(s)


s = 'Hello@123'
print(s, type(s))

s = "Hello again"
print(s, type(s))


s = '''
Hello!
Welcome to Learning

'''

print(s, type(s))






'''
List is an ordered sequence of items.
It is one of the most used data type in Python and is very 
flexible
[]
a = [1, 2.2, 'swe']

'''


l = [10, 'ws', 5.5]

print(l, type(l))

l[2] = 5.1

print(l)





'''
Tuple is an ordered sequence of items same as a list.   
It is defined within parenthesis () where items are separated by 
commas.  It is immutable.

t = (5, 'process', 5 + 3j)

'''

t = (5, 'process', 5+1j)
print(t, type(t))



'''
Dictionary is an unordered collection of key-value pairs.
In python, dictionaries are defined with braces {} with aeach item being a parie in the 
form of key: values. 'key' is always unique.

d = {1: 'value1', 'key': 2}
print(d, type(d))

'''


d= {
    'name': 'Nadia',
    'age': 23,
    'course': ['Python', 'Javascript'],
}

print(d, type(d))

print(d['name'])






'''
A set is an unordered collection of items.   
Every set element is unique(no duplicates) and must be 
immutable(cannot be changed).
{}
my_set = {1, 2, 3}
print(my_set)

'''

s = {10, 20 , 10 , 15, 35}
print(s)
