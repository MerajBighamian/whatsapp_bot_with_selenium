from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'D:\selenium\selenium-app\chromedriver.exe')
driver.get('https://toplearn.com')
se = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/input')
time.sleep(2
)
se.clear()
se.send_keys('selenium' + Keys.ENTER )
time.sleep(4)
driver.find_element_by_xpath('//*[@id="filter-search"]/div[2]/div/div[2]/div/div/div/h2/a').click()

# driver.find_element_by_name('q').send_keys('تاپ لرن') 
# driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').send_ke ys(Keys.ENTER)
# driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,700)')

# time.sleep(2)
# driver.execute_script('window.scrollTo(700,1400)')

