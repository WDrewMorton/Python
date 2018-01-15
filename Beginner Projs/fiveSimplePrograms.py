#!/usr/bin/python
'''
Created by Drew Morton
Last Editted: 01/14/18

This program is to build practice w/ Python and to get used to 

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
    var = input("\nDo you want to select another program? (Y/N)")
    if var == "y":
        select_program()
    else:
        quit()

# Simulates rolling a dice
# TODO: allow user to select which type of die they wish to roll
def dice_roller():
	
    min = 1
    max = 20

    print("Welcome to Dice Roller!")
    print("\nDo you want to roll the d20")
    play_var = input("Y/N : ")

    while (play_var == "y"):
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
    print("\nSorry Mad Libs is still under construction.")
    select_new_program()

def text_rpg():
    print("Welcome to Text RPG Adventure")
    print("\nSorry Text RPG Adventure is still under construction.")
    select_new_program()

def hangman():
    print("Welcome to Hangman")
    print("\nSorry Hangman is still under construction.")
    select_new_program()

print ("Welcome to Drew's Python Programming!")
select_program()

#print("Var is ", var)

'''
if var == 1:
    dice_roller()
elif var == 2:
    guess_number()
else:
    print("Option doesnt exist")
'''
'''
def numbers_to_program(argument):
    switcher = {
        0: dice_roller,
        1: guess_number,
        #2: three,
        #3: four,
        #4: five,   
    }
    print(switcher)
    #func = getattr(amodule, switcher)
    #func()

numbers_to_program(var)
'''
