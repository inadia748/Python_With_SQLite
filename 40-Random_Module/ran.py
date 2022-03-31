import random


n = random.randint(2,8)
print(n)


n2 = random.randrange(2,5)
print(n2)


l = [10, 20, 30, 99]
lc = random.choice(l)
print(lc)


r = random.random() # it will return float values between 0 and 1
print(r)

print('\n')
l2 = [10,20,30,40]
print(l2)
random.shuffle(l2)
print(l2)


u = random.uniform(3,9)
print(u)