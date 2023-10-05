#step1.프로젝트에 필요한 패키지 불러온다.
from bs4 import BeautifulSoup as bs
import requests

#step2.크롤링할 url 주소를 입력한다.
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%89%B4%EC%A7%84%EC%8A%A4'

#step3.requests 패키지의 함수를 이용해 url의 html 문서를 가져온다.
response = requests.get(url)
html_text=response.text

#step4.bs4 패키지의 함수를 이용해서 html 문서를 파싱한다.
soup = bs(html_text, 'html.parser')

#step5.bs4 패키지의 select 함수와 선택자 개념을 이용해서 뉴스기사 제목을 모두 가져온다.
titles = soup.select('a.news_tit')

for i in titles:
    title = i.get_text()
    print(title)
