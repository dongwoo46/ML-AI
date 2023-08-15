import requests
from bs4 import BeautifulSoup

url = "https://entertain.naver.com/home"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"] # a tag의 href값을 가져오기
# print(title)
# print("https://comic.naver.com" + link)

# 만화제목+링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title,link)
    

# 평점 구하기
cartoons = soup.find_all('div',attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates +=float(rate)
print("전체점수:", total_rates)
print("평균점수:", total_rates/len(cartoons))