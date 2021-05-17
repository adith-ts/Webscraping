from bs4 import BeautifulSoup
import requests
from requests.api import get
gname = input("Enter the series name: ")
html_text = requests.get(f"https://www.imdb.com/find?q={gname}").text
soup = BeautifulSoup(html_text, 'lxml')

series= soup.find('td', class_='result_text')
link = series.find('a')
link= str(link)
res = link.find('"')
bres = link.rfind('"')
x = link [res+1:bres] 

rlink = requests.get(f"https://www.imdb.com{x}").text
soup2 = BeautifulSoup(rlink, 'lxml')
rating = soup2.find('strong')
rating=str(rating)
rat = rating.find('"')
rev_rat = rating.find('"><')
final_rating = rating[rat+1:rev_rat]


series=series.text
print("INFO-->",series)
print("Rating-->",final_rating)
print('test')
    
    

