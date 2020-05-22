# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [0, 35.5]
bars2 = [25, 100]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='#FF5376', width=barWidth, edgecolor='white', label='IOS')
plt.bar(r2, bars2, color='#242154', width=barWidth, edgecolor='white', label='Android')
 
# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2'])
 
# Create legend & Show graphic
plt.legend()
plt.show()
