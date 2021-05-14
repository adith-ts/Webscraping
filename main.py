from bs4 import BeautifulSoup
import requests
from requests.api import get
gname = input("Enter the series name: ")
html_text = requests.get(f"https://www.imdb.com/find?q={gname}").text
soup = BeautifulSoup(html_text, 'lxml')
series= soup.find('td', class_='result_text').text
print("INFO-->",series)
