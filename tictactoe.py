from IPython.display import clear_output
import random

#board display
def display_board(board):
    clear_output()
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])
    print('-'+'-'+'-'+'|'+'-'+'-'+'-'+'|'+'-'+'-'+'-')
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6])
    print('-'+'-'+'-'+'|'+'-'+'-'+'-'+'|'+'-'+'-'+'-')
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])

board = [' ']*10

#choosing X or O
def player_input():
    marker = ''
    
    while marker not in ['X','O']:
        marker = input('Player 1, Choose your marker (X or O):').upper()
        if marker not in ['X','O']:
            print('Marker invalid!')

    Player1 = marker
    if Player1 == 'X':
        Player2 = 'O'
    else:
        Player2 = 'X'
    return (f'Player1 is {Player1}\nPlayer2 is {Player2}')


#choosing which player to go first
def flip_test():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

#space check if the position is empty
def space_check(board, position):
    return board[position] == ' '

#space check if the board is full
def board_space_check():
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#check the position player wants to assign the marker to
def position_check():
    choice = input('Pick a position (1-9):')

    while choice not in range(1,10) or not space_check(board,position):
        print('Sorry you did not choose a valid position, Try Again!')
        choice = input('Pick a position (1-9):')
    return int(choice)

position = position_check()


#does the user want to play again?
def play_again():
    play = ' '
    while play.upper() not in ['YES', 'NO']:
        play = input('Do you want to play again? (Yes or No):')

        if play.upper() not in ['YES', 'NO']:
            print('Command invalid, Try again!')

    if play.upper() == 'YES':
        return True
    else:
        return False

    





