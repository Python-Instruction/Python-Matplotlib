import matplotlib.pyplot as plt

labels = 'China', 'India', 'United States', 'Indonesia','Pakistan'
sizes = [1394, 1326, 332, 267,233]
explode = (0, 0, 0, 0,0)
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.1f%%', shadow=True, startangle=90)
ax.set_aspect('equal')
plt.show()