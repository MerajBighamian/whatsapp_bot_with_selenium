from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'D:\selenium\selenium-app\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
driver.add_cookie({"name": "tok", "value": "1@PxNTCujRpsJtSAGxUPRwfqiJ19LisD6iiomeJUlCixAHOXiqIkYjLDQ+kL/kdmmL5suGLC2OfOFIYw=="})
driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[13]/div/div/div[2]/div[1]/div[1]/span/span').click()