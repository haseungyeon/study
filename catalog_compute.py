from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/user/OneDrive/바탕 화면/파이썬 연습장/chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://tdevauth.l-cloud.co.kr/sso/auth/login')

driver.find_element_by_id('username').send_keys('bdlee112@ldcc.kr')
driver.find_element_by_id('password').send_keys('test123')
driver.find_element_by_xpath('/html/body/main/section/div/form[1]/div[2]/label[2]/input').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/main/section/div/form[1]/div[1]/button').click()

