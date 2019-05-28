from __future__ import print_function #8 import code
import random 

''' Part 1: Nested if structures and testing '''

def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
#1a: return value results from line 17 of the code on the instructions sheet. 

#1b: 
    #i: An input of "orange" will execute line 15. 
    #ii: An input of "apple" or banana" will execute line 17. 
    #iii: An input of "potato" will execute line 20. 
    #iv: An input of any other word will execute line 22. 

#1c: Line 20 will never execute as a result of the input "banana" because banana 
    # is also listed in the fruits list. Line 20 is a line of code placed after
    # the "else" command, which means it will only execute if the corresponding 
    # "if" statement to the "else" statement it is nested in returns a value of 
    # false. Since the "if" statement checks if the input is in the fruits list,
    # and "banana" is in that list, the else block of code will never run. 

#2: Performed in ipython session

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    #Added tests below 
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = 'apple bug in food_id()'
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug in food_id()'

    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

#3: 
def f(n):
    ''' The parameter n is a number that is checked for its datatype (integer or 
    float) and its divisibility. If n is divisible by 2 and 3, the function prints
    that the number is divisible by 6; if n is only divisible by 2, the function 
    prints that the number is even; if n is not divisible by 2, then the function
    prints that the number is odd; the output of the function is a string.''' 
    if int(n) == n:
        if n%2==0:
            if n%3==0:
                return 'The number is a multiple of 6.'
            else: 
                return 'The number is even.'
        else: 
            return 'The number is odd.'
    else:
        return 'The value is not an integer.'

#4: Test cases I could use to visit all my code are numbers that are odd, even 
    # but not divisble by 3, and multiples of 6. Examples are 3, 8, and 18. 
    
#5: 
def f_test(): 
    ''' Function tests whether or not function f(n) is working; has no parameters,
    runs the function f(n) for multiple values and checks the output against what
    is supposed to be returned; the local variable 'works' is set initially to 
    true, but if anything false comes up in the code, meaning there is an error,
    the variable 'works' is set to a string that tells the coder what the error 
    is; the output of this function is a string that tells the coder whether or 
    not the function works and a Boolean value of True or False, depending on 
    if the function works. '''
    works = True
    if f(1.5) != 'The value is not an integer.':
        works = "There is a bug for non-integer numbers."
    if f(3) != 'The number is odd.':
        works = "There is a bug for odd numbers."
    if f(2) != 'The number is even.':
        works = "There is a bug for even numbers."
    if f(18) != 'The number is a multiple of 6.':
        works = "There is a bug for numbers that are divisble by both 2 and 3."
    if works == True:
        print('The function is working')
        return True
    else: 
        print(works)
        return False 

''' ''' ''' ''' ''' ''' 

''' Part 2: The raw_input() function, type casting, and print() from Python 3 ''' 

#7: In concactenation, 2 strings of charactors and/or words are combined to form
    # 1 phrase, while numeric addition computes the value of the addition of 2 
    # numbers. Concactenation returns a result that contains parts of both 
    # strings, while addition may return a number that looks completely different. 
    
#8a: #11 prints 2 strings, then has an argument called " end="!\n" "; this is 
    # also a keyword-value pair, and most likely determines the end of the string.
    # There is a backslash behind the !, so the code will print the ! but ignore
    # the backslash, and will print without a space separating the !.  

#8b: 
def guess_once(): 
    ''' This function selects a random integer between 1 and 4 (inclusive), and 
    uses raw_input so that the user can guess which number the function chose; 
    the function returns an answer of what their number was and whether or not 
    the user got it right; the output of this function is a printed string. '''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4 inclusive.')
    guess = int(raw_input('Guess: '))
    if guess > secret:
        print('Too high, my number was', secret, end='!\n')
    elif guess < secret: 
        print('Too low - my number was', secret, end='!\n')
    else: 
        print('Right on! I was number', secret, end='!\n')

#9:
def quiz_decimal(low, high):
    ''' This function takes 2 arguments that are numbers (either integer or
    decimals), and quizzes the user on whether or not they can provide a number 
    that has a value between the 2 arguments; the function tells the user if the 
    number they gave is valid (more than the lower value and less than the higher
    value); the output is a printed string. '''
    print('Type a number between', low, 'and', high, end=':\n')
    guess = float(raw_input())
    if low < guess < high: 
        print('Good!', low, '<', guess, '<', high)
    elif guess > high: 
        print('No,', guess, 'is greater than', high)
    elif guess < low:
        print('No,', guess, 'is less than', low)

''' ''' ''' ''' ''' ''' 

''' Conclusion ''' 

#1: If-structures and glass box testing are related in that the glass box testing 
    # method runs the function that the if-structures are in for mulitple values 
    # to test if the function works. Glass box testing checks every if statement 
    # by trying different values for arguments that should get a specific value. 

#2: Nested if-else structures contain many blocks of code that may be executed 
    # depending on the situation. If the first if-statement is false, that block
    # of code and will be skipped and only the elif-statements and the else-
    # statement will run. If the if-statement is true, only that code will be run,
    # and any other elif or else-statements will be completely ignored. 

#3: A test suite is a test function that tests whether or not a specific function
    # works. It will run different values as arguments for the function to test 
    # all its if-statements. A programmer may create a test suite even before the 
    # function itself in order to see what the results of the function should be,
    # so that they are more organized in coding the actual function because they
    # know what needs to work and how it should work. 

#4: Yes, a function can be made for each output case: 
def integer(n): 
    ''' This function checks if the argument, n, is an integer. This is done by
    seeing if n is the same as the integer version of n with int(). The output 
    is a returned Boolean value of True or False. '''
    if n == int(n):
        return True
    else: 
        return False

def odd(n): 
    ''' This function checks if the argument, n, is odd by checking if it is 
    divisible by 2 by using the modulo operator (%). If the number n has 
    a remainder when divided by 2, then the number must be odd. The output is a 
    a returned Boolean value of True or False. '''
    if int(n) % 2 != 0:
        return True
    else:
        return False 
        
    
def even(n):
    ''' This function checks if the argument, n, is even by checking if it is 
    divisible by 2 by using the modulo operator (%). If the number n does not have
    a remainder when divided by 2, then the number must be even; if there is a 
    remainder, then the number is odd. The output is a returned Boolean value of
    True or False. '''
    if int(n) % 2 == 0:
        return True
    else:
        return False 

def multiple_six(n):
    ''' This function checks if the number is divisible by 6 by using the 
    modulo operator (%). If the number divided by 6 does not leave a remainder,
    then it must be a multiple of 6; if it leaves a remainder, the number is 
    not divisible by 6. The output of this function is a Boolean value of
    True or False. ''' 
    if int(n) % 6 == 0:
        return True
    else: 
        return False

''' ''' ''' ''' ''' ''' 

''' Challenge! ''' 

def f_challenge(n):
    ''' This function uses previously created functions to check if the entered 
    argument n is an integer, an odd number, an even number, or a multiple of six. '''
    if integer(n) != True:
        print('The number is not an integer.')
    elif odd(n) == True:
        print('The number is odd.')
    elif multiple_six(n) == True:
        print('The number is a multiple of six.')
    else:
        print('The number is even.')


''' ''' ''' ''' ''' ''' 

#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)





    