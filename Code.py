import matplotlib.pyplot as plt
import pandas as pd
r = [0, 1, 2, 3, 4]
raw_data = {'greenBars': [10, 20, 25, 35, 15], 'orangeBars': [10, 20, 25, 35, 15], 'blueBars': [80, 60, 50, 30, 70]}
df = pd.DataFrame(raw_data)
# From raw value to percentage
totals = [i + j + k for i, j, k in zip(df['greenBars'], df['orangeBars'], df['blueBars'])]
greenBars = [i / j * 100 for i, j in zip(df['greenBars'], totals)]
orangeBars = [i / j * 100 for i, j in zip(df['orangeBars'], totals)]
blueBars = [i / j * 100 for i, j in zip(df['blueBars'], totals)]
# plot
barWidth = 0.85
names = ('Chr1', 'Chr2', 'Chr3', 'Chr4', 'Chr5')
# Create green Bars
plt.bar(r, greenBars, color='#b5ffb9', edgecolor='black', width=barWidth)
# Create orange Bars
plt.bar(r, orangeBars, bottom=greenBars, color='#f9bc86', edgecolor='black', width=barWidth)
# Create blue Bars
plt.bar(r, blueBars, bottom=[i + j for i, j in zip(greenBars, orangeBars)], color='#a3acff', edgecolor='black',
        width=barWidth)
# Custom x axis
plt.xticks(r, names)
plt.xlabel('Chromosomes', fontweight='bold', color='red', fontsize='12', horizontalalignment='center')
plt.show()
