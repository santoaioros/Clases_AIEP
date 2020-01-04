from bs4 import BeautifulSoup
import requests
import pandas as pd 

url = 'https://www.ecartelera.com/listas/mejores-peliculas/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#año

yr = soup.find_all('div', class_='year')
year = list()
contador = 0
for i in yr:
    if contador < 40:
        year.append(i.text)
    else:
        break
    contador +=1 

#titulo

tt = soup.find_all('p', class_='title')
title = list()
contador = 0
for i in tt:
    if contador < 40:
        title.append(i.text)
    else:
        break
    contador +=1  

#notaverde

nt = soup.find_all('div', class_='nota verde')
nota = list()
contador = 0
for i in nt:
    if contador < 40:
        nota.append(i.text)
    else:
        break
    contador +=1   

df = pd.DataFrame({'AÑO': year,'TITULO': title, 'NOTA': nota}, index=list(range(1,41)))
print('')
print(' ♥♦♣♠ ♥♦♣♠  LAS 50 MEJORES PELICULAS // E-CARTELERA   ♥♦♣♠  ♥♦♣♠')
print('')
print(df)
