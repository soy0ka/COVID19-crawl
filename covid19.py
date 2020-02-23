import requests
from bs4 import BeautifulSoup

request = requests.get('http://ncov.mohw.go.kr/index_main.jsp')
html = request.text

soup = BeautifulSoup(html, 'html.parser')

links = soup.select('li > a')
for link in links:

    if link.has_attr('href'):
        
            print(link.text)

