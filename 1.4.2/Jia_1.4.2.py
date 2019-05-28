
''' Part 1: Working with a File System ''' 
#4 C:/Users/Student login/Desktop/nice.jpg

#5 ../Student login/Desktop/nice.jpg

#6 C:\\Windows\\Cursors\\cursor1.png is an absolute filename, and can make 
    # sense no matter which directory it is currently in. The difference between
    # these commands is that they perform different functions in order to 
    # manipulate files. 
    
    
    
    
''' Part 2: Rendering an Image on the Screen ''' 

#7 
# '''
# JDoe_JSmith_1_4_2: Read and show an image. (*This is old code)
# '''
# import matplotlib.pyplot as plt 
# import os.path
# import numpy as np      # 'as' lets us use standard abbreviations

# '''Read the image data'''
# # Get the directory of this python script
# directory = os.path.dirname(os.path.abspath(__file__)) 
# # Build an absolute filename from directory + filename
# filename = os.path.join(directory, 'woman.jpg')
# # Read the image data into an array
# img = plt.imread(filename)

# '''Show the image data'''
# # Create figure with 1 subplot
# fig, ax = plt.subplots(1, 1)
# # Show the image data in a subplot
# ax.imshow(img, interpolation='none')
# # Show the figure on the screen
# fig.show()

# '''
# JDoe_JSmith_1_4_2: Read and show an image.
# '''
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

# '''Read the image data'''
# # Get the directory of this python script
# directory = os.path.dirname(os.path.abspath(__file__)) 
# # Build an absolute filename from directory + filename
# filename = os.path.join(directory, 'woman.jpg')
# # Read the image data into an array
# img = plt.imread(filename)

# '''Show the image data'''
# # Create figure with 1 subplot
# fig, ax = plt.subplots(1, 1)
# # Show the image data in a subplot
# ax.imshow(img, interpolation='none')
# # Show the figure on the screen
# # fig.show()
# fig.savefig('women_plot')

''' 7: The differences include "matplotlib.use("Agg")" and 
    "fig.savefig('women_plot')" - these fixed the code because of the way the 
    environment was set up by the code. The Cloud 9 Python environment is a 
    non-GUI (graphic user interface) workspace, while matplotlib is set up to 
    work in a GUI environment. '''

#7a (280, 400) 
#7b (60, 40)
# '''
# JDoe_JSmith_1_4_2: Read and show an image.
# '''
# import matplotlib 
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt 
# import os.path
# import numpy as np      # 'as' lets us use standard abbreviations

# '''Read the image data'''
# # Get the directory of this python script
# directory = os.path.dirname(os.path.abspath(__file__)) 
# # Build an absolute filename from directory + filename
# filename = os.path.join(directory, 'cat1-a.gif')
# # Read the image data into an array
# img = plt.imread(filename)

# '''Show the image data'''
# # Create figure with 1 subplot
# fig, ax = plt.subplots(1, 1)
# # Show the image data in a subplot
# ax.imshow(img, interpolation='none')
# # Show the figure on the screen
# # fig.show()
# fig.savefig('cat_plot')


''' Part Three: Objects and Methods ''' 

#8a fig is an instance of the class Figure.
#8a ax is an instance of the class AxesSubplot. 

#8b Similarly, in line 25, the method savefig() is being called on the object fig.
    #That method is being given 1 arguments. That method is a method of the 
    #class Figure.

#8c The lines of comments right above a certain line of code explain what it 
    # does. The triple quote comments explain the general function of a section 
    # of code. 



''' Part IV: Arrays of Objects'''

#9a The method imshow() is being called on the object ax. 

# '''
# JDoe_JSmith_1_4_2: Read and show an image.
# '''
# import matplotlib 
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt 
# import os.path
# import numpy as np      # 'as' lets us use standard abbreviations

# '''Read the image data'''
# # Get the directory of this python script
# directory = os.path.dirname(os.path.abspath(__file__)) 
# # Build an absolute filename from directory + filename
# filename = os.path.join(directory, 'cat1-a.gif')
# # Read the image data into an array
# img = plt.imread(filename)

# '''Show the image data'''
# # Create a 1x2 grid of subplots
# # fig is the Figure, and ax is an ndarray of AxesSubplots
# # ax[0] and ax[1] are the two Axes Subplots
# fig, ax = plt.subplots(1, 2)
# # Show the image data in the first subplot
# ax[0].imshow(img, interpolation='none')
# ax[1].imshow(img, interpolation='none')
# # Show the figure on the screen
# # fig.show()
# fig.savefig('cat_plot')

#9b: Check 1.4.2 directory 
# '''
# two_women.png
# '''
# import matplotlib 
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt 
# import os.path
# import numpy as np      # 'as' lets us use standard abbreviations

# '''Read the image data'''
# # Get the directory of this python script
# directory = os.path.dirname(os.path.abspath(__file__)) 
# # Build an absolute filename from directory + filename
# filename = os.path.join(directory, 'woman.jpg')
# # Read the image data into an array
# img = plt.imread(filename)

# '''Show the image data'''
# # Create a 1x2 grid of subplots
# # fig is the Figure, and ax is an ndarray of AxesSubplots
# # ax[0] and ax[1] are the two Axes Subplots
# fig, ax = plt.subplots(1, 2)
# # Show the image data in the first subplot
# ax[0].imshow(img, interpolation='none')
# ax[1].imshow(img, interpolation='none')
# # Show the figure on the screen
# # fig.show()
# fig.savefig('two_women')

# '''
# five_cats.png 
# '''
# import matplotlib 
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt 
# import os.path
# import numpy as np      # 'as' lets us use standard abbreviations

# '''Read the image data'''
# # Get the directory of this python script
# directory = os.path.dirname(os.path.abspath(__file__)) 
# # Build an absolute filename from directory + filename
# filename = os.path.join(directory, 'cat1-a.gif')
# # Read the image data into an array
# img = plt.imread(filename)

# '''Show the image data'''
# # Create a 1x2 grid of subplots
# # fig is the Figure, and ax is an ndarray of AxesSubplots
# # ax[0] and ax[1] are the two Axes Subplots
# fig, ax = plt.subplots(1, 5)
# # Show the image data in the first subplot
# ax[0].imshow(img, interpolation='none')
# ax[1].imshow(img, interpolation='none')
# ax[2].imshow(img, interpolation='none')
# ax[3].imshow(img, interpolation='none')
# ax[4].imshow(img, interpolation='none')
# # Show the figure on the screen
# # fig.show()
# fig.savefig('five_cats')



''' Part V: Keyword = Value Pairs ''' 
#10 Interpolation between data points causes the image to become blurred, as the 
    # code finds the average of two distinct points. 

#11a See experiment.png 
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt 
# import os.path
# import numpy as np      # 'as' lets us use standard abbreviations
# directory = os.path.dirname(os.path.abspath(__file__)) 
# # Build an absolute filename from directory + filename
# filename = os.path.join(directory, 'woman.jpg')
# # Read the image data into an array
# img = plt.imread(filename)

# # Create figure with 2 subplots
# fig, ax = plt.subplots(1, 2)
# # Show the image data in the first subplot
# ax[0].imshow(img, interpolation='none') # Override the default
# ax[1].imshow(img)
# ax[0].set_xlim(135, 165)
# ax[0].set_ylim(470, 420)
# ax[1].set_xlim(135, 165)
# ax[1].set_ylim(470, 420)
# ax[0].axis('off')
# # Show the figure on the screen
# # fig.show()
# fig.savefig('experiment')

#11b See three_closeup.png
'''Read the image data'''
# Get the directory of this python script
# directory = os.path.dirname(os.path.abspath(__file__)) 
# # Build an absolute filename from directory + filename
# filename = os.path.join(directory, 'cat1-a.gif')
# # Read the image data into an array
# img = plt.imread(filename)

# # Create figure with 2 subplots
# fig, ax = plt.subplots(1, 3)
# # Show the image data in the first subplot
# ax[0].imshow(img, interpolation='none') # Override the default
# ax[1].imshow(img, interpolation='none')
# ax[2].imshow(img, interpolation='none')
# ax[0].set_xlim(40, 50)
# ax[0].set_ylim(20, 30)
# ax[1].set_xlim(50, 60)
# ax[1].set_ylim(10, 20)
# ax[2].set_xlim(20, 30)
# ax[2].set_ylim(30, 40)
# # Show the figure on the screen
# # fig.show()
# fig.savefig('three_closeup')

#12 Axes.pie() is another method of AxesSubplot that makes a pie chart. One 
    # optional argument is radius, and its default value is None, which creates 
    # a pie chart with radius 1. 

#13 See crazy_mice.png 
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 1)
# Show the image data in the first subplot
ax.imshow(img, interpolation='none')
ax.plot(138, 42, 'ro') #white mouse right eye 
ax.plot(116, 41, 'ro') #white mouse left eye 
ax.plot(37, 49, 'ro') #black mouse eye 
# Show the figure on the screen
fig.savefig('crazy_mice')



''' Conclusion ''' 
#1 Absolute file names contain all the parent directories of the file specified, 
    # while relative file paths contain only directories necessary from that 
    # position in the file tree. 

#2 An object is an instance of a certain class that it is instantiated in. 

#3 Methods are functions that manipulate the object and are specific to a 
    # certain class; properties are characteristics of the object, which may be 
    # specified when they are instantiated or set to the default value of the 
    # class. 

#4 When a method is called on an object, a certain action is done to the object, 
    # and properties of that object may be changed. 
    

