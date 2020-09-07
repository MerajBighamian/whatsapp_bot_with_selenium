from selenium import webdriver
import time

driver = webdriver.Chrome(r'D:\selenium\selenium-app\chromedriver.exe')

driver.get('https://onlineplus.mofidonline.com/Account/Login')
driver.find_element_by_name('username').send_keys('mfdonline2366818')
driver.find_element_by_name('password').send_keys('merajbighamian@09373951511//2581382')
driver.find_element_by_xpath('').send_keys()