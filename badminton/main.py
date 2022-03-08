#encoding=utf-8

import time
from selenium import webdriver
from PIL import Image
import ddddocr
 
browser = webdriver.Chrome()
# 预约羽毛球
browser.get("https://gym.sysu.edu.cn/product/show.html?id=35")
browser.maximize_window()
order_button = browser.find_elements_by_xpath('//div[@class="boxes"]/a')[0]
order_button.click()
time.sleep(0.5)
next_day_button = browser.find_elements_by_xpath('//div[@class="dates-viewport"]/ul[@class="stock-date date-week dates-list"]/li')[1]
next_day_button.click()
time.sleep(0.5)
# get time slot
time_slot = browser.find_elements_by_xpath('//ul[@class="cell-ul cell-vanue-sm"]/li/span')[110] # 8:00 - 9:00  number 6
time_slot.click()
browser.find_element_by_xpath('//button[@class="normal-button-mid button-danger"]').click()
time.sleep(0.5)
# 10次机会识别验证码
for i in range(10):
  username = browser.find_element_by_id("username")
  username.send_keys('username')
  pwd = browser.find_element_by_id("password")
  pwd.send_keys('password')
  browser.save_screenshot('screenshot.png')
  im = Image.open('screenshot.png')
  rangle = (1155, 850, 1333, 907) # position of code image
  code = im.crop(rangle)
  code.save('code.png')
  with open('code.png', 'rb') as f:
    img_bytes = f.read()
  ocr = ddddocr.DdddOcr()
  res = ocr.classification(img_bytes)
  captcha = browser.find_element_by_id("captcha")
  captcha.send_keys(res)
  browser.find_element_by_xpath('//input[@class="btn btn-submit btn-block"]').click()
  time.sleep(0.5)
  try:username = browser.find_element_by_id("username")
  except:break

order_button = browser.find_elements_by_xpath('//div[@class="boxes"]/a')[0]
order_button.click()
next_day_button = browser.find_elements_by_xpath('//div[@class="dates-viewport"]/ul[@class="stock-date date-week dates-list"]/li')[1]
next_day_button.click()
time.sleep(0.5)
# get time slot
time_slot = browser.find_elements_by_xpath('//ul[@class="cell-ul cell-vanue-sm"]/li/span')[110] # 8:00 - 9:00  number 6
time_slot = browser.find_elements_by_xpath('//ul[@class="cell-ul cell-vanue-sm"]/li/span')[0]
time_slot.click()
browser.find_element_by_xpath('//button[@class="normal-button-mid button-danger"]').click()
time.sleep(0.5)
browser.find_element_by_id("reserve").click()
time.sleep(0.5)
#browser.find_elements_by_xpath('//div[@class="sa-button-container"]/button[@class="confirm"]').click()
browser.find_element_by_xpath('//div[@class="sa-button-container"]/button[@class="cancel"]').click()
print('预定中')
