from __future__ import print_function # use Python 3.0 printing; code from #9 needs to be at top due to import 

'''Procedure'''
#1-5 N/A

''' ''' ''' ''' ''' '''

'''Part 1: Conditional'''

#6a Prediction: I think the output is True. 
    #My prediction was correct. 
#6b Prediction: I think the output is True.
    #My prediction was correct. 
    
#7 x, y = (65, 40)
    # Compound conditional: x>40 and x<130 and y>100 and y<120

#8 x, y = (90, 115)
    # Compound conditional: x>40 and x<130 and y>100 and y<120
    
''' ''' ''' ''' ''' ''' 

''' Part 2: if-else Structures a& the print() Function!!!!''' 

#9 
def age_limit_output(age):
    '''Step 9a if-else example; age is a parameter that takes a number for an 
    argument, and compares it to a fixed variable AGE_LIMIT; if the number for age
    exceeds the variable value, then the function prints the output that the age 
    limit has been reached; if the number for age is below the value, then the 
    function tells the user that the age is below the age limit; regardless of 
    what age is, the function will print the value of AGE_LIMIT'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT) 
    
#9a Predictions: "10 is below the age limit. Minimum age is 13"; "16 is old enough. Minimum age is 13"
age_limit_output(10)
age_limit_output(16)
# The output checks the value given for age and compares it with the age limit; 
    # if the age limit is satisfied, the function prints a certain string; if the
    # age limit is not satisfied, the function prints a different string; also, 
    # regardless of input for age, the function will print the minimum age. 
#9b 
def report_grade(percent):
    ''' percent is a parameter that takes a number as an argument (either float 
    or int); the function takes this value and compares it to a number grade that 
    indicates mastery, and if the entered 'percent' is greater or equal to that 
    number, then the student with that grade has mastered the content; the output
    is a print statement that tells the user whether or not the grade indicates
    mastery of content ''' 
    if percent >= 80:
        print ('A grade of', percent, 'percent indicates mastery. Keep up the good work!')
    else: 
        print ('A grade of', percent, 'percent does not indicate mastery. Seek extra practice or help.')  

''' ''' ''' ''' ''' ''' 

''' Part 3: The in operator and an introduction to collections ''' 

#10 True, False (both correct)

#11 
def letter_in_word(guess, word):
    ''' guess and word are both parameters that have strings as arguments; guess
    is a letter guessed by the user that is in the word, and the word is a secret
    word that the user defines; the function tells the user whether or not the 
    guessed letter is in the word; this function returns Boolean values of True 
    or False ''' 
    if guess in word:
        return True 
    else:
        return False
        
#12 
def hint(color, secret):
    ''' color is a parameter that is the user's guess of what is in the secret, 
    and secret is a list defined by the user of a sequence of colors; this 
    function gives the user a hint on whether or not the color they guessed is 
    in the secret sequence of colors; the output of the function is a statement 
    of whether or not color is in the secret sequence''' 
    if color in secret:
        print('The color', color, 'IS in the secret sequence of colors.')
    else: 
        print('The color', color, 'is NOT in the secret sequence of colors.')

''' ''' ''' ''' ''' '''

''' Conclusion ''' 

#1 Blocks of code indented after the colon in if, elif, or else statements are 
    # blocks of code that run if the code statements they are under are True. The
    # code will only run if it is indented properly. 

#2 Boolean operators I have learned about are and, not, and or, as well as several
    # comparators: ==, !=, >, < >=, <= 
    # An additional operator I learned about on the Internet is ^, or exclusive or; 
    # this operator returns True if only one value is true, but not both on the 
    # sides of the ^ symbol
    
#3 Each of them are right; Ira is somewhere in the middle because the program 
    # is minimally affected by the amount of lines in the code; Kendra also has 
    # a similar problem, because the code is fairly small and the memory should 
    # not be a large factor. Jayla provides the most logical reasoning of why 
    # the code should be simplified. 
   
 
''' Assignment Check '''
#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)