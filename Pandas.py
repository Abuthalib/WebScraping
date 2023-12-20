import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

names = soup.find_all("a", class_ := "title")
# print(names)

product_names = []
for i in names:
    name = i.text
    product_names.append(name)

#print(product_names)

prices = soup.find_all("h4", class_ := "float-end price card-title pull-right")
# print(prices)
product_price = []
for i in prices:
    price = i.text
    product_price.append(price)
#print(product_price)

description = soup.find_all("p", class_ := "description card-text")
# print(description)
product_description = []
for i in description:
    desc = i.text
    product_description.append(desc)
#print(product_description)

reviews = soup.find_all("p", class_ := "float-end review-count")

# print(reviews)
review_count = []
for i in reviews:
    rev = i.text
    review_count.append(rev)
#print(review_count)

##making data frame
df = pd.DataFrame({"ProductName": product_names, "price": product_price,
                   "Description": product_description, "review_count": review_count})

#df.to_csv("Product_details.csv")
