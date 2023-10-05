#step1.관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#step2.검색할 키워드 입력
gLFyf = input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://www.google.com/'
driver = webdriver.Chrome('/Users/USER/Desktop/네트워크/chromedriver_win32/chromedriver')
driver.get(url)
time.sleep(3)

#step4.검색창에 키워드 입력 후 엔터
search_box = driver.find_element_by_css_selector("textarea.gLFyf")
search_box.send_keys(gLFyf)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

#step5.동영상 탭 클릭
driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[4]').click()
time.sleep(2)

#step6.동영상 추출
news_thumbnail = driver.find_elements_by_css_selector("div.VYkpsb")
link_thumbnail = []
for video in news_thumbnail:
    link = video.get_attribute('data-url')
    if link is not None:
        link_thumbnail.append(link)

import os
path_folder = '/Users/USER/Desktop/네트워크/파이썬 과제/코로나/'
if not os.path.isdir(path_folder):
    os.mkdir(path_folder)

from urllib.request import urlretrieve
i = 0
for link in link_thumbnail:          
    i += 1
    urlretrieve(link, path_folder + gLFyf + f'{i}.mp4')
