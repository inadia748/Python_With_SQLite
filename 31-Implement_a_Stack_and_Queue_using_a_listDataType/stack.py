l = []

while True:
    c = int(input('''
        1  Push Elements
        2  Pop Elements
        3  Peek Elements
        4  Display Elements
        5  Exit
    '''))
    if c == 1:
        n = input('Enter the value')
        l.append(n)
        print(l)
    
    elif c == 2:
        if len(l) == 0:
            print('Empty String: ')
        else:
            p = l.pop()
            print('Deleted Element :', p)
            print('The list is: ', l)
    
    elif c == 3:
        if len(l) == 0:
            print('Empty Stack')
        else:
            print('Last element of Stack is: ', l[-1] )
    
    elif c == 4:
        print("Display Stack: ", l)

    elif c == 5:
        break;
    
    else:
        print('Invalid choices: choose 1 or 2 or 3 or 4 or 5')

        
        

