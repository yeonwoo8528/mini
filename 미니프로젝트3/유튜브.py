#step1.관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
import time

#step2.검색할 키워드 입력
word = input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://www.youtube.com/'
driver = webdriver.Chrome('/Users/USER/Desktop/네트워크/chromedriver_win32/chromedriver')
driver.get(url)
time.sleep(3)

#step4.검색창에 키워드 입력 후 엔터
search_box = driver.find_element_by_name("search_query")
search_box.send_keys(word)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

#step5.스크롤 다운
body = driver.find_element_by_tag_name('body')
for i in range(20):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

#step6.값을 저장받을 리스트
thumbnail_list = list()
title_list = list()
length_list = list()
view_list = list()
date_list = list()

#step7.크롤링 시작
idx = 1
count = 1
while(1):

    #step8.리스트에 해당하는 xpath
    thumbnail_xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer['+str(count)+']/div[3]/ytd-video-renderer['+str(idx - (count - 1)*19)+']/div[1]/ytd-thumbnail/a/yt-image/img'
    title_xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer['+str(count)+']/div[3]/ytd-video-renderer['+str(idx - (count - 1)*19)+']/div[1]/div/div[1]/div/h3/a/yt-formatted-string'
    length_xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer['+str(count)+']/div[3]/ytd-video-renderer['+str(idx - (count - 1)*19)+']/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span'
    view_xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer['+str(count)+']/div[3]/ytd-video-renderer['+str(idx - (count - 1)*19)+']/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]'
    date_xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer['+str(count)+']/div[3]/ytd-video-renderer['+str(idx - (count - 1)*19)+']/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]'
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, thumbnail_xpath)))

    #step9.동영상 썸네일 추출
    thumbnail = driver.find_elements_by_xpath(thumbnail_xpath)
    for thumb in thumbnail:
        thumbnail_link = thumb.get_attribute('src')
        thumbnail_list.append(thumbnail_link)
    
    #step10.동영상 제목 추출
    title = driver.find_elements_by_xpath(title_xpath)
    for tit in title:
        title_list.append(tit.text)

    #step11.동영상 영상 길이 추출
    length = driver.find_elements_by_xpath(length_xpath)
    for leng in length:
        length_list.append(leng.text)

    #step12.동영상 조회수 추출
    view = driver.find_elements_by_xpath(view_xpath)
    for vi in view:
        view_list.append(vi.text)

    #step13.동영상 날짜 추출
    date = driver.find_elements_by_xpath(date_xpath)
    for da in date:
        date_list.append(da.text)

    #step14.크롤링 멈춤
    idx += 1
    if idx == 31:
        break

    #step15.예외 처리
    if (idx - 1) % 19 == 0:
        count += 1

#step16.동영상 전처리
for i in range(30):
    
    #step16-1.반각 -> 전각
    title_list[i] = title_list[i].replace(":", "：")
    
    length_list[i] = length_list[i].replace(":", "：")
    
    #step16-2.문자형 -> 정수형
    view_list[i] = view_list[i].replace("조회수 ", "").replace("천", "000").replace("만", "0000").replace("억", "00000000")
    if '.' in view_list[i]:
        view_list[i] = view_list[i].replace(".", "").replace("0회", "")
    elif '없음' in view_list[i]:
        view_list[i] = view_list[i].replace("없음", "0")
    else:
        view_list[i] = view_list[i].replace("회", "")
    view_list[i] = int(view_list[i])
    
    date_list[i] = date_list[i].replace(" 전", "")
    if '분' in date_list[i]:
        date_list[i] = int(date_list[i].replace("분", ""))
    elif '시간' in date_list[i]:
        date_list[i] = int(date_list[i].replace("시간", "")) * 60
    elif '일' in date_list[i]:
        date_list[i] = int(date_list[i].replace("일", "")) * 60 * 24
    elif '주' in date_list[i]:
        date_list[i] = int(date_list[i].replace("주", "")) * 60 * 24 * 7
    elif '개월' in date_list[i]:
        date_list[i] = int(date_list[i].replace("개월", "")) * 60 * 24 * 30
    elif '년' in date_list[i]:
        date_list[i] = int(date_list[i].replace("년", "")) * 60 * 24 * 365

#step17.동영상 sorting
video = list(zip(thumbnail_list, title_list, length_list, view_list, date_list))
p = int(input('조회순 정렬: press 1, 최신순 정렬: press 2 - '))
if p == 1:
    video = sorted(video, key = lambda x : -x[3])
elif p == 2:
    video = sorted(video, key = lambda x : x[4])

#step18.파일 경로 설정
import os
path_folder = '/Users/USER/Desktop/네트워크/파이썬 과제/유튜브/'
if not os.path.isdir(path_folder):
    os.mkdir(path_folder)

#step19.동영상 저장
i = 0
for vid in video:
    i += 1
    urlretrieve(vid[0], path_folder + f'{i} ' + vid[1] + ' ' + vid[2] + f'.png')
print(video)
driver.close()
