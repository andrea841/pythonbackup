# Imported Functions: 
from __future__ import print_function
import time
import random

''' Python Text Adventure '''

''' Life of a Caterpillar: A Survival Game ''' 

death = "oof, you died."
called = False 

def intro(): 
    ''' This function is called to start the game. It collects input on the user
    to know whether to start the game. It will then start the game despite what 
    the user says. It will call countdown when life starts, and call 
    start_game, which runs a series of other functions.'''
    c1 = raw_input("Do you want to start this game, The Life Of A Caterpillar?\
 Type yes or no: ") # a "main menu" for the game 
    if c1 == "yes":
        print("Good luck! You'll need it...")     # ####################################################### ask Mr. Brown if we need to provide instructions on how to win game 
    else: 
        print("Well, you don't have a choice.")
    time.sleep(1) #This line of code waits one second before running the next line
    countdown() 
    start_game()

def countdown():
    ''' This function prints text with delays to simulate a countdown to the 
    beginning of the main game or program. ''' 
    print("Life starts in 3")
    time.sleep(1) 
    print("Life starts in 2")
    time.sleep(1)
    print("Life starts in 1")
    time.sleep(1)
    print(" ")
    time.sleep(1)

def stage_one():
    '''In this stage, users chose which leaf to eat. D''' 
    print("You are now a caterpillar. You are hungry, and you see different \
leaves surrounding you. ")
    food_guess = raw_input("Will you eat the leaf on the right or the left? Type \
right or left: ") # players should pick the leaf on the right to survive this stage 
    print("  ")
    if food_guess == "right":
        print("Good choice. Milkweed is good for you.")
        time.sleep(1)
    else: 
        print("That leaf was poisonous... ", death) 
        restart()

def stage_two():
    ''' This function provides players a choice between building the caterpillar 
    cocoon on a tree or not on a tree. Depending on which choice they type in 
    with raw input, the player either survives and moves on to the next stage or 
    a=raw_input("Do yuo")
    print(" ")
    tree=raw_input("Do you want to make your cocoon on the tree? Type t\
for tree and n for not: ") # players should pick not to build their cocoon on the tree
    if tree=="n":
        print("Good choice. Trees have more predators.")
        time.sleep(1)
    else: 
        print("A bird ate your cocoon", death)
        restart()
    

def stage_three():
    ''' This function is the third section of our story. The caterpillar (the 
    player) has emerged from their cocoon, and their survival this time depends 
    on chance. This function uses the imported function random.randint() to 
    pick either 1 or 2, and the player has to guess which number it is. This 
    simulates the chance of whether or not the player will find food, and adds 
    challenge to the game because luck is also a factor in its completion.''' 
    print(" ")
    print("You have emerged from your cocoon.")
    print("You need food again, but your milkweed supply has been finished. Can\
 you find food?")
    guess = raw_input("Guess 1 or 2: ")
    answer = random.randint(1,2)
    if int(guess) == answer: 
        print("Congratulations! You found some food and avoided starvation.")
    else: 
        print("No food for you...", death)
        time.sleep(2)
        restart()

def restart(): 
    ''' This function gives the player a choice to restart the game with 
    raw_input. If they choose yes, the countdown function starts and the game 
    begins. If no, they are taken to the "main menu" and asked if they would like
    to play. ''' 
    restart_choice = raw_input("Do you want to play again? Type yes or no: ")
    if restart_choice == "yes":
        countdown()
        start_game()
    else: 
        print("You will now go to the main menu.")
        print("")
        intro()

def start_game(): 
    ''' This function contains all smaller functions that code for different 
    sections of the text adventure. Every function listed has a conditional for 
    a choice; whenever the wrong choice is made, that function will restart, and 
    the next stage won't be called because the player failed to reach that stage.''' 
    stage_one()
    stage_two()
    stage_three()
    print("You survived the Life Of A Caterpillar.")
    time.sleep(1) #delay before restart 
    restart() #may comment this out later due to complication in code

intro() 

# remember to add docstrings while coding 

# no loops allowed 