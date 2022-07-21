from time import clock_settime
from turtle import position
from IPython.display import clear_output
import random

#board display
def display_board(board):
    clear_output(wait=True)
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])
    print('-'+'-'+'-'+'|'+'-'+'-'+'-'+'|'+'-'+'-'+'-')
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6])
    print('-'+'-'+'-'+'|'+'-'+'-'+'-'+'|'+'-'+'-'+'-')
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])

#choosing X or O
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



#choosing which player to go first
def flip_test():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


#check the position player wants to assign the marker to
def position_check(board):
    position = int(input('Pick a position (1-9):'))

    while position not in range(1,10) or not space_check(board,position):
        print('Sorry you did not choose a valid position, Try Again!')
        position = int(input('Pick a position (1-9):'))
    return position


#space check if the position is empty
def space_check(board, position):
    return board[position] == ' '

#space check if the board is full
def board_space_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#positioning the marker
def placing(board, position, mark):
    board[position] = mark

#win conditions
def win_condition(board, mark):
    return ((board[7] == board[8] == board[9] == mark)
     or (board[4] == board[5] == board[6] == mark)
     or (board[1] == board[2] == board[3] == mark)
     or (board[1] == board[4] == board[7] == mark)
     or (board[2] == board[5] == board[8] == mark)
     or (board[3] == board[6] == board[9] == mark)
     or (board[3] == board[5] == board[7] == mark)
     or (board[1] == board[5] == board[9] == mark))



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
    



#loop to keep running the game
print('Welcome To Tic Tac Toe!')
while True:
    the_board = [' ']*10
    Player1, Player2 = player_input()
    turn = flip_test()
    print(f'{turn} will go first')
    play_game = input("Ready to play? (Y or N):").upper()
    while play_game not in ['y', 'n', 'Y', 'N']:
        print('Invalid input, Type (Y or N)!')
        play_game = input("Ready to play? (Y or N):").upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player1':
                #board shown
            display_board(the_board)
                #choose a position
            position = position_check(the_board)
                #placing marker to the required position
            placing(the_board, position, Player1) 
                #checking if they won
            if win_condition(the_board,Player1) == True:
                    display_board(the_board)
                    print('Congrats, Player1 won!')
                    game_on = False
            else:
                    #when game is tied
                if board_space_check(the_board) == True:
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player2'
        else:
            #board shown
            display_board(the_board)
            #choose a position
            position = position_check(the_board)
            #placing marker to the required position
            placing(the_board, position, Player2) 
            #checking if they won
            if win_condition(the_board,Player2) == True:
                display_board(the_board)
                print('Congrats, Player2 won!')
                game_on = False
            else:
                #when game is tied
                if board_space_check(the_board) == True:
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player1'


    #loop out 
    if not play_again():
        break




