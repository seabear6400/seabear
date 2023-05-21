from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="

print("네이버")
keyword = input("검색하고 싶은 단어를 입력하세요 : ")

search_url = base_url + keyword

r = requests.get(search_url)

soup = BeautifulSoup(r.text, "html.parser")

items = soup.select(".api_txt_lines.total_tit")

for e, item in enumerate(items, 1):
    print(f"{e} : {item.text}")

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://search.naver.com/search.naver?where=view&sm=tab_jum&query=")

bsObject = BeautifulSoup(html, "html.parser")

for link in bsObject.find_all('img'):
    print(link['alt'], link['src'])
print("sbs뉴스")
base_url = "https://news.sbs.co.kr/news/newsMain.do?page=1&mn_id=2000000000"

keyword = input("검색하고 싶은 단어를 입력하세요 : ")

search_url = base_url + "&keyword=" + keyword

r = requests.get(search_url)

soup = BeautifulSoup(r.text, "html.parser")

items = soup.select(".api_txt_lines.total_tit")

for e, item in enumerate(items, 1):
    print(f"{e} : {item.text}")


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://news.sbs.co.kr/news/newsMain.do?page=1&mn_id=2000000000")

bsObject = BeautifulSoup(html, "html.parser")
for link in bsObject.find_all('img'):
    print(link['alt'], link['src'])
