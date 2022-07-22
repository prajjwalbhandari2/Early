'''mistake'''


from turtle import position
from IPython.display import clear_output
import random
def display_board(board):
    clear_output()
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])
    print('-'+'-'+'-'+'|'+'-'+'-'+'-'+'|'+'-'+'-'+'-')
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6])
    print('-'+'-'+'-'+'|'+'-'+'-'+'-'+'|'+'-'+'-'+'-')
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])

def player_input():
    marker = ''
    
    while marker not in ['X','O']:
        marker = input('Player 1, Choose your marker (X or O):').upper()
        if marker not in ['X','O']:
            print('Marker invalid!')

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, position, marker):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark)
     or (board[4] == board[5] == board[6] == mark)
     or (board[1] == board[2] == board[3] == mark)
     or (board[1] == board[4] == board[7] == mark)
     or (board[2] == board[5] == board[8] == mark)
     or (board[3] == board[6] == board[9] == mark)
     or (board[3] == board[5] == board[7] == mark)
     or (board[1] == board[5] == board[9] == mark))

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = int(input('Pick a position (1-9):'))

    while position not in range(1,10) or not space_check(board,position):
        print('Sorry you did not choose a valid position, Try Again!')
        position = int(input('Pick a position (1-9):'))
    return position

def replay():
    play = ' '
    while play.upper() not in ['YES', 'NO']:
        play = input('Do you want to play again? (Yes or No):')

        if play.upper() not in ['YES', 'NO']:
            print('Command invalid, Try again!')

    if play.upper() == 'YES':
        return True
    else:
        return False

print('Welcome to tic tac toe!')

while True:
    the_board = [' ']*10
    Player1, Player2 = player_input()
    turn = choose_first()
    print(turn + 'will go first!')
    play_game = input('Ready To play? (y or n):')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,position, Player1)
            if win_check(the_board,Player2):
                display_board(the_board)
                print('Congrats, Player2 won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    game_on = False
                else:
                    turn = 'Player2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,position, Player2)
            if win_check(the_board,Player2):
                display_board(the_board)
                print('Congrats, Player2 won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    game_on = False
                else:
                    turn = 'Player1'




    if not replay():
        break
