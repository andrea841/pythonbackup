from __future__ import print_function
import random

''' Part 1: for loops, range(), and help() ''' 

#4 
def days():
    ''' This function prints the days of the week by using an iterable of those
    days, and using a for loop to print it. It also prints 3 days of September
    by using range(), which makes a list of numbers that are printed in a string 
    as the nth day of September (n represents the number). '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')


#5 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

def picks():
    ''' This function makes a histogram with numbers from a list. '''
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('picks')


#6a
def roll_hundred_pair():
    ''' This function makes a histogram of the sum of rolling 2 dice 100 times 
    by using an imported function from matplotlib. ''' 
    roll = []
    for i in range(1, 101):
        roll += [random.randint(1, 6)+random.randint(1, 6)]
    plt.hist(roll)
    plt.savefig('roll_hundred_pair')

#6b
def dice(n):
    ''' This function takes argument n as the number of times a 6-sided dice is 
    rolled, and uses it in a for loop to roll a dice that many times. The output
    is the sum of all dice rolls. '''
    sum = 0
    for i in range(1, n):
        sum += random.randint(1,6)
    return "Roll was "+str(sum)


#7 Line 2 is necessary in order to initialize the loop; if guess were 
    # initialized as a letter already in the answer, then the loop would not run
    # because the condition would be false. If guess were not initialized at all, 
    # there would be an error because there is no condition to check since the 
    # variable "guess" does not exist.
def validate():
    ''' The function asks the player to guess a letter in a phrase stored in the 
    variable "answer." The outputs are print statements that tell the player to 
    keep guessing or "Thank you!", meaning they guessed a correct letter. '''
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')


#8
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''The function guess_winner has the argument "players," which is a list 
    containing the names of 4 people as strings. A variable, winner, is randomly
    set to one of these people's names. The program then prompts the player to 
    guess who "won the lottery" by printing a statement using a for loop in order
    to add a comma after each person's name. Every time the person guesses 
    incorrectly, a variable "guesses," initialized to the value of one, is 
    incremented by one, and the code will tell the player to guess again. The 
    value of guesses is returned, which is an integer that represents the number
    of times the player guessed. '''
    winner = random.choice(players) 
    #The following code prints a sentence that tells the player what to do with 
        # the program. It tells the player to guess between people whose names
        # have already been placed in a list, which allows them to be printed 
        # with commas in a for loop. 
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # the code will print every name in the 
        # list except the last one with a comma after it 
        print(p+', ', end='')
    print(players[len(players)-1]) # the last name in the list is printed after
        # everything else without a comma 
    # The section below defines a variable "guesses" that is initially given the 
        # value of 1. Everytime the player guesses the wrong person, guess will 
        # increment and the program will ask the player to guess again. When the 
        # player guesses the right person, the total amount of "guesses" is 
        # printed. 
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    


#9
def goguess():
    ''' This function chooses a random integer from 1-20 inclusive and has the 
    player guess the number by giving them hints on if they guessed too low or 
    too high. The outputs are print statements that inform the player if they 
    guessed the right number, and if not, a hint is printed to help them.'''
    answer = random.randint(1,20)
    print("I have a number between 1 and 20 inclusive.")
    guess = int(raw_input("Guess: "))
    #print(answer)
    tries = 1
    while int(guess) != answer: 
        tries += 1 
        if int(guess) > answer:
            print(guess, "is too high.")
        elif int(guess) < answer:
            print(guess, "is too low.")
        guess = raw_input("Guess: ")
    else:
        print("Right! My number is", str(answer)+"!", "You guessed in", str(tries), "guesses!")
        
#10 If the range of numbers from #9 changed to 1-6000, a minimum of 13 guesses 
    # are needed. This is because in a program that tells the player if their 
    # guess is too high or low, the amount of guesses can be limited by 
    # eliminating the most possibilities at a time, or guessing in the middle. 
    # By guessing in the middle of the range every time, the range of 
    # possibilities will decrease by a factor of 1/2 every time. The total 
    # number of guesses each time can then be modeled by raising 1/2 to the n, 
    # where n is the nth guess. This means that the amount of guesses needed is 
    # the first power of 2 that is larger than the total - in this case, 2**13 
    # is 8192, which covers 6000 possibilities. 

''' Part 3: Practice ''' 

#11a
def matches(ticket, winners):
    ''' This function checks for matching numbers in 2 different lists, the 
    arguments "ticket" and "winners." A variable count is initialized with a 
    value of 0, and is incremented everytime an item in the list "ticket" is 
    also found in the list "winners." The output is the final amount stored in 
    "count." ''' 
    count = 0 
    for number in ticket:
        if number in winners:
            count += 1
    return count

#11b
def report(guess, secret):
    ''' This function takes 2 lists as arguments, guess and secret. An empty list 
    named result is initialized with 2 values in it, 0 and 0. A copy is made of 
    the list secret in order to remove duplicates for the colors placed in the 
    wrong place. When a color matches the color and place of the secret, the 
    corresponding number in the result list is incremented by one, and if only 
    the color and not the place matches, the other number is incremented by one. 
    The output of this function is the final list for result. ''' 
    result = [0, 0]
    secret_copy = secret[:]
    for i, color in enumerate(guess):
        if secret[i] == color:
            result[0] += 1
            secret_copy.remove(color)
        elif color in secret_copy: 
            result[1] += 1
    return result


''' Conclusion ''' 
#1 Disadvantages of developing code without loops is redundancy in the program 
    # and increased difficulty in debugging the code. The programmer would need 
    # to test many more lines of code, and would take more time to code because 
    # the method of programming is not efficient. 
#2 The difference between an iteration and analysis of data is that iteration 
    # goes through the iterable no matter the condition, and analysis of data 
    # allows a loop to happen only if some condition is true. An example of this 
    # is the for loop and the while loop. 
#3 A for loop goes through every item of an iterable once, but a while loop only
    # executes code if a certain named condition is true, and will continue 
    # executing as long as that condition is true. 
#4 My partner and I worked together best when we discussed what to do to on how 
    # to make a specific function. We talked about parts that we were uncertain 
    # in, which helped both of us complete the functions better. Improvement 
    # could be made in working together because we work at different speeds and 
    # this may decrease the team dynamic. 


''' Function Test ''' 

days()
# picks() # these functions are commented because they would create 2 files 
          # with the same name 
# roll_hundred_pair()
dice(10)
validate()
guess_winner()
goguess()
print(matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17]))
print(report(['red','red','red','green','yellow'], ['red','red','yellow','yellow','black']))
    
# Based on the results of my function test, I believe I have successfully 
    # completed the assignment. For matches() and report(), their output is 
    # returned, so they were printed instead of merely called. 