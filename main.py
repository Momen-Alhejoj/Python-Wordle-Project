"""
Momen Alhejoj
"""

from wordleUtils import getRed, getGreen, getGray, getYellow
import random



option_to_play = ""

def  getColorTextResult(secret_word, user_guess):

    color_text = ""

    for i in range(len(user_guess)): #
        if user_guess[i] == secret_word[i]:
            color_text += getGreen(user_guess[i]) 
        elif user_guess[i] in secret_word:
            color_text += getRed(user_guess[i]) 
        else:
            color_text += getGray(user_guess[i]) 
            
    return color_text 


def getWordList(filename):

    open_file = open(filename)
    file_list = open_file.readlines() 

    new_file = [] 

    for item in range(len(file_list)):
        stripped_version = file_list[item].strip() 
        new_file.append(stripped_version)    

    return new_file 


def getValidGuess(valid_word_list):

    user_guess = ""

    while len(user_guess) != 5 or user_guess not in valid_word_list:

        print('-'*90)
        print()

        user_guess = input("guess a word: ") 
        user_guess = user_guess.upper()

        if user_guess in valid_word_list: 
            return user_guess             
        else:
            print()
            print(getRed(' inavlid option.. ❌ '))
            print()
            print('it seems like your option \ndoes not exist.. try again, \nand type a 5-letter word!')
            print()
            

def welcomePlayer():
    print('-'*90)
    print()
    print(getGreen(' WELCOME to pythons immitated wordle world! 🎊 '))
    print()
    print("Do you want to test your \nguessing game against \npythons wordle world 🥳")
    print()

    global option_to_play 
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
        

def playWordle():

    round_num = 0
    word_list = getWordList("wordleWords.txt") 
    secret_word = random.choice(word_list)
    user_guess = "" 
    
    while round_num < 6 and user_guess != secret_word:
        round_num += 1
        user_guess = getValidGuess(word_list) 
        print(getColorTextResult(secret_word, user_guess)) 
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
