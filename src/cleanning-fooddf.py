import pandas as pd

def ImportDF(path):
    df = pd.read_csv(path)
    return df

def DropColumns(df):
    df=df[['Area','Y1990', 'Y1991', 'Y1992', 'Y1993',
       'Y1994', 'Y1995', 'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001',
       'Y2002', 'Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009',
       'Y2010', 'Y2011', 'Y2012', 'Y2013']]
   
    return df

def CleanColNames(df):
    df.columns = df.columns.str.replace("Y", "")
    return df

def CountryNames(df):
    df['Area'][41]='Republic of Cyprus'
    df['Area'][42]='Czech Republic'
    return df

def FilterUeCountries(df):
    eu=['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Republic of Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland',
    'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 
    'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'United Kingdom']
    df = df[df['Area'].isin(eu)]
    return df

def GroupSumCountries(df):
    df=df.groupby('Area').sum().reset_index()
    return df

def RenameColArea(df):
    df = df.rename(columns={"Area": "Country"})
    return df

def RecolocateDf(df):
    df=df.T
    df.columns = df.iloc[0]
    df.drop(df.tail(1).index,inplace=True) 
    df.drop(df.head(1).index,inplace=True)
    df.reset_index(level=0, inplace=True)
    df = df.rename(columns={"index": "Year"})
    df = df.apply(pd.to_numeric)
    return df


def ExportCleanDfFood(df):
    return df.to_csv(r'./output/Food-production.csv')