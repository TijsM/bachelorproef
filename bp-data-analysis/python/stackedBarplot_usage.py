# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
 
# y-axis in bold
rc('font', weight='bold')
 
# Values of each group
bars1 = [0.007, 0.25] #IOS data
bars2 = [0.007, 0.875] #Android data
 
# Heights of bars1 + bars2
bars = np.add(bars1, bars2).tolist()
 
# The position of the bars on the x-axis
r = [0,1]
 
# Names of group and bar width
names = ['A','B']
barWidth = 1
 
# Create brown bars
plt.bar(r, bars1, color='#FF5376', edgecolor='white', width=barWidth, label="iOS")
# Create green bars (middle), on top of the firs ones
plt.bar(r, bars2, bottom=bars1, color='#242154', edgecolor='white', width=barWidth, label="Android")

 
# Custom X axis
plt.xticks(r, names, fontweight='bold')
plt.xlabel("group")
 
# Show graphic
plt.show()
