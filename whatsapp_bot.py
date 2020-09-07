from selenium import webdriver 
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

message = input(" Enter message : ")
num = int(input("Enter num for repeate : "))
content = input("Enter your content : ")
contents = content.split(",")
input("Run!")

for name in contents:
    user = driver.find_element_by_xpath(f'//span[@title="{name}"]')
    user.click()
    msg=driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for j in range(num):
        msg[0].send_keys(message)
        send_btn = driver.find_elements_by_class_name('_1U1xa')
        send_btn[0].click()

#------------
#for debug 
# print(type(msg))
# print(msg)
# print(len(msg)