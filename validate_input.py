def user_choice():
    choice = 'Wrong'
    acceptable_range = range(0,11)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input('Enter a number (0-10):')

        if choice.isdigit() == False:
            print('Sorry that is not a digit!')
        
        elif choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry, you are out of acceptable range!')
                within_range = False
    return int(choice)
print(user_choice())
