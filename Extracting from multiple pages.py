import requests
from bs4 import BeautifulSoup
import pandas as pd

Names = []
Prices = []
description = []
Reviews = []
for i in range(1, 3):
    url = "https://webscraper.io/test-sites/e-commerce/static/phones/touch?page=" + str(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    box = soup.find("div", class_ := "col-lg-9")
    names = box.find_all("a", class_ := "title")
    for i in names:
        n = i.text
        Names.append(n)
    # print(Names)

    price = box.find_all("h4", class_ := "float-end price card-title pull-right")
    for i in price:
        p = i.text
        Prices.append(p)
    # print(Prices)

    desc = box.find_all("p", class_ := "description card-text")
    for i in desc:
        d = i.text
        description.append(d)
    # print(description)

    review = box.find_all("p", class_ := "float-end review-count")
    for i in review:
        r = i.text
        Reviews.append(r)
    # print(Reviews)

df = pd.DataFrame(
    {"Product Name": Names, "Product Price": Prices, "Product Description": description, "Product Review": Reviews})
print(df)
