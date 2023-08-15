# pip install requests
import requests

res = requests.get("https://google.com")
# res = requests.get("https://nadocoding.tistory.com")
res.raise_for_status() # 문제가 있으면 알려주고 없으면 출력해줌

# print("응답코드: ", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("문제가 생겼다. [에러코드", res.status_code,"]")


print(len(res.text))
print(res.text)

# res의 주소의 html을 읽어와서 mygoogle.html파일로 만들어줌
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)