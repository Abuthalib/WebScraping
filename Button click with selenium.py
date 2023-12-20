from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

s = Service("C:/Users/ABUTHALIB/Desktop/WebScraping/chrome-win64/chrome-win64/chromedriver.exe")
chrome_options = Options()
chrome_options.binary_location = "C:/Users/ABUTHALIB/Desktop/WebScraping/chrome-win64/chrome-win64/chrome.exe"

driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://www.wscubetech.com/")
l = driver.find_element("xpath", """/html/body/section[1]/div/div/div[1]/div/div/button""")
l.click()
print("Page title is:")
print(driver.title)
time.sleep(60)
