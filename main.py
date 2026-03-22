"""
Momen Alhejoj
malhe
March 16, 2025
"""

# imported modules (random & colors)
from wordleUtils import getRed, getGreen, getGray, getYellow
import random



option_to_play = "" # global var. to allow user input if they want to play or not 




#                                          whats does this function do?
#   
#   This function starts off by applying an empty string to color_text, then a for-loop iterates over the
#   length of users guess. If the character of user guess at that specific index i, matches the character of 
#   the secret word at index i then that specifc character is added to color_text in the color green. if the
#   character of user guess at the specific index i, is in the secret word somewhere, then that character is 
#   added to color_text, but in red. Otherwise, if the character of user guess at index i is completely not
#   in the secret word, then the character is added to color_text, but in grey. Once the loop is complete,
#   the full string of color_text is returned to the function that had called it.
def  getColorTextResult(secret_word, user_guess):

    color_text = ""

    for i in range(len(user_guess)): # iterates based on the length of user guess (5 times since Wordle accepts a 5-letter word)
        if user_guess[i] == secret_word[i]:
            color_text += getGreen(user_guess[i]) # adds the letter in green
        elif user_guess[i] in secret_word:
            color_text += getRed(user_guess[i]) # adds the letter in red
        else:
            color_text += getGray(user_guess[i]) # adds the letter in grey

    return color_text # returns the full composed string with the colored letters that were 'appended'





#                                          whats does this function do?
# 
#   This function begins by opening the file and reading its lines into one list of strings, then in order to
#   add new strings into a list, a new list can be created to not mess with the originals file information.
#   Once that is set, then a for loop iterates over each string in the list, and for each string its stripped,
#   meaning new-lines are removed, but then its appended to the new list. The for-loop will repeat until
#   its done with all the strings in the original file, afterwards it will return the new file to the original
#   function that had called it.
def getWordList(filename):

    open_file = open(filename)
    file_list = open_file.readlines() # creates a list of strings

    new_file = [] # empty list

    for item in range(len(file_list)): # for every string in the 10k word list it will do:
        stripped_version = file_list[item].strip() # strip new-lines at the specific index
        new_file.append(stripped_version)    # append() the string to the new file since '+=' can be 
                                             # used on strings strictly and not files

    return new_file # returns the newly composed file with the stripped words





#                                          whats does this function do?
#
#   This function starts off with an empty string to ensure entry into the while loop, and the loop will
#   repeat while the user inputs' character lenght is not equal to 5 OR if the users guess is not in the
#   valid word list (the file with available words), then the loop asks for the user input. Once that is 
#   entered, the users guess is turned into upper case to check if its in valid word list -- if its true 
#   then the guess is returned to te function that called it, otherwise, the user has to re-enter another
#   guess.
def getValidGuess(valid_word_list):

    user_guess = ""

    while len(user_guess) != 5 or user_guess not in valid_word_list:

        print('-'*90)
        print()

        user_guess = input("guess a word: ") # asks for user word input here
        user_guess = user_guess.upper()

        if user_guess in valid_word_list: # no need to check if the length is 5 since if the user input
            return user_guess             # matches a word in the valid list then by logic the length is 5
        else:
            print()
            print(getRed(' inavlid option.. ❌ '))
            print()
            print('it seems like your option \ndoes not exist.. try again, \nand type a 5-letter word!')
            print()
            



        
#                                          whats does this function do?
#   
#   This function is more of a fun/user-interactive function which allows them to play the game or not,
#   if the user inputs specifically a 'yes', then their promted with an input asking for their user/name, and 
#   once that is entered, then a print statement explains what the user should do in order to win the game.
#   Otherwise, if they input a 'no', then the game ends there by printing out a silly message, and to take
#   into ccount other possible inputs, it would require the user to start again by inputing a valid option 
#   such as a yes or no.
def welcomePlayer():
    print('-'*90)
    print()
    print(getGreen(' WELCOME to pythons immitated wordle world! 🎊 '))
    print()
    print("Do you want to test your \nguessing game against \npythons wordle world 🥳")
    print()

    global option_to_play # refering to the global variable in order to be able to alter a side-effect
    option_to_play = input("do you accept the challenge, yes or no: ")
    print()
    username = ""
    print('-'*90)

    if option_to_play == 'yes':
        print()
        print(getGray(" AMAZING CHOICE 👀 "))
        print()
        print('we will need a few more \ninformation to give you \nthe best environment!')
        print()
        print('-'*90)
        print()
        username = input("whats your name: ")
        print()
        print('-'*90)
        print()
        print(f'{getYellow(username.capitalize())} 🤩 \ngoodluck in your round \nyou will need to guess \nthe word within 6 attempts!') 
        print()
    elif option_to_play == 'no':
        print()
        print(getGray(' oh okay.. 😔 '))
        print()
        print('are you really that scared \nto test your skills \nout against python ')
        print()
    else:
        print()
        print(getGray(' inavlid option.. ❌ '))
        print()
        print('it seems like your option \ndoes not exist.. try again')
        print()
        welcomePlayer()
        




#                                          whats does this function do?
#
#   This function is specifically what runs the whole game, since in the function, it includes calls to other
#   functions that return a specific value. The while loop will keep on repeating while the user is between
#   a round less than 6 AND while the users guess is not the actual secret word that their attemtping 
#   to guess. 0nce either value becomes 'false', then the while loop ends there -- if they guessed the 
#   secret word, a win message is printed out, otherwise, a lose message is printed out  
def playWordle():

    round_num = 0
    word_list = getWordList("wordleWords.txt") # calls the function which returns a new stripped list of words
    secret_word = random.choice(word_list) # uses the list to randomly pick a word in the list 
    user_guess = "" 
    
    while round_num < 6 and user_guess != secret_word:
        round_num += 1
        user_guess = getValidGuess(word_list) # returns the user guess uppercase if their guess is valid
        print(getColorTextResult(secret_word, user_guess)) # colors the users guess based on the secret word
        print()
    if user_guess == secret_word:
        print('-'*90)
        print()
        print(getYellow(" WINNER 🥇: "))
        print(f'congrats, you guessed the correct word within {round_num} attempts! 🎉')
    else:
        print('-'*90)
        print()
        print(getRed(" LOSER 👻: "))
        print(f'oh no, you reached your set attempts, \nthe secret word was: {getGray(secret_word)}.. 😕')

if __name__ == "__main__":
    welcomePlayer()
    if option_to_play == 'yes':
        playWordle()

 #  using the function welcomePlayer() to get user input if they want to play, 
 #  and the game continues from there since I was unable to have the playWordle()
 #  function call the welcomePlayer() function inside, since the 'submit for grading' was
 #  coded specifically to play the game instantly w/ no barriars -- once the user 
 #  inputs their choice, if its strictly yes then the game continues from there
 #  otheriwse, the side effect will be whatever the welcomePlayer() included based on other 
 #  inputs.