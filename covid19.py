import requests
from bs4 import BeautifulSoup

request = requests.get('http://ncov.mohw.go.kr/index_main.jsp')
html = request.text

soup = BeautifulSoup(html, 'html.parser')

# <a> 태그를 포함하는 요소를 추출합니다.

links = soup.select('li > a')

# 모든 링크에 하나씩 접근합니다.

for link in links:

    # 링크가 href 속성을 가지고 있다면

    if link.has_attr('href'):
        
            print(link.text)

