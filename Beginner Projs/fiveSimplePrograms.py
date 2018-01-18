'''
Created by Drew Morton
Last Editted: 01/18/18

I created this program to practice learning Python!
Enjoy!!  

'''


# amodule PHP code to call a function that's name is stored in a String 
#import amodule

import random

# Select Program is similar to a home screen for the multiple programs and will allow you to play each one 
def select_program():
    print ("Select a program:")

    prog_tup = ("Dice Roller", "Guess the Number", "Mad Libs", "Text Based RPG", "Hangman")

    i = 1
    for x in prog_tup:
        print ("Option {}: {}".format(i, x))
        i = i + 1

    var = int(input("Option: "))
    
    #Ensures users answer is correct    
    while var < 1 or var > 5:
        print("{} is an invalid option".format(var))
        var = int(input("Option: "))
    
    prog_option = prog_tup[var - 1]

    print ("\nYou chose ", prog_option)
    if var == 1:
        dice_roller()
    elif var == 2:
        guess_number()
    elif var == 3:
        mad_libs()
    elif var == 4:
        text_rpg()
    elif var == 5:
        hangman()
    else:
        print("Option doesnt exist")
        select_program()

# Select New Program will appear at the end of each game so that once the user decides to leave 
# the program they originaly chose
def select_new_program():
    var = input("\nDo you want to select another program? \n(Y/N) ")
    if var.lower() == "y":
        select_program()
    else:
        print("NOOO COME BACK!!!!")
        quit()

# Simulates rolling a dice
# TODO: allow user to select which type of die they wish to roll
def dice_roller():
	
    min = 1
    max = 20

    print("Welcome to Dice Roller!")
    print("\nDo you want to roll the d20")
    play_var = input("Y/N : ")

    while (play_var.lower() == 'y'):
        d20 = random.randint(min, max)
        print("D20 Roll: {}".format(d20))
        play_var = input("Roll again?")
    print ("Thank you for playing Dice Roller!")
    select_new_program()



# Prob need to put these in separate file
def guess_number():

    min = 1
    max = 100
    count = 1    
    random_gen_number = random.randint(min,max)

    #print(random_gen_number)

    print("\nWelcome to Guess the Number!!")
    print("Guess which number I've chosen between 1 and 100!")
    guess = int(input("Guess: "))
    
    #print(random_gen_number)
    
    while random_gen_number != guess:
        if random_gen_number < guess:
            print("You guessed too HIGH")
        else:
            print("You guessed too LOW")
        count += 1
        guess = int(input("Guess: "))
    else:
        print("Congratulations you have guessed the correct number in {} tries. My number was {}".format(count,random_gen_number))
    print ("Thank you for playing Dice Roller!")   
    select_new_program()

def mad_libs():
    print("Welcome to Mad Libs")
    #print("\nSorry Mad Libs is still under construction.")
    a = input("What is your name?\n")
    b = input("Why are you playing this game?\n")
    c = input("w?\n")
    d = input("What kind of pet do you want?\n")
    print("\nHello {}. How are you?\n Aww I'm sorry to hear your {} got you sick".format(a,d))
    print("On the good note, I've been informed {} has sent you a job offer.".format(c))
    print("They told me you were chosen because {}".format(d))
    select_new_program()

def text_rpg():
    print("Welcome to Text RPG Adventure")
    print("\nSorry Text RPG Adventure is being built as a separate game. Go enjoy life!.")
    select_new_program()

def hangman():
    '''
    pseudo code
    get random word for user to geuss
    allow user to see # of characters '_' that are in the word  
    while word and gues not equal
        user guesses letter
            confirm if letter is in word
                replace '_' with letters  

    '''
    print("Welcome to Hangman")
    # Hangman setup
    word_list = ["random", "words", "highlander", "control", "alternate", "destory"]
    answer = word_list[random.randint(0,len(word_list) - 1)]
    answer_list = list(answer)
    
    guess_list = []
    for w in answer_list:
        guess_list.append(' _ ')

    a = ''.join(answer_list)
    b = ''.join(guess_list)
    
    '''
    Testing functionality
    count = 0
    for x in answer_list:
        if 'o' == x:
            print("found O")
            print(count)
            #print(answer_list.index(x))
            del guess_list[count]
            guess_list.insert(count, x)
            print(guess_list)
            b = ''.join(guess_list)
            print(a, b)
        count = count + 1
    '''
    # User guessing
    print("Hangman has begun. The word will only have lower case characters.\n")
    print("{}\n".format(b))
    turns = 0

    while (a != b) or (guess == "quit"):
        guess = input("Guess a letter: ")
        if guess == "quit":
            break
        count = 0
        for x in answer_list:
            #print(guess, x)
            if guess == x:
                del guess_list[count]
                guess_list.insert(count, x)
                #print(guess_list)
                b = ''.join(guess_list)
                #print(a, b)
            count = count + 1
        print("\nYour word so far: \n{}\n".format(b))
        turns = turns + 1
    if guess != "quit":
        print("Congratulations you have completed Hangman in {} amount of turns. The word was {}".format(turns, b))

    select_new_program()

print ("Welcome to Drew's Python Programming!")
select_program()
