# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:55:45 2021

@author: gemelli
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joypy
import seaborn as sns
sns.set()
import os
import matplotlib.cm as cm
import plotly


from matplotlib.cm import ScalarMappable
from matplotlib.lines import Line2D
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from textwrap import wrap

qualifiche = ('qualifying.csv')
qualifiche = pd.read_csv(qualifiche)

risultati = ('results.csv')
risultati = pd.read_csv(risultati)

piloti = ('drivers.csv')
piloti = pd.read_csv(piloti)

data_vuoto = []
df = pd.DataFrame(data_vuoto)
df['idPilota'] = piloti['driverId']
df['nomePilota'] = piloti['driverRef']



temp = qualifiche[qualifiche['position'] == 1]
temp = temp.drop(columns = ['qualifyId', 'raceId', 'constructorId', 'number', 'q1', 'q2', 'q3'])
temp = temp.rename(columns = {'position': 'numPole'})
temp = temp['driverId'].value_counts()




winspoles = ('WinsPoles.csv')
winspoles = pd.read_csv(winspoles)
winspoles = winspoles.drop(columns = ['Unnamed: 0'])

'''
winspoles.plot.scatter(x = 'Wins', y = 'Poles')
#bisettrice
plt.plot([-2, 110], [-2, 110], color = 'black', linewidth = 2)
plt.xlim(-5, 115)
plt.ylim(-5, 115)
'''

#MARGINAL BOXPLOT
#MARGINAL BOXPLOT
# Create Fig and gridspec
fig = plt.figure(figsize=(16, 10), dpi= 80)
grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2)
# Define the axes
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])

# Scatterplot on main ax
#colors = np.where(winspoles["WinPerc"])
ax_main.scatter('Wins', 'Poles', alpha=.9, data=winspoles, 
                cmap="Set1", edgecolors='black', linewidths=.2)
#mediana
#mediana_wins = winspoles['Wins'].median(axis = 1)

#bisettrice
#ax_main.plot([0, 110], [0, 110], color = 'black', linewidth = 2)

# Add a graph in each part
sns.boxplot(data=winspoles['Poles'], ax=ax_right, orient='vertical')
sns.boxplot(data=winspoles['Wins'], ax=ax_bottom, orient='horizontal')

# Decorations ------------------
# Remove x axis name for the boxplot
ax_bottom.set(xlabel='')
ax_right.set(ylabel='')

# Main Title, Xlabel and YLabel
ax_main.set(title='Scatterplot with Histograms \n wins & poles', xlabel='Number of wins', 
            ylabel='Number of poles')

# Set font size of different components
ax_main.title.set_fontsize(20)
for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
    item.set_fontsize(14)

plt.show()






#importo dati mondiali vinti-piloti
mondiali = ('worldChampions.csv')
mondiali = pd.read_csv(mondiali)
mondiali = mondiali.drop(columns = ['Unnamed: 0'])



#LOLLIPOP PER MONDIALI VINTI ORIZZONTALE
#ordino x valori
ordered_mondiali = mondiali.sort_values(by='WorldTitles')

# Category values for the colors
CATEGORY_CODES = pd.Categorical(ordered_mondiali['WorldTitles']).codes
#d1eeea,#a8dbd9,#85c4c9,#68abb8,#4f90a6,#3b738f,    #2a5674
COLORMAP = ["#154500" ,"#7db208", "#bcdd7a", "#acdffe", "#4e9bf8", "#0b2b81"]
# Select colors for each password according to its category.
#COLORS = np.array(COLORMAP)[CATEGORY_CODES]
COLORS = ['grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                             'grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                             'grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                             'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 
                             'grey', 'gold', 'grey', 'grey', 'grey', 'darkorange',
                             'mediumblue', 'limegreen', 'red', 'turquoise']

#plot orizzontale
plt.hlines(y=ordered_mondiali['Driver'], xmin=0, xmax=ordered_mondiali['WorldTitles'],
           color=COLORS)

plt.scatter(ordered_mondiali['WorldTitles'], ordered_mondiali['Driver'], 
          color = COLORS);
#titoli e nomi assi
plt.yticks(ordered_mondiali['Driver'], ordered_mondiali['Driver'])
#plt.title("A vertical lolipop plot", loc='left')
plt.xlabel('Number of world titles')
plt.ylabel('Driver')
#Mostra il plot
plt.show();





#LOLLIPOP PER MONDIALI VINTI CIRCOLARE
#definire per dimensione punti
TITLE_MAX = np.max(ordered_mondiali['WorldTitles'])
TITLE_MIN = np.min(ordered_mondiali['WorldTitles'])
#basso o alto x dimensione punti
def scale_to_interval(x, low=10, high=70):
    return ((x - TITLE_MIN) / (TITLE_MAX - TITLE_MIN)) * (high - low) + low
# Category values for the colors
CATEGORY_CODES = pd.Categorical(ordered_mondiali['WorldTitles']).codes
#d1eeea,#a8dbd9,#85c4c9,#68abb8,#4f90a6,#3b738f,    #2a5674
COLORMAP = ["#154500" ,"#7db208", "#bcdd7a", "#acdffe", "#4e9bf8", "#0b2b81"]
# Select colors for each password according to its category.
COLORS = ['grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                             'grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                             'grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                             'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 
                             'grey', 'orchid', 'grey', 'grey', 'grey', 'darkorange',
                             'mediumblue', 'limegreen', 'red', 'turquoise']


ANGLES = np.linspace(0, 2 * np.pi, len(ordered_mondiali['WorldTitles']), endpoint=False)
# Heights of the lines and y-position of the dot are given by the times.
HEIGHTS = np.array(ordered_mondiali['WorldTitles'])

PLUS = 15

# Initialize layout in polar coordinates
fig, ax = plt.subplots(figsize=(15, 15), subplot_kw={"projection": "polar"})
# Set background color to white, both axis and figure.
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
# Angular axis starts at 90 degrees, not at 0
ax.set_theta_offset(np.pi / 2)
# Reverse the direction to go counter-clockwise.
ax.set_theta_direction(-1)
# Add lines
ax.vlines(ANGLES, 0 + PLUS, HEIGHTS + PLUS, color=COLORS, lw=2)
# Add dots
ax.scatter(ANGLES, HEIGHTS + PLUS, color=COLORS);
# Start by removing spines for both axes
ax.spines["start"].set_color("none")
ax.spines["polar"].set_color("none")
# Remove grid lines, ticks, and tick labels.
ax.grid(False)
ax.set_xticks([])
ax.set_yticklabels([])
# Add our custom grid lines for the radial axis.
# These lines indicate one day, one week, one month and one year.
GREY1 = "#d6d6d6"
GREY2 = "#cccccc"
GREY3 = "#c1c1c1"
GREY4 = "#b7b7b7"
GREY5 = "#adadad"
GREY6 = "#a3a3a3"
GREY7 = "#999999"


HANGLES = np.linspace(0, 2 * np.pi, 200)
ax.plot(HANGLES, np.repeat(PLUS, 200), color= GREY1, lw=0.7)
ax.plot(HANGLES, np.repeat(1 + PLUS, 200), color= GREY1, lw=0.7)
ax.plot(HANGLES, np.repeat(2 + PLUS, 200), color= GREY2, lw=0.7)
ax.plot(HANGLES, np.repeat(3 + PLUS, 200), color= GREY3, lw=0.7)
ax.plot(HANGLES, np.repeat(4 + PLUS, 200), color= GREY4, lw=0.7)
ax.plot(HANGLES, np.repeat(5 + PLUS, 200), color= GREY5, lw=0.7)
ax.plot(HANGLES, np.repeat(6 + PLUS, 200), color= GREY6, lw=0.7)
ax.plot(HANGLES, np.repeat(7 + PLUS, 200), color= GREY7, lw=0.7)



#salvataggio figura
fig.savefig(f'LollipopCirc.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)



















