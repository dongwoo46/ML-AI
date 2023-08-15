import requests
url = "https://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status() # 문제가 있으면 알려주고 없으면 출력해줌


# res의 주소의 html을 읽어와서 mygoogle.html파일로 만들어줌
with open("nanocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)