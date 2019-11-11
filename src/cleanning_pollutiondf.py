import pandas as pd

def SelectCols(df):
    df=df[['Country', '1990', '1991', '1992', '1993', '1994', '1995', '1996',
       '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
       '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']]
    return df

def CorrectNameCols(df):
    df.at[28,'Country']='Slovakia'
    return df

def ReplaceUnknownVal(df):
    df=df.replace('..', 0.0)
    return df

def ChangeColType(df):
    for col in df.columns:
        if col=='Country':
            df[col] = df[col].astype(str)
        else:
            df[col] = df[col].astype(float)
    return df

def TransformDf(df):
    df=df.T
    df.columns = df.iloc[0]
    df.drop(df.tail(1).index,inplace=True) 
    df.drop(df.head(1).index,inplace=True)
    df.reset_index(level=0, inplace=True)
    df = df.rename(columns={"index": "Year"})
    return df

def ExportCleanDfEmissions(df):
    return df.to_csv('../output/Pollution-emissions.csv')

