import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

prices = soup.findAll("h4", class_ := "float-end price card-title pull-right")
# print(len(prices))
for i in prices:
    print(i.string)

desc = soup.findAll("p", class_ := "description card-text")
for i in desc:
    print(i.text)
