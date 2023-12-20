from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


s = Service("C:/Users/ABUTHALIB/Desktop/WebScraping/chrome-win64/chrome-win64/chromedriver.exe")
chrome_options = Options()
s.binary_location="C:/Users/ABUTHALIB/Desktop/WebScraping/chrome-win64/chrome-win64/chrome.exe"

driver = webdriver.Chrome(service=s,options=chrome_options)

driver.get("https://www.instagram.com/")


user= driver.find_element("xpath","""//*[@id="loginForm"]/div/div[1]/div/label/input""")
user.send_keys("testscrap7")
passw = driver.find_element("xpath","""//*[@id="loginForm"]/div/div[2]/div/label/input""")
passw.send_keys("test@123")
passw.send_keys(Keys.ENTER)

element = WebDriverWait(driver,10).until(ec.presence_of_element_located(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/button"""))



time.sleep(600)