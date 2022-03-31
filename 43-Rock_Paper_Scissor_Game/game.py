import random

l = ['rock', 'scissor', 'paper']

'''
rock vs paper -> paper wins
rock vs scissors -> rock wins
paper vs scissor -> scissor wins

'''

while True:
    ccount = 0  # computer point count
    ucount = 0 # user point count
    uc = int(input('''
    Game Start----
    1 YES
    2 NO | Exit
    '''))
    if uc == 1:
        for a in range(1,6):
            print('Round ', a)
            userInput = int(input('''
            1 Rock
            2 Scissor
            3 Paper  
            '''))

            if userInput == 1:
                uchoice = 'rock'
            elif userInput == 2:
                uchoice = 'scissor'
            elif userInput == 3:
                uchoice = 'paper'
            
            Cchoice = random.choice(l)
            

            if Cchoice == uchoice:
                print('User Choice:  ',uchoice)
                print('Computer Choice: ',Cchoice)
                print('Game Draw')
                ucount = ucount + 1
                ccount = ccount + 1

            elif (uchoice == 'rock' and Cchoice == 'scissor') or (uchoice == 'paper' and Cchoice == 'rock') or (uchoice == 'scissor' and Cchoice == 'paper'):
                print('User Choice:  ',uchoice)
                print('Computer Choice: ',Cchoice)
                print('User Wins !!!')
                ucount = ucount + 1
            
            else:
                print('User Choice:  ',uchoice)
                print('Computer Choice: ',Cchoice)
                print('Computer Wins!!!')
                ccount = ccount + 1
            
            print('-------------------------')

        if ucount == ccount:
                print('It is a draw!!!')
                print('The points are the same by: ', ucount)
            
        elif ucount > ccount:
                print('User Wins finally!!')
                print('User wins by ', ucount, ' points')
        else:
            print('Computer wins finally!!!')
            print('Computer wins by,', ccount, ' points')       

            
    else:
        break