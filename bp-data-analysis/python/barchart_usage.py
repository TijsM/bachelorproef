# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [0.007, 0.5] #IOS data
bars2 = [0.007, 0.875] #Android data

# Set position of bar on X axis
r1 = np.arange(2)
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='#FF5376', width=barWidth, edgecolor='white', label='IOS')
plt.bar(r2, bars2, color='#242154', width=barWidth, edgecolor='white', label='Android')
 
# Add xticks on the middle of the group bars
plt.xlabel('Gebruiker weet wat de voordelen van een PWA zijn', fontweight='bold')
plt.xticks([r + barWidth/2 for r in range(2)], ['nee', 'ja'])

plt.ylabel('Procent van de gebruikers die een PWA boven een native app zou kiezen', fontweight='bold')
 
# Create legend & Show graphic
plt.legend()
plt.show()

