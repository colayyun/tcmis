import requests
from bs4 import BeautifulSoup


url = "http://www.atmovies.com.tw/movie/next/"
Data = requests.get(url)
Data.encoding = "utf-8"
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".flimListALLX li")


for x in result:
	print("電影介紹:http://www.atmovies.com.tw" + x.find("a").get("href"))
	print()