position_list = [0,1,2]

def display_game(position_list):
    print(f"Here is the list of positions:\n{position_list}")

display_game(position_list)

def position_check():
    choice = input('Pick a position (0-2):')

    while choice not in ['0','1','2']:
        print('Sorry you did not choose a valid position, Try Again!')
        choice = input('Pick a position (0-2):')

    return int(choice)

position_index = position_check()

def replacement_choice(gamelist,position_index):
    user_placement = input 