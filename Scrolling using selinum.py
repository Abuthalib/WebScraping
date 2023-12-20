from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/ABUTHALIB/Desktop/WebScraping/chrome-win64/chrome-win64/chromedriver.exe")
chrome_options = Options()
s.binary_location="C:/Users/ABUTHALIB/Desktop/WebScraping/chrome-win64/chrome-win64/chrome.exe"

driver = webdriver.Chrome(service=s,options=chrome_options)

driver.get("https://www.google.com/")
user = driver.find_element("xpath","""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
user.send_keys("Messi")
user.send_keys(Keys.ENTER)
while True:
    height = driver.execute_script("return document.body.scrollHeight")
print(height)

time.sleep(1)