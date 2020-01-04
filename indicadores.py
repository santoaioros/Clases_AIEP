from bs4 import BeautifulSoup
import requests
import random
import datetime

url = 'https://si3.bcentral.cl/indicadoressiete/secure/indicadoresdiarios.aspx'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

valorUf = soup.find_all('label', id='lblValor1_1')
valorDolar = soup.find_all('label', id='lblValor1_3')
valorEuro = soup.find_all('label', id='lblValor1_5')
indicadores = list()
for i in valorUf:
    indicadores.append(i.text)
for i in valorDolar:
    indicadores.append(i.text)
for i in valorEuro:
    indicadores.append(i.text)
fecha = datetime.date.today()
print('Fecha actual: {}'.format(fecha))
print('El valor de los siguientes indicadores es: ')
print('')
print('Valor UF:    {}'.format(indicadores[0]))
print('Valor DOLAR: {}'.format(indicadores[1]))
print('Valor EURO:  {}'.format(indicadores[2]))
print('')
print('//Base de datos estadisticos - Banco Central de Chile// ')