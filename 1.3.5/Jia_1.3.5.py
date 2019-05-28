from __future__ import print_function

''' Introduction '''
# A line of text is called a string because it is similar to a string of characters
    # connected together.
    
''' ''' ''' ''' ''' ''' 
''' Procedure ''' 
#5 The data type long can be used to represent 6 million because it is an integer
    # with a very large value. 
slogan = 'My school is the best'
type(slogan)
# str
slogan
# 'My school is the best'

#6 The second line of code will produce an error because a string and an integer
    # cannot be concatenated. 
type('tr' + "y this")
# type('tr' + 5)

#7 The index of a string returns the character at that index, starting from 0. If
    # the index is greater than the amount of characters in the string, the code 
    # will produce an error. If the index is a negative number, the code will 
    # count that index from the end of the string. In the case of slogan[-7], it 
    # returns the 7th to last character in the string. 
    
#8 
# slogan[5:21] = 'hool is the best'
# slogan[:5] = 'My sc'
# Slicing for 'best':
slogan[17:]

#9 
slogan[:12] + 'in Dublin.'

#10 
    #10a The variable activity is set to the value of a string, 'theater,' and 
        # using the len() function on activity will return the length of the 
        # string it holds, not the name of the variable. 
    #10b The output of the code is 'theate' because the string is sliced so that 
        # it returns all characters except the last one, because the second number
        # in slicing is excluded. 

#11 The code returns True because the string 'test goo' is found in part of 
    # 'Greatest good for the greatest number!' between 'Greatest' and 'good'. 
    
#12 
def how_eligible(essay):
    counter = 0 
    if '?' in essay:
        counter += 1
    if '"' in essay:
        counter += 1
    if ',' in essay: 
        counter += 1
    if '!' in essay: 
        counter += 1
    return counter

#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

# I believe I have successfully completed the assignment because the output of 
    # assignment check matches that of the instructions. 