import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def OpenData(file):
    df = pd.read_csv(file)
    return df

def Maximum(df,country):
    max_year = df.loc[df[country].idxmax()]
    return 'The year with more production was:',int(max_year[0])

def CompareEvolutionGraffics(df_food,df_poll,country):
    grafica_1=df_food.plot(x='Year', y=[country])
    grafica_2=df_poll.plot(x='Year', y=[country])
    return grafica_1,grafica_2

def SaveGraffics(grafica_1, grafica_2): # TENGO DOS GRAFICAS
    fig = grafica_1.get_figure()
    fig.savefig('graf_food' + '.png')
    fig = grafica_2.get_figure()
    fig.savefig('graf_poll' + '.png')