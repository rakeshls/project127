from bs4 import BeautifulSoup as bs
from bs4.element import TemplateString
import requests
import pandas as pd

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
print(page)

soup = bs(page.text,'html.parser')
star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
V_Mag = []
Star_names = []
Bayer_designation = []
Distance = []
Spectral_class = []
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    V_Mag.append(temp_list[i][0])
    Star_names.append(temp_list[i][1])
    Bayer_designation.append(temp_list[i][2])
    Distance.append(temp_list[i][3])
    Spectral_class.append(temp_list[i][4])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    
df2 = pd.DataFrame(list(zip(V_Mag,Star_names,Bayer_designation,Distance,Spectral_class,Mass,Radius,Lum)),
columns=['V_Mag','Star_name','Bayer_designation','Distance','Spectral_class','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('stars.csv')