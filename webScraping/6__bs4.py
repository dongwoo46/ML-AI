# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.title)
# print(soup.title.get_text()) 
# print(soup.a) # 처음발견되는 a tag가져와라
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element 의 href 속성 정보를 출력

# print(soup.find("a", attrs={"class","Nbtn_upload"})) # a tag에 클래스가 Nbtn_upload인 것을 찾아라
# print(soup.find(attrs={"class","Nbtn_upload"})) # 클래스가 Nbtn_upload인 것을 찾아라

# print(soup.find("li", attrs={"class","rank01"}))
# rank1 = soup.find("li", attrs={"class","rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank1.parent)
# rank2 =rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_sibling("li"))



webtoon = soup.find("a", text="독립일기-11화 밥공기 딜레마")
print(webtoon)

