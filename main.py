import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)
# print(r.status_code)
# print(r.text)
soup = BeautifulSoup(r.text, "lxml")
# tag = soup.header
# atb= tag.attrs
# print(atb["role"])

tag = soup.header.div.a.button.span.string
print(tag)
