import requests

url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzAzMDFfMTAz%2FMDAxNjc3NjY1NTA0MDc1.3erUVCKtQp3DHtou1niacALZp62rAFNn0WZozBEbFEog.HKsUzNQtYxWk9G0Ahhgr3N5Gjxmb5e2RdKJLIhWP55Ag.JPEG.tony2351%2FKakaoTalk_20230221_193250475.jpg&type=a340' 
savename='고양이.png'  # 저장 파일 명

mem=requests.get(url).content 

with open(savename, "wb") as f:    #바이너리(이미지)일 경우 'wb',  텍스트일 경우 'w'
    f.write(mem)
    print("저장완료!")
