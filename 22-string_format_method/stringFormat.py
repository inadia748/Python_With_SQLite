# named indexes
from turtle import clear


tx1 = 'Welcome to {fname} {lname}'.format(fname= 'W', lname='Learning')
print(tx1)

#numberd indexes
tx2 = 'Welcome to {0} {1}'.format('Wtech', 'Learning')
print(tx2)


#empty placeholders:
tx3 = 'Welcome to {} {}'.format('WTech', 'Learning')
print(tx3)


w = "Welcome {} to {} WLearning". format('Program', 20)
print(w)

t = 'Welcome to {0} to {1} '. format('WLe', 'Angle')
print(t)

p = 'Welcome to {f} to {l}'.format(l='Learning', f='W')
print(p)

s = 'Welcome {a} to {b} Wscube'. format(a = 30, b = 40)
print(s)

s = 'Welcome {b:11} to {a}'. format(a = 'di', b=20) # b:11 indicates it takes up 11 spaces
print(s)

s = 'Welcome {b:^11} to {a}'. format(a = 'di', b=20) # b:11 indicates it takes up spaces inbetween of b.
print(s)

s = 'Welcome {b:>11} to {a}'. format(a = 'di', b=20) # b:11 indicates it takes up 11 spaces
print(s)


s = 'Welcome {b:<11} to {a}'. format(a = 'di', b=20) # b:11 indicates it takes up 11 spaces
print(s)



# https://www.w3schools.com/python/ref_string_format.asp

'''
<
10------

^
----10----

>
--------10

'''
