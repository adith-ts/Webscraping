from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')
soup = BeautifulSoup(html_text.text, 'lxml')
series = soup.find_all('td', class_='titleColumn')


print(series.title)
