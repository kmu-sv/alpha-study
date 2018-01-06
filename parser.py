# parser.py
import requests
from bs4 import BeautifulSoup

# HTTP GET Request

req = requests.get('https://beomi.github.io/beomi.github.io_old/')

# HTML 소스 가져오기

html = req.text

# BeautifulSoup으로 html소스를 python 객체로 변환하기
# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할 것인지 명시
# 이 글에서는 python 내장 html.parser를 이용했다.

soup = BeautifulSoup(html, 'html.parser')

# CSS Selector를 통해 html요소들을 찾아낸다.
my_titles = soup.select(
    'h3 > a'
    )

# my_titles는 string의 list가 아니라 soup 객체들의 list이다.
# 따라서 태그의 속성들도 이용할 수 있는데, a 태그의 경우 href 속성이 대표적인 예시이다.

# my_titles는 list 객체 
for title in my_titles:
    #Tag안의 텍스트
    print(title.text)

    #Tag의 속성을 가져오기(ex : herf속성)
    print(title.get('href'))
