import random

# computer random number

Cnumber = random.randrange(1,101) # gives you random number from 1 to 100.
print(Cnumber)

userInput = int(input('Enter your number between 1 to 100 ---'))

if userInput > Cnumber:
    print('Computer Number ', Cnumber )
    print('Your guess number is too hign')
elif userInput < Cnumber:
    print('Computer Number ', Cnumber )
    print('your guess number is too low')
else:
    print('your guess number is equal')