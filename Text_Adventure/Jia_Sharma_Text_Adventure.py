# Imported Functions: 
from __future__ import print_function
import time
import random

''' Notes: (delete later)
- remember to add docstrings to all functions and in-scene comments 
'''


''' Python Text Adventure '''

''' Life of a Caterpillar: A Survival Game ''' 

death = "Oof, you died." # code displayed once the character dies

def countdown():
    ''' This function prints text with delays to simulate a countdown to the 
    beginning of the main game or program. The output is a series of printed 
    lines that are displayed one second after each other, telling the user when
    the game will begin.''' 
    print("Life starts in 3")
    time.sleep(1) 
    print("Life starts in 2")
    time.sleep(1)
    print("Life starts in 1", "\n")
    time.sleep(1)
    
def restart(): 
    ''' This function gives the player a choice to restart the game with 
    raw_input. If they choose yes, the countdown function starts and the game 
    begins. If no, they are taken to the "main menu" and asked if they would like
    to play. The outputs are print statements that correspond to what the player
    chose to do.''' 
    restart_choice = raw_input("Do you want to play again? Type yes or no: ")
    if restart_choice == "yes": 
        ''' yes will directly go to the game instead of going through the
        intro, which will ask them to play again '''
        countdown()
        start_game()
    else: 
        print("You will now go to the main menu.", "\n") # "\n" is a new line
        # main menu = intro, and asks user to play 
        time.sleep(1)
        intro()

def second_chance():
    '''This function gives player a second chance to survive if they guess the 
    wrong number in stage_three. This stage is a trivia question, which asks the
    player to guess what type of butterfly they are. This was hinted at in the 
    first stage, which told them they only ate a certain type of plant. The 
    output is a series of printed statements. '''
    print("A kind human has offered you a second chance.", \
    "If you get this question right, you might survive.", \
    "What kind of butterfly are you? Your choices are:", "\n", "1, Queen ", \
    "\n", "2, Question Mark", "\n", "3, Monarch", "\n", "4, Zebra", "\n", \
    "5, Striped Garden", "\n", "6, Cyncia")
    trivia = raw_input("Type 1, 2, 3, 4, 5, or 6: ")
    trivia_answer = "3" 
    if trivia == trivia_answer:
        print("Correct! Monarch larvae only eat milkweed.")
    else:
        print("Good try...", death)
        restart()

def stage_three():
    ''' This function is the third section of our story. The caterpillar (the 
    player) has emerged from their cocoon, and their survival this time depends 
    on chance. This function uses the imported function random.randint() to 
    pick either 1 or 2, and the player has to guess which number it is. This 
    simulates the chance of whether or not the player will find food, and adds 
    challenge to the game because luck is also a factor in its completion. The 
    answer is a string instead of an integer because if it is an integer, the 
    code will display an error and exit out the program if the user typed 
    anything other than an integer. The output is printed statements. ''' 
    print("You have emerged from your cocoon.")
    print("You need food again, but your milkweed supply has been finished.", \
    "Can you find food? Test your luck...")
    answer = str(random.randint(1, 2)) 
    # answer is a string because raw_input produces a string
    # print(answer) # this line of code was used for debugging and checking 
    guess = raw_input("Guess 1 or 2: ")
    if guess == answer: 
        print("Thankfully, you found some food and avoided starvation.", "\n")
    elif guess == "1" or guess == "2":
        print("Bad luck, you didn't find food.")
        time.sleep(1)
        print("But wait! Here is a chance at redemption...", "\n")
        second_chance()
    else: 
        print("Ignoring instructions will get you nowhere in life...", death)
        # code for when the user fails to input either 1 or 2
        restart()

def stage_two():
    ''' This function provides players a choice between building the caterpillar 
    cocoon on a tree or not on a tree. Depending on which choice they type in 
    with raw input, the player either survives and moves on to the next stage or 
    fails and has to restart. This is displayed in the output as a printed line.''' 
    print("\n", end="Do you want to make your cocoon on the tree? ")
    tree=raw_input("Type t for tree and n for not: ") 
    #
    if tree == "n":
        print("Good choice. Trees have more predators.", "\n")
        time.sleep(1)
    else: 
        print("A bird ate your cocoon...", death)
        restart() # function to restart the game
        
def stage_one():
    '''In this stage, users type in which leaf to eat. Depending if they chose 
    right or left, they will die or continue to the next stage. The output of 
    this function is a print statement telling the player their results.''' 
    print("You are now a caterpillar.", \
    "You are hungry, and you see different leaves surrounding you.", \
    "Will you eat the leaf on the right or the left? ")
    food_guess = raw_input("Type right or left: ") 
    # 
    if food_guess == "right":
        print("Good choice. Milkweed is the only thing you can eat.")
        # 
        time.sleep(1)
    elif food_guess == "left": 
        print("That leaf was poisonous... ", death) 
        restart()  
    else: 
        print("You can't escape this...", death)
        restart()

def start_game(): 
    ''' This function contains all smaller functions that code for different 
    sections of the text adventure. Every function listed has a conditional for 
    a choice; whenever the wrong choice is made, that function will restart, and 
    the next stage won't be called because the player failed to reach that stage.''' 
    stage_one()
    stage_two()
    stage_three()
    print("Congratulations! You survived the Life Of A Caterpillar.", "\n")
    time.sleep(1) #delay before restart 
    restart()

def intro(): 
    ''' This function is called to start the game. It collects input on the user
    to know whether to start the game. It will then start the game despite what 
    the user says. It will call countdown when life starts, and call 
    start_game, which runs a series of other functions.'''
    print("Do you want to start this game, The Life Of A Caterpillar?")
    c1 = raw_input("Type yes or no: ") # a "main menu" for the game 
    if c1 == "yes":
        print("Good luck! You'll need it...", "\n")
    else: 
        print("Well, you don't have a choice.", "\n")
    time.sleep(1) # code waits one second before running the next line
    countdown() # countdown until game begins 
    start_game()

intro() 

'''calls intro function, which begins introduction, and will call other 
        functions, like the domino effect; runs entire game'''