w = 'Welcome to Wlearning'

l = len(w)

print(l)


for a in range(l):
    print(a, w[a])


print('\n')
# Reverse for string iteration

reverse1 = w[-1::-1]
print(reverse1)

length1 = len(reverse1)
print(length1)

for a in range(length1):
    print(a, reverse1[a])



print('\n')
#Another way of reversing for string iteration

for a in range(l-1, -1, -1):
    print(w[a])