from bs4 import BeautifulSoup
import requests
import pandas as pd 

url = 'https://es.fifa.com/fifa-world-ranking/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

pais = soup.find_all('span', class_='fi-module-ranking__ranking__item__name')
seleccion = list()
contador = 0
for i in pais:
    if contador < 10:
        seleccion.append(i.text)
    else:
        break
    contador +=1 

pts = soup.find_all('span', class_='fi-module-ranking__ranking__item__points')
puntos = list()
contador = 0
for i in pts:
    if contador < 10:
        puntos.append(i.text)
    else:
        break
    contador +=1  


df = pd.DataFrame({'SELECCION': seleccion,'PUNTUACION': puntos}, index=list(range(1,11)))
print('')
print('LAS 10 MEJORES SELECCION RANKING FIFA.COM')
print('')
print(df)