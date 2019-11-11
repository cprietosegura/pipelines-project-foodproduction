import god
import argparse

def recibeConfig():
    my_parser = argparse.ArgumentParser(description="""This program provides you with information 
    about food production and its relation with Greenhouse gas emissions within the European Union. 
    The data has been extracted from the Organisation for Economic Co-operation and Development and kaggle.com. 
    Choose an UE country to obtain information.""")
    my_parser.add_argument('--country',
                           type=str,
                           help='Enter a country of the EU',
                           default="Spain")
    args = my_parser.parse_args()
    #print(args)
    return args

def CheckCountryData(country):
    dffood=god.GetFile("../input/FAO.csv")
    dffood=god.CleaningFoodDf(dffood)
    dfpoll=god.Scrapping('https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG')
    dfpoll=god.CleaningPollDf(dfpoll)
    graffic=god.Analysis(dffood,country) #el pais es lo que tiene que meter el usuario
    #print(graffic)


def main():
    
    config = recibeConfig()
    CheckCountryData(config.country)

if __name__ == "__main__":
    main()