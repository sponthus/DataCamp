############ GRAPHICS : MATPLOTLIB ############

import matplotlib.pyplot as plt

# Line plot
plt.plot(x, y)
plt.plot(x = varx, y = vary)

# Scatter plot
# # s = size
# # c = col
# # alpha = transparenct from 0 (transparent) to 1 (opaque)
plt.scatter(x, y, s=var, c=col, alpha=0.8)

# Histogram
# # Bins : default number = 10
plt.hist(val, bins=5)

############ CUSTOMIZATION ############

# Labels for axis, title
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Scale
plt.xscale('log')
plt.yscale('log')

# Definition of ticks used on the graph, possibility to use 2 for ticks & label for ticks
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
plt.xticks(tick_val, tick_lab)

# Add a grid

# Additional customizations : adds text at certain loc
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

############ DISPLAY ############

# After customizing, display the plot
plt.show()

# Clear the plot
plt.clf() 