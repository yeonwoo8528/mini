#step1.관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#step2.검색할 키워드 입력
query = input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://www.naver.com/'
driver = webdriver.Chrome('/Users/USER/Desktop/네트워크/chromedriver_win32/chromedriver')
driver.get(url)
time.sleep(3)

#step4.검색창에 키워드 입력 후 엔터
search_box = driver.find_element_by_css_selector("input#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

#step5.이미지 탭 클릭
driver.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
time.sleep(2)

#step6.이미지 추출
news_thumbnail = driver.find_elements_by_css_selector("img._image._listImage")
link_thumbnail = []
for img in news_thumbnail:
    link_thumbnail.append(img.get_attribute('src'))

import os
path_folder = '/Users/USER/Desktop/네트워크/파이썬 과제/고양이/'
if not os.path.isdir(path_folder):
    os.mkdir(path_folder)

from urllib.request import urlretrieve
i = 0
for link in link_thumbnail:          
    i += 1
    urlretrieve(link, path_folder + query + f'{i}.jpg')
    if(i == 10):
        break
