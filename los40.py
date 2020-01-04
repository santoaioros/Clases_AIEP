from bs4 import BeautifulSoup
import requests
import pandas as pd 


url = 'https://los40.cl/lista-los-40'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#numero

nm = soup.find_all('div', class_='number')
numero = list()
count = 0
for i in nm:
    if count < 40:
        numero.append(i.text)
    else:
        break
    count +=1 

#titulo

tt = soup.find_all('div', class_='title')
titulo = list()
count = 0
for i in tt:
    if count < 40:
        titulo.append(i.text)
    else:
        break
    count +=1 

#autor

aut = soup.find_all('div', class_='author')
autor = list()
count = 0
for i in aut:
    if count < 40:
        autor.append(i.text)
    else:
        break
    count +=1 

#album

al = soup.find_all('div', class_='albun')
album = list()
count = 0
for i in al:

    if count < 40:
        album.append(i.text)
    else:
        break
    count +=1 

#semana
sem = soup.find_all('span', id='date-check')
semana = list()
for i in sem:
    semana.append(i.text)
semana_str = ''.join(semana)
df = pd.DataFrame({'POSICION': numero,'TITULO': titulo, 'AUTOR': autor, 'ALBUM': album}, index=list(range(1,41)))

print('')
print('░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓               LOS PRINCIPALES               ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░')
print('░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓             RANKING DEL 40 AL 1             ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░')
print('░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓          LISTADO DE VOTACIONES DEL          ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░')
print('                                                     {}'.format(semana_str))
print('')
print(df)

df.to_csv('los40.csv',index = False)