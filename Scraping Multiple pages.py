import requests
from bs4 import BeautifulSoup

for i in range(0,2):
    print(i)

    url = "https://webscraper.io/test-sites/e-commerce/static/phones/touch?page="+str(i+1)
    r = requests.get(url)
    print(r)

    soup = BeautifulSoup(r.text,"lxml")

    np = soup.find("a",class_ :="page-link").get("href")
    cnp = "https://webscraper.io"+np
    print(cnp)

    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text,"lxml")
