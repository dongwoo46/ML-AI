import requests
from bs4 import BeautifulSoup

url = "https://entertain.naver.com/home"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a",attrs={"class":"title"}) # a태그이고 class속성명이 title인거 가져오기
# class속성이 title인 모든 a태그 반환
for cartoon in cartoons:
    print(cartoon.get_text())