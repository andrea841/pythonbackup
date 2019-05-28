
''' Part 1: Tuples, Syntax '''

#4 
(1, 2, 3)

#5 One convention I can think of for formatting submitted work is MLA format for 
    # English essays. 
#5 Our teacher is fine with any format, but all lowercase and camelCase are most 
    # likely more preferred. 

some_values = ('a', 'b', 3)
some_values[1]
#6a The code above returns 'b' because 'b' it is at index 1 in the tuple named. 

some_values[0:2]
#6b The code above returns ('a', 'b'), because the slicing of an iterable will 
    # include the first index but not the second, so the value at index 2 is not 
    # displayed. Additionally, since some_values is a tuple, the output will be 
    # displayed as a tuple, which means it will have parentheses around it. 

a = 10
b = (9, a, 11)
a = 15
#7a The code b[1] == 10 will return True because the value at index 1, a, first 
    # had the value 10, and will always hold that value. 

b = (9, a, 11)
b[1]
#7b The code above will return 15, because the tuple was redefined after the 
    # variable a changed to hold the value 15. 

''' Part 2: Lists ''' 

values = ['a', 'b', 3]
values[1:]
#8 The above code returns ['b', 3] because the sliced indices start at index
    # 1, which holds the value 'b', and goes to the end. The sliced iterable is 
    # also a list, so the output will be displayed with square brackets. 

values[2] = '3' 
values[2] == 3
#9 The above code returns False because the value assigned to index 2 of values 
    # is a string, not an integer, and therefore have different values. 
    
values = values + [4, 5]
values
#10a The code above returns ['a', 'b', '3', 4, 5] because it added 2 elements at
    # the end of the list. 

values.append([6, 7])
values
#10b The code above returns ['a', 'b', '3', 4, 5, [6, 7]] because .append() only 
    # takes one argument and does not interpret [6, 7] as 2 items in a list 
    # because it only appends 1 item. 
    
# values + 5 
#11 The above code does not work because lists can only be concatenated with 
    # another list, not an integer. 

a = 6
a *= 3
a 
#12 The above code returns 18 because a is set to its original value, 6, multiplied
    # by 3. 

''' Lists and the Random Module ''' 

import random
#13 

#14 
def roll_two_dice():
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    return dice_one+dice_two

''' Conclusion ''' 

#1 a is a string, b is a tuple, and c is a list. a is a string of characters, b 
    # is immutable, and c is mutable. 

#2 Computer programming languages use a variety of data types to be able to store 
    # different types of everything. Integers cannot represent everything - if 
    # code was limited to the integer datatype, decimals and word information 
    # would not be able to be transferred or stored. 

#3 In activities 1.3.2-1.3.6, I learned the basics of Python coding. I learned 
    # about the different datatypes, how to manipulate them, how to use Boolean 
    # operators, how to use conditionals to create functions, and how to use 
    # iterables and the different characteristics of different types of iterables. 


#1.3.6 Function Test
print(roll_two_dice())

# My result was 3; since 3 is a plausible number that can result from rolling 2
    # dices, I believe I have successfully completed the assignment. 