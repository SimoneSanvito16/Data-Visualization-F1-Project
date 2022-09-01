# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 12:00:54 2022

@author: gemelli
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np
import seaborn as sns

testUtenteRis = ('testUtenteRis.csv')
testUtenteRis = pd.read_csv(testUtenteRis)

testUtenteTime = ('testUtenteTemp.csv')
testUtenteTime = pd.read_csv(testUtenteTime)

questionario = ('questionario.csv')
questionario = pd.read_csv(questionario)

sbagliato_task1 = 3
giusto_task1 = 3
sbagliato_task2 = 1
giusto_task2 = 5
sbagliato_task3 = 0
giusto_task3 = 6

sbagliato = [3, 1, 0]
giusto = [3, 5, 6]
task = ["Task 1", "Task 2", "Task 3"]

tempoT1 = [80,49,85,95,120,117]
tempoT2 = [120,50,50,55,41,64]
tempoT3 = [67,90,110,95,51,96]
tempoMedio = [85, 50, 100]

#TEST UTENTE
#TEST UTENTE

#efficacia
fig, ax = plt.subplots()

ax.barh(task, giusto, label='Corrette', color = "lightgreen")
ax.barh(task, sbagliato, left=giusto, label='Errate', color = "lightcoral")

ax.set_ylabel('Task')
ax.set_xlabel('Numero di risposte')
ax.set_title('Efficacia delle visualizzazioni')

plt.show()
fig.savefig(f'Efficacia BarChart.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)



#efficienza

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(8, 10), sharex=True)
fig.suptitle('Efficienza delle visualizzazioni per le 3 task', fontsize = 16)
# Plot violin plot on axes 1
v1 = sns.violinplot(y=tempoT1, inner = 'stick', order = task, ax=axes[0], color = "lightskyblue")
v1.axhline(tempoMedio[0], color = "red")
v1.boxplot(tempoT1, positions=np.array([0]),
            widths=0.15, patch_artist=True,
            boxprops=dict(color="blue", facecolor="blue"),
            whiskerprops=dict(color="blue", linewidth=2),
            medianprops=dict(color="w", linewidth=2 ))
v1.set_xlabel('Task 1')
v1.set_ylabel('Tempo (in secondi)')

v2 = sns.violinplot(y=tempoT2, inner='stick', order = task, ax=axes[1], color = "lightskyblue")
v2.axhline(tempoMedio[1], color = "red")
v2.boxplot(tempoT2, positions=np.array([0]),
            widths=0.15, patch_artist=True,
            boxprops=dict(color="blue", facecolor="blue"),
            whiskerprops=dict(color="blue", linewidth=2),
            medianprops=dict(color="w", linewidth=2 ))
v2.set_xlabel('Task 2')
v2.set_ylabel('Tempo (in secondi)')

v3 = sns.violinplot(y=tempoT3, inner='stick', order = task, ax=axes[2], color = "lightskyblue")
v3.axhline(tempoMedio[2], color = "red")
v3.boxplot(tempoT3, positions=np.array([0]),
            widths=0.15, patch_artist=True,
            boxprops=dict(color="blue", facecolor="blue"),
            whiskerprops=dict(color="blue", linewidth=2),
            medianprops=dict(color="w", linewidth=2 ))
v3.set_xlabel('Task 3')
v3.set_ylabel('Tempo (in secondi)')

fig.set_size_inches(18, 8)
fig.savefig(f'Efficienza ViolinPlot.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)




#QUESTIONARIO
#QUESTIONARIO


#SCATTERPLOT
#SCATTERPLOT
category_names = ['1 - 2', '3 - 4', '5 - 6']
results = {
    'Utile Scatterplot': [1, 6, 7],
    'Chiara Scatterplot': [2, 4, 8],
    'Informativa Scatterplot': [0, 1, 13],
    'Bella Scatterplot': [0, 9, 5],
    'Val complessivo Scatterplot': [0, 5, 9]
}


def survey(results, category_names):
    
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    middle_index = data.shape[1]//2
    offsets = data[:, range(middle_index)].sum(axis=1) + data[:, middle_index]/2
    
    # Color Mapping
    category_colors = plt.get_cmap('coolwarm_r')(
        np.linspace(0.15, 0.85, data.shape[1]))
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot Bars
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths - offsets
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
    
    # Add Zero Reference Line
    ax.axvline(0, linestyle='--', color='black', alpha=.25)
    
    # X Axis
    ax.set_xlim(-15, 15)
    ax.set_xticks(np.arange(-15, 15, 1))
    ax.xaxis.set_major_formatter(lambda x, pos: str(abs(int(x))))
    
    # Y Axis
    ax.invert_yaxis()
    
    # Remove spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Ledgend
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    
    # Set Background Color
    fig.set_facecolor('#FFFFFF')

    return fig, ax


fig, ax = survey(results, category_names)
plt.show()
fig.savefig(f'Questionario Scatterplot.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)



#LOLLIPOP
#LOLLIPOP

category_names = ['1 - 2', '3 - 4', '5 - 6']
results = {
    'Utile Lollipop': [0, 5, 9],
    'Chiara Lollipop': [2, 3, 9],
    'Informativa Lollipop': [0, 4, 10],
    'Bella Lollipop': [0, 6, 8],
    'Val complessivo Lollipop': [0, 6, 8]
}


def survey(results, category_names):
    
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    middle_index = data.shape[1]//2
    offsets = data[:, range(middle_index)].sum(axis=1) + data[:, middle_index]/2
    
    # Color Mapping
    category_colors = plt.get_cmap('coolwarm_r')(
        np.linspace(0.15, 0.85, data.shape[1]))
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot Bars
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths - offsets
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
    
    # Add Zero Reference Line
    ax.axvline(0, linestyle='--', color='black', alpha=.25)
    
    # X Axis
    ax.set_xlim(-15, 15)
    ax.set_xticks(np.arange(-15, 15, 1))
    ax.xaxis.set_major_formatter(lambda x, pos: str(abs(int(x))))
    
    # Y Axis
    ax.invert_yaxis()
    
    # Remove spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Ledgend
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    
    # Set Background Color
    fig.set_facecolor('#FFFFFF')

    return fig, ax


fig, ax = survey(results, category_names)
plt.show()
fig.savefig(f'Questionario Lollipop.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)





#LINECHART
#LINECHART
category_names = ['1 - 2', '3 - 4', '5 - 6']
results = {
    'Utile LineChart': [0, 2, 12],
    'Chiara LineChart': [0, 3, 11],
    'Informativa LineChart': [0, 2, 12],
    'Bella LineChart': [0, 4, 10],
    'Val complessivo LineChart': [1, 2, 11]
}


def survey(results, category_names):
    
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    middle_index = data.shape[1]//2
    offsets = data[:, range(middle_index)].sum(axis=1) + data[:, middle_index]/2
    
    # Color Mapping
    category_colors = plt.get_cmap('coolwarm_r')(
        np.linspace(0.15, 0.85, data.shape[1]))
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot Bars
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths - offsets
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
    
    # Add Zero Reference Line
    ax.axvline(0, linestyle='--', color='black', alpha=.25)
    
    # X Axis
    ax.set_xlim(-15, 15)
    ax.set_xticks(np.arange(-15, 15, 1))
    ax.xaxis.set_major_formatter(lambda x, pos: str(abs(int(x))))
    
    # Y Axis
    ax.invert_yaxis()
    
    # Remove spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Ledgend
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    
    # Set Background Color
    fig.set_facecolor('#FFFFFF')

    return fig, ax


fig, ax = survey(results, category_names)
plt.show()
fig.savefig(f'Questionario LineChart.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)


#ALLUVIALPLOT
#ALLUVIALPLOT
category_names = ['1 - 2', '3 - 4', '5 - 6']
results = {
    'Utile Alluvial Plot': [1, 4, 9],
    'Chiara Alluvial Plot': [1, 5, 8],
    'Informativa Alluvial Plot': [0, 3, 11],
    'Bella Alluvial Plot': [3, 6, 5],
    'Val complessivo Alluvial Plot': [1, 7, 6]
}


def survey(results, category_names):

    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    middle_index = data.shape[1]//2
    offsets = data[:, range(middle_index)].sum(axis=1) + data[:, middle_index]/2
    
    # Color Mapping
    category_colors = plt.get_cmap('coolwarm_r')(
        np.linspace(0.15, 0.85, data.shape[1]))
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot Bars
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths - offsets
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
    
    # Add Zero Reference Line
    ax.axvline(0, linestyle='--', color='black', alpha=.25)
    
    # X Axis
    ax.set_xlim(-15, 15)
    ax.set_xticks(np.arange(-15, 15, 1))
    ax.xaxis.set_major_formatter(lambda x, pos: str(abs(int(x))))
    
    # Y Axis
    ax.invert_yaxis()
    
    # Remove spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Ledgend
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    
    # Set Background Color
    fig.set_facecolor('#FFFFFF')

    return fig, ax


fig, ax = survey(results, category_names)
plt.show()
fig.savefig(f'Questionario Alluvial.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)





plt.close()
# CORRPLOT
#CORRPLOT

# SCATTERPLOT
data_vuoto = []
scatter_data = pd.DataFrame(data_vuoto)
scatter_data["utile"] = questionario["Utile Scatterplot"]
scatter_data["chiara"] = questionario["Chiara Scatterplot"]
scatter_data["informativa"] = questionario["Informativa Scatterplot"]
scatter_data["bella"] = questionario["Bella Scatterplot"]
scatter_data["valore complessivo"] = questionario["Valore complessivo Scatterplot"]

corr_scatter = scatter_data.corr()
mask_scatter = np.zeros_like(corr_scatter)
mask_scatter[np.triu_indices_from(mask_scatter)] = True
sns.heatmap(corr_scatter, cmap = sns.diverging_palette(256, 0, sep = 80, n=7, as_cmap = True), annot = True, mask = mask_scatter)
fig.savefig(f'Corrplot Scatterplot.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)


#LOLLIPOP
plt.close()

data_vuoto = []
lollipop_data = pd.DataFrame(data_vuoto)
lollipop_data["utile"] = questionario["Utile Lollipop"]
lollipop_data["chiara"] = questionario["Chiara Lollipop"]
lollipop_data["informativa"] = questionario["Informativa Lollipop"]
lollipop_data["bella"] = questionario["Bella Lollipop"]
lollipop_data["valore complessivo"] = questionario["Valore complessivo Lollipop"]

corr_lollipop = lollipop_data.corr()
mask_lollipop = np.zeros_like(corr_lollipop)
mask_lollipop[np.triu_indices_from(mask_lollipop)] = True
sns.heatmap(corr_lollipop, cmap = sns.diverging_palette(256, 0, sep = 80, n=7, as_cmap = True), annot = True, mask = mask_lollipop)
fig.savefig(f'Corrplot Lollipop.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)



#LINECHART
plt.close()

data_vuoto = []
linechart_data = pd.DataFrame(data_vuoto)
linechart_data["utile"] = questionario["Utile LineChart"]
linechart_data["chiara"] = questionario["Chiara LineChart"]
linechart_data["informativa"] = questionario["Informativa LineChart"]
linechart_data["bella"] = questionario["Bella LineChart"]
linechart_data["valore complessivo"] = questionario["Valore complessivo LineChart"]

corr_linechart = linechart_data.corr()
mask_linechart = np.zeros_like(corr_linechart)
mask_linechart[np.triu_indices_from(mask_linechart)] = True
sns.heatmap(corr_linechart, cmap = sns.diverging_palette(256, 0, sep = 80, n=7, as_cmap = True), annot = True, mask = mask_linechart)
fig.savefig(f'Corrplot LineChart.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)


#ALLUVIALPLOT
plt.close()

data_vuoto = []
alluvial_data = pd.DataFrame(data_vuoto)
alluvial_data["utile"] = questionario["Utile Alluvial"]
alluvial_data["chiara"] = questionario["Chiara Alluvial"]
alluvial_data["informativa"] = questionario["Informativa Alluvial"]
alluvial_data["bella"] = questionario["Bella Alluvial"]
alluvial_data["valore complessivo"] = questionario["Valore complessivo Alluvial"]

corr_alluvial = alluvial_data.corr()
mask_alluvial = np.zeros_like(corr_alluvial)
mask_alluvial[np.triu_indices_from(mask_alluvial)] = True
sns.heatmap(corr_alluvial, cmap = sns.diverging_palette(256, 0, sep = 80, n=7, as_cmap = True), annot = True, mask = mask_alluvial)
fig.savefig(f'Corrplot Alluvial.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)


