import requests_async as requests
from bs4 import BeautifulSoup

async def main():
    request = await requests.get('http://ncov.mohw.go.kr/index_main.jsp')
    html = request.text

    soup = BeautifulSoup(html, 'html.parser')

    links = soup.select('li > a')
    for link in [link for link in linkes if link.has_attr('href')]:
        print(link.text)

