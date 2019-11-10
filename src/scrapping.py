from bs4 import BeautifulSoup


def ExtractOddColValues(odd_number):
    odd_values=[]
    odd_row = soup.find_all('tr', attrs={'class':'row{}'.format(odd_number)})
    for row in odd_row:    
        r=row.select('.Data')    
        for d in r:
            values_per_row=str(d.text.replace(u'\xa0', u''))
            odd_values.append(values_per_row)
    valores.append(odd_values)


def ExtractEvenColValues(even_number):
    even_values=[]
    even_row = soup.find_all('tr', attrs={'class':'row{}'.format(even_number)})
    for row in even_row:    
        r=row.select('.Data2')    
        for d in r:
            values_per_row=str(d.text.replace(u'\xa0', u''))
            even_values.append(values_per_row)
    valores.append(even_values)
