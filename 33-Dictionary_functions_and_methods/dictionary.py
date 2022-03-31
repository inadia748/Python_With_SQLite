'''
Dictionary Functions

get()
keys()
values()
items()

Delete ---> del() and pop() uses key to delete
dict()
update()
clear()
insert()

'''


d = {
    'course': 'Python',
    'fees': 8000,
    'duration': '2 months',
}

# get function
g = d.get('course')
print(g)

# directly accessing the value instead of using get function
c = d['course']
print(c)


# keys function

for a in d.keys():
    print(a)


# values function

for a in d.values():
    print(a)



# items function

for a, b in d.items():
    print(a, ' : ', b )


# del

del d['fees'] # deleting  key 'fees' from dictionary d
print(d)


# pop

d.pop('duration')

print(d)




# dict(), it is used to create a dictionary. Another way of creating dictionary

d1 = dict(name = 'python', fees = 8000, duration= '3 months' )
print(d1)


# update
d1.update({'fees': 10000})
print(d1)


# clear

d1.clear()
print(d1)



#insert
d2 = dict(name = 'Python', fees = 10000, duration = '5 months')
d2['descript'] = 'This is a Python course'

print(d2)





