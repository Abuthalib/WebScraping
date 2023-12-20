import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

boxes = soup.find_all("div", class_ := "col-md-4 col-xl-4 col-lg-4")

box = soup.find_all("div", class_ := "col-md-4 col-xl-4 col-lg-4")[3]

name = box.find("a").text
print(name)

desc = box.find("p", class_ := "description card-text").text
print(desc)

#############


url1 = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

r = requests.get(url1)

soup = BeautifulSoup(r.text, "lxml")

navbar = soup.find_all("ul", class_ := "nav flex-column", id="side-menu")[0]
name = (soup.find("li", class_ := "nav-item  active "))
print(name)
