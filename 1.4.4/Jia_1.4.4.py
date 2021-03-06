'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
#fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
#fig2.savefig('resize_earth')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
#fig3.savefig('earth_eye')

''' #20 ''' 
# Paste earth into both eyes and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
student_img.paste(earth_small, (700, 943), mask=earth_small) 
# Display
fig4, axes4 = plt.subplots(1, 2)
axes4[0].imshow(student_img, interpolation='none')
axes4[1].imshow(student_img, interpolation='none')
axes4[1].set_xlim(500, 1500)
axes4[1].set_ylim(1130, 850)
#fig4.savefig('earth_as_eyes')

# work for other questions 
print(earth_img.size)
print(earth_small.size)
print(earth_img.size[1]) 
print("")
print(student_img.size)
print(earth_small.size)
#earth_small.save('smallEarth.png')

# Conclusion answers are on Tanish's submission document 

