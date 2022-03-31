
#https://www.askpython.com/python/list/iterate-through-list-in-python
# range (start, stop, step])

l = [1, 2, 3, 4]
print(l[-1])
print(l[-1::-1])

list = [10, 20, 30, 40, 60, 80, 90]


print('\n ***List Iteration Method 1:*** ')
for n in list:
    print(n)

length = len(list)

print('\n The length is :', length)

for n in range(length):
    print(n, ' : ', list[n])

for n in range(0, 3):
    print(n, list[n])


for n in range(5):
    print(n)

for n in range(0,5):
    print(n)

for n in range(0, 5, 2):
    print(n)

                # 7-1, 0, decrement by -1
for a in range(length-1, -1, -1):
    print(a, ':', list[a])


