from IPython.display import clear_output


def display_board(board):
    clear_output()
    print(board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])
    print('-'+'-'+'|'+'-'+'-'+'-'+'|'+'-'+'-')
    print(board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6])
    print('-'+'-'+'|'+'-'+'-'+'-'+'|'+'-'+'-')
    print(board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])


board = [' ']*10


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
print(player_input())

