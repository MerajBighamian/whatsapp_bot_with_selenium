from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome(r'D:\selenium\selenium-app\chromedriver.exe')
driver.get('https://instagram.com/')
driver.find_element_by_xpath('//input[@name="username"]').send_keys('merajbighamian')