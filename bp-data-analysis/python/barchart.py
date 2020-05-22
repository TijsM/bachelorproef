# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [0.355, 0.007]
bars2 = [1, 0.25]


# Set position of bar on X axis
r1 = np.arange(2)
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='#FF5376', width=barWidth, edgecolor='white', label='IOS')
plt.bar(r2, bars2, color='#242154', width=barWidth, edgecolor='white', label='Android')
 
# Add labels to the bars
# todooo

print(r1)

# Add xticks on the middle of the group bars
plt.xlabel('Manier van informeren dat PWA installeerbaar is', fontweight='bold')
plt.xticks([r + barWidth/2 for r in range(2)], ['custom A2HS', 'standaard A2HS'])


plt.ylabel('Procent van gebruikers die app zou installeren', fontweight='bold')
 
# Create legend & Show graphic
plt.legend()
plt.show()

