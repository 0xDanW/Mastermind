# TITLE: MASTERMIND
# AUTHOR: DANIEL WONG YU HENG
# DATE: 26 NOV 2020

# START

import random

# Instruction menu function
def Game_Instruction():
    while True:
        print('---------------------------------------------------------------')
        print('Instruction Menu'.center(62, ' '))
        print('---------------------------------------------------------------')
        print('(1) BRIEF OVERVIEW ON MASTERMIND')
        print()
        print('    You are required to decode a password of 4 random colours.')
        print()
        print('(2) HOW TO PLAY')
        print()
        print('    Key in 4 colours to guess the password.')
        print('    Colours can be repeated, ie. [Blue, Blue, Blue, Blue]')
        print('    Unlimited attempts until password is decoded.')
        print('    C is the number of correct colours but incorrect position.')
        print('    P is the number of correct colours and correct position.')
        print('    After >6 attempts, tips will be given every 4 attempts.')
        print()
        print('(3) GAME INTERFACE')
        print()
        print('    Example:')
        print('    Password = [Red, Green, Yellow, Blue] (*NOT SHOWN IN-GAME*)')
        print('    Enter your choice = R Y B G')
        print('    <-------------------------ATTEMPT  #02------------------------->')
        print()
        print('    AT | C P |')
        print('    01 | 2 2 |         Red        Green         Blue        Yellow  --> Attempt 1')
        print('    02 | 3 1 |         Red       Yellow         Blue         Green  --> Attempt 2')
        print()
        print('    [C] Correct colours but wrong position  : 3')
        print('    [P] Correct colours and correct position: 1')
        print('    <-------------------------------------------------------------->')
        print()
        print('(4) HOW TO WIN')
        print()
        print('    Succesfully decode the password (P = 4).')
        print('    Titles:')
        print('    If password decoded within 2 attempts: Legendary MASTERMIND.')
        print('    If password decoded within 4 attempts: Super MASTERMIND.')
        print('    If password decoded within 10 attempts: Ordinary MASTERMIND.')
        print('    If password decoded in more than 10 attempts: Rookie MASTERMIND.')
        print()
        print('GOOD LUCK DECODING THE PASSWORD, ' + str(username.upper()) + '!')
        print('---------------------------------------------------------------')
        break

# Tips function
def H_hints():
    while True:
        h_tips = input('Stuck? Need a helping tip? [y/n]: ').lower() # Prompts user for input, converted to lower case
        if h_tips == 'y':
            r = random.randint(0, 4) # Random number generated for colour index
            print('Here is your hint...')
            print('Colour', str(r + 1), 'is', str(colours[r]))
            break
        elif h_tips == 'n':
            break
        else:
            print('Invalid Input! Please enter ''y'' for YES or ''n'' for NO.')
            continue
        
game_restart = 'y'
while game_restart == 'y' or game_restart == 'Y':

    attempts = 1  # Number of attempts
    pos_correct = 0  # Number of correct colours and correct position
    col_correct = 0  # Number of correct colours but wrong position
    user_colour_index = 0  # Colour index of user input
    actual_colour_index = 0  # Colour index of randomly generated colours
    game_win = False

    attempts_list = []
    user_guess = []  # List of user input (full letters)
    actual_guess = []  # List of randomly generated colours (full letters)
    wrong_col = []  # List of wrong colours input by user
    temp = []  
    temp2 = []
    pos_list = []  # Stores P value 
    col_list = []  # Stores C value


    # Initialize MASTERMIND game
    print()
    print('\t =========================================')
    print("MASTERMIND".center(62, ' '))
    print('\t =========================================')
    print()
    username = input('Please enter your username: ')   # Prompt users for username
    while len(username) < 1:  # Data validation (Check if username is valid)
        print('Invalid name.')
        username = input('Please enter your username: ')
        continue
    print()
    print('Hello ' + str(username.upper()) + '. Welcome to the MASTERMIND game!')
    print('Are you ready to prove yourself to become a true mastermind?')
    while True:
        print('\n[S] Start Game \n[I] Instruction Menu')  # Game options
        print()
        prompt_menu = input('Enter your choice [S/I]: ').upper()  # Prompt users for option
        while prompt_menu != 'S' and prompt_menu != 'I':  # Check if user input is S or I only
            print('Invalid Input! Please enter ''S'' to start the game or ''I'' for instruction menu.')
            prompt_menu = input('Enter your choice [S/I]: ').upper()
            if prompt_menu == 'S' or prompt_menu == 'I':
                break
            else:
                continue
        print('---------------------------------------------------------------')


        # Open up Instruction Menu if user option is 'I'
        if prompt_menu == 'I':
            Game_Instruction()
            continue
        elif prompt_menu == 'S':
            break


    # Start game if user option is 'S'
    if prompt_menu == 'S':
        # Colour list
        full_colour_lst = ['Red', 'Green', 'Yellow', 'Blue', 'Pink', 'Orange']  # Colour options (full spelling)
        colour_lst = ['R', 'G', 'Y', 'B', 'P', 'O']  # Colour options (initial letters)
        colours = random.choices(colour_lst, k=4)  # 4 randomized colours and store in 'colours' list
        
        # Repeats loop until user gets all 4 colours correct (P = 4)
        while pos_correct < 4 and game_win == False:
            print()
            print('---------------------------------------------------------------')
            print('User Menu'.center(62, ' '))
            print('---------------------------------------------------------------')
            print('Enter code using single letters.')
            print('(R) RED | (G) GREEN | (Y) YELLOW | (B) BLUE | (P) PINK | (O) ORANGE')
            print('Example: RED GREEN YELLOW BLUE ---> R G Y B (Not Case Sensitive)')
            print('---------------------------------------------------------------')
            
            print(colours) #--> Shows the actual colours for testing purposes
            
            answer = (input('Enter your choice of 4 colours = ').upper())  # Accept user input and store in 'answer' variable
            # Convert 'answer' variable into a list and store user input
            # Format and standardise user input into a fixed form, ie. (RGYB)
            if answer.__contains__(' '):  
                answer = list(answer)
                num_of_spaces = answer.count(' ')
                for q in range(0, num_of_spaces):
                    answer.remove(' ')
            else:
                answer = list(answer)

          
            # Data validation (Check is user input is appropriate)
            # Checks for user inputs which are not letters AND input is not 4-unit long
            if (all(colours in colour_lst for colours in answer) == False) and (len(answer) != 4):  
                print()
                print('Invalid code length! Please enter 4 colour codes.')
                wrong_col = []  
                for x in range(0, len(answer)):
                    if (answer[x] not in colour_lst):
                        wrong_col.append(answer[x])  # Places wrong user input into 'wrong_col' list
                print(wrong_col,' is not available in the colour list.')
                continue

            # Checks for user inputs which are not letters OR input is not 4-unit long        
            elif (all(colours in colour_lst for colours in answer) == False) or (len(answer) != 4):
                if (all(colours in colour_lst for colours in answer) == False):  
                    wrong_col = []
                    for x in range(0, 4):
                        if (answer[x] not in colour_lst):
                            wrong_col.append(answer[x])  # Places wrong user input into 'wrong_col' list
                    print()
                    print(wrong_col,'is not available in the colour list.')
                    continue
                elif len(answer) != 4:  
                    print()
                    print('Invalid code length! Please enter a 4 colour code.')
                    continue


            # Converts user input (initial letter) to full letters and store in 'user_guess'
            temp = []
            for c in range(0, 4):
                user_colour_index = 0
                user_colour_index = colour_lst.index(answer[c])
                temp.append(full_colour_lst[user_colour_index])
            user_guess.append(temp)
                
            temp2 = []
            for d in range(0, 4):
                actual_colour_index = 0
                actual_colour_index = colour_lst.index(colours[d])
                temp2.append(full_colour_lst[actual_colour_index])
            actual_guess.append(temp2)


            # Checks if any of the user input matches with the randomly generated colours
            pos_correct = 0
            col_correct = 0


            # Check input values which are correct colour and correct position (P value)    
            for p in range(0, 4):
                if (answer[p] == colours[p]): 
                    pos_correct += 1

                    # Prevent repeated colours to be counted twice
                    answer[p] += '-'
                    colours[p] += '-'
                else:
                    pos_correct = pos_correct

                    
            # Check input value which are correct colour but wrong position (C value)      
            for p in range(0, 4):
                if (answer[p] != colours[p]) and (answer[p] in colours): 
                    col_correct += 1
                    colours[colours.index(answer[p])] += '-'
                else:
                    col_correct = col_correct

            # Removes the '-' from previous attempts
            for p in range(0, 4):
                if len(colours[p]) > 1:
                    colours[p] = (colours[p])[0]

            pos_list.append(pos_correct)
            col_list.append(col_correct)


            # Display colours input by users (full letters)
            print()
            print('<------------------------ ATTEMPT #' + ("%02d" % attempts) + ' ------------------------>')
            attempts_list.append(attempts)
            print('AT | C P |')
            for p in attempts_list:
                print(("%02d" % p), '|', col_list[p - 1], pos_list[p - 1], '|', end = ' ')
                for e in range(0, 4):
                    print("%11s" % user_guess[p - 1][e], end = ' ')
                print()
            print()
            print('[C] Correct colours but wrong position  : ' + str(col_correct))
            print('[P] Correct colours and correct position: ' + str(pos_correct))
            attempts += 1


            # After 6 attempts, every 4 attempts user will be requested if tips are needed
            if (attempts > 5) and (user_guess != actual_guess) and game_win == False:
                if attempts % 4 == 0:
                    print()
                    H_hints()
            print('<------------------------------------------------------------->')
            print()


        # Win game
        # Display final message
        game_win = True

        # Title decision for user based on number of attempts
        if attempts <= 2:
            title = 'Legendary MASTERMIND'
        elif attempts <= 4:
            title = 'Super MASTERMIND'
        elif attempts <= 10:
            title = 'Ordinary MASTERMIND'
        else:
            title = 'Rookie MASTERMIND'
        
        print()
        print('<<----------------------- GAME ENDED ------------------------>>')
        print()
        print(('CONGRATULATIONS ' + str(username.upper()) + '!!').center(62, ' '))
        print('. . . . .'.center(62, ' '))
        print()
        print(('PASSWORD DECODED IN ' + str(attempts - 1) + ' ATTEMPTS.').center(62, ' '))
        print('. . . . .'.center(62, ' '))
        print()
        print(('YOU HAVE OFFICIALLY ACHIEVED THE TITLE <' + title + '>!').center(62, ' '))
        print('. . . . .'.center(62, ' '))
        print()

        # Requests if user wants to play again
        repeat = 1
        while repeat == 1:
            game_restart = input('Would you like to play again to gain a better title? [y/n]: ').lower()
            if game_restart == 'y':
                break
            elif game_restart == 'n':
                repeat = 2
        if repeat == 2:
            break

print()
print('<<<---------------------------------------------------------->>>')
print()
print('Thank you for playing! See you next time =D !')
quit()

# END











    
