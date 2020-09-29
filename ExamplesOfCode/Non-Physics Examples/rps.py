from random import choice

def rps():
#   Setting up the Rock, Paper, and Scissors values, also getting the user and computer inputs
    x = input('Enter R, P, or S: ')
    R = ['r', 'R']
    P = ['p', 'P']
    S = ['s', 'S']
    cpu = ['R', 'P', 'S']
    y = choice(cpu)
    print('CPU chose ' + y)
#   User picks rock
    if x in R:
#   Outcomes
        if y in R:
            print('Draw')
        elif y in P:
            print('You lose')
        elif y in S:
            print('You win')
#   User picks Paper
    elif x in P:
#   Outcomes
        if y in R:
            print('You win')
        elif y in P:
            print('Draw')
        elif y in S:
            print('You lose')
#   User picks Scissors
    elif x in S:
#   Outcomes
        if y in R:
            print('You lose')
        elif y in P:
            print('You win')
        elif y in S:
            print('Draw')
    else:
#   In case a value that isn't meant to be entered is entered
        print('That was not Rock, Paper, or Scissors, dummy')
#   User deciding to continue playing
    playagain = input('Enter E to play again (or anything else to stop playing): ')
    if playagain == 'e' or playagain == 'E':
        return rps()
    else:
        return 'Thanks for playing!'

print(rps())
        
          
