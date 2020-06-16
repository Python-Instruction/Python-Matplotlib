

import matplotlib.pyplot as plt
import numpy as np
# 100 linearly spaced numbers
x = np.linspace(2*(-np.pi),2*(np.pi),100)
# the function, which is y = sin(x) here
y = np.sin(x)
# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# plot the function
plt.plot(x,y, 'b',label='y=sin(x)')
plt.title('Graph of y=sin(x)')
plt.legend(loc='upper left')
# show the plot
plt.show()