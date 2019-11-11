import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cleanning_fooddf
import cleanning_pollutiondf
import analysis
import scrapping
from bs4 import BeautifulSoup
import requests

def GetFile(path):
    df = pd.read_csv(path)
    return df

def CleaningFoodDf(df):
    df=cleanning_fooddf.DropColumns(df)
    df=cleanning_fooddf.CleanColNames(df)
    df=cleanning_fooddf.CountryNames(df)
    df=cleanning_fooddf.FilterUeCountries(df)
    df=cleanning_fooddf.GroupSumCountries(df)
    df=cleanning_fooddf.RenameColArea(df)
    df=cleanning_fooddf.RecolocateDf(df)
    
    return df

def Scrapping(url):
    step1=scrapping.GetSoup(url)
    values=scrapping.InsertCols(step1)
    df=scrapping.CreateDf(values,step1)
    return df

def CleaningPollDf(df):
    df=cleanning_pollutiondf.SelectCols(df)
    df=cleanning_pollutiondf.CorrectNameCols(df)
    df=cleanning_pollutiondf.SelectCols(df)
    df=cleanning_pollutiondf.ReplaceUnknownVal(df)
    df=cleanning_pollutiondf.ChangeColType(df)
    df=cleanning_pollutiondf.TransformDf(df)
    return cleanning_pollutiondf.ExportCleanDfEmissions(df)

def Analysis(dffood,country):
    df_poll=analysis.OpenData('../output/Pollution-emissions.csv')
    maximos=analysis.Maximum(dffood,df_poll,country)
    print(maximos)
    grafica_1, grafica_2 = analysis.CompareEvolutionGraffics(dffood,df_poll,country)
    analysis.SaveGraffics(grafica_1, grafica_2)
    