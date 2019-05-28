'''
import matplotlib.pyplot as plt

# Column 2 from data table
A_input_chars = [1, 2, 3, 4]
B_input_chars = [1, 2, 3, 4, 5, 6, 7, 8]

# Column 3 and 4 from data table
# Replace list elements with your times
A_time = [0.0068,0.0136,0.195,2.029] 
B_time = [0.0257,0.0385,0.0216,0.0353,0.0721,0.202,0.633,1.938]

fig, ax = plt.subplots(1,1)
# plot(x_list, y_list, "color and style")
ax.plot(A_input_chars, A_time, 'ro-', label='Algorithm A') # red dots
ax.plot(B_input_chars, B_time, 'bo-',label='Algorithm B') # blue dots

# Label and show
ax.set_xlabel ("Length of input in characters")
ax.set_ylabel("Worst case execution time")
ax.set_title("Execution time vs. input length")
ax.legend(loc='center left')
ax.margins(.1)
fig.set_facecolor('white')
fig.show()


'''


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Column 2 from data table
A_input_chars = [1, 2, 3, 4]
B_input_chars = [1, 2, 3, 4, 5, 6, 7, 8]

# Column 3 and 4 from data table
# Replace list elements with your times
A_time = [
0.00354290008545,
0.0218169689178,
0.172673940659,
1.76431298256
]
B_time = [
0.00706100463867,
0.00862884521484,
0.0118138790131,
0.022068977356,
0.0551450252533,
0.175952911377,
0.555413007736,
1.84425592422
]

fig, ax = plt.subplots(1,1)
# plot(x_list, y_list, "color and style")
ax.plot(A_input_chars, A_time, 'ro-', label='Algo. A') # red dots
ax.plot(B_input_chars, B_time, 'bo-', label='Algo. B') # blue dots

# Label and show
ax.set_xlabel ("Length of input in characters")
ax.set_ylabel("Execution time")
ax.set_title("Execution time vs. input length")
ax.legend(loc='center left') # Show and place the legend fig.set_facecolor('white')
fig.savefig('graph_data')
