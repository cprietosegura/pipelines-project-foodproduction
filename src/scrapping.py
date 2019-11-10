from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

def GetSoup(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def InsertCols(step1):
    valores=[]
    
    for number in range(1, 49):
            
        if number%2==0:
            even_values=[]
            even_row = step1.find_all('tr', attrs={'class':'row{}'.format(number)})
            for row in even_row:    
                r=row.select('.Data2')    
                for d in r:
                    values_per_row=str(d.text.replace(u'\xa0', u''))
                    even_values.append(values_per_row)
            valores.append(even_values)    
        else:
            odd_values=[]
            odd_row = step1.find_all('tr', attrs={'class':'row{}'.format(number)})
            for row in odd_row:    
                r=row.select('.Data')    
                for d in r:
                    values_per_row=str(d.text.replace(u'\xa0', u''))
                    odd_values.append(values_per_row)
            valores.append(odd_values)
    
    return valores

def CreateDf(valores,step1):
    country=step1.findAll(True, {'class':['RowDimLabel', 'RowDimLabel2']})
    country_col=[]
    for c in country:
        country_col.append((c.text)) 
    name_col = []
    for f in range(1990, 2018):
        name_col.append(str('{}'.format(f)))   
    
       
    empty_df= pd.DataFrame(np.zeros([len(set(country_col))-1, len(name_col)])*np.nan)
    empty_df.columns = empty_df.columns[:0].tolist() + name_col
    for value_list in range(len(valores)):
        empty_df.loc[value_list] = valores[value_list]
    
    countries=[country for country in country_col if country!='']
    countries.remove('Non-OECD Economies')
    empty_df=empty_df.drop(48)
    empty_df.insert(0, 'Country', countries)
    
    return empty_df