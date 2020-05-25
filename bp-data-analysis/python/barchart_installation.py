# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [0.355, 0.007]
bars2 = [1, 0.25]

labelYLocation = [0.355, 1, 0.007, 0.25]


# Set position of bar on X axis
r1 = np.arange(2)
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='#FF5376', width=barWidth, edgecolor='white', label='iOS')
plt.bar(r2, bars2, color='#242154', width=barWidth, edgecolor='white', label='Android')

# Add xticks on the middle of the group bars
plt.xlabel('Manier van informeren dat PWA installeerbaar is', fontweight='bold')
plt.xticks([r + barWidth/2 for r in range(2)], ['custom A2HS', 'standaard A2HS'])

plt.ylabel('Procent van gebruikers die app zou installeren', fontweight='bold')
 
# Text on the top of each barplot
label = [0.355, 1, 0, 0.25]
location = [-0.03, 0.24, 0.98, 1.225]
for i in range(4):
  plt.text(x = location[i] , y = labelYLocation[i], s = label[i], size = 6)


# Create legend & Show graphic
plt.legend()
plt.show()

