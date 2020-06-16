

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
n = 5
milan= (18, 18, 18, 18, 22)
inter = (18, 12, 16, 14, 22)
fig, ax = plt.subplots()
index = np.arange(n)
bar_width = 0.35
opacity = 0.9
ax.bar(index, milan, bar_width, alpha=opacity, color='yellow',
                label='CSK')
ax.bar(index+bar_width, inter, bar_width, alpha=opacity, color='b',
                label='MI')
ax.set_xlabel('Seasons')
ax.set_ylabel('Points')
ax.set_title('CSK Vs MI')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('2019','2018','2015','2014','2013'))
ax.legend()
plt.show()