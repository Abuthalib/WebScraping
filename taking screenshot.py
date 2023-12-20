from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/ABUTHALIB/Desktop/WebScraping/chrome-win64/chrome-win64/chromedriver.exe")
chrome_options = Options()
s.binary_location="C:/Users/ABUTHALIB/Desktop/WebScraping/chrome-win64/chrome-win64/chrome.exe"

driver = webdriver.Chrome(service=s,options=chrome_options)

driver.get("https://www.instagram.com/")
#driver.save_screenshot("C:/Users/ABUTHALIB/Desktop/WebScraping/full_page.png")


time.sleep(60)
