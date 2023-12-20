import requests
from bs4 import BeautifulSoup
import re

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

data = soup.findAll(["h4", "p", "a"])
# print(data)

data = soup.findAll(string  = re.compile("Galaxy"))
print(data)


