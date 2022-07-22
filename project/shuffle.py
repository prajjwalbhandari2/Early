from random import shuffle
mylist = [' ', '0', ' ']
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
final = shuffle_list(mylist)
def player_guess():
    guess = ''
    while guess not in ['1', '2', '3']:
        guess = input("Pick a number (1, 2 or 3):")
    return int(guess)
guessed = player_guess()

#comment also correct:

def check_order(final,guessed):  
    if final[guessed] == 'O': #mylist[guessed] == "O" 
        print("Congratulations, You are Correct!")
    else:
        print('Sorry, better luck next time!')
        print("The correct order is", final) #final ko thauma {mylist}
check_order(final,guessed)


