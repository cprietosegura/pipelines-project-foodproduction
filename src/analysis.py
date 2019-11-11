import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def OpenData(file):
    df = pd.read_csv(file)
    return df

def Maximum(df_food,df_poll,country):
    max_year_food = df_food.loc[df_food[country].idxmax()]
    max_year_poll = df_poll.loc[df_poll[country].idxmax()]
    return '\n The year with more food production in {} was {} and with more gas emissions was {}.'.format(country,int(max_year_food[0]), int(max_year_poll[1]))

def CompareEvolutionGraffics(df_food,df_poll,country):
    grafica_1=df_food.plot(x='Year', y=[country])
    grafica_2=df_poll.plot(x='Year', y=[country])
    print('Check your output to analyse the graffics and study the correlation of these levels throughout the last years.')
    return grafica_1,grafica_2

def SaveGraffics(grafica_1, grafica_2): # TENGO DOS GRAFICAS
    fig1 = grafica_1.get_figure()
    fig1.savefig('../output/graf_food.png')
    #plt.savefig('../output/graf_food.png', dpi= 100)
    fig2 = grafica_2.get_figure()
    fig2.savefig('../output/graf_poll.png')
    #plt.savefig('../output/graf_poll.png', dpi= 100)
    