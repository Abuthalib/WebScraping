import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text, "lxml")
# print(soup.find('div'))

price = soup.find("h4", {"class": "float-end price card-title pull-right"}).string
print(price)

desc = soup.find(("p", {"class": "description card-text"})).string
print(desc)
