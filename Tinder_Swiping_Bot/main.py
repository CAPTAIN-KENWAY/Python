from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

webdriver_path = "C:\Dell\Chrome Driver\chromedriver.exe"
s = Service(webdriver_path)
driver = webdriver.Chrome(service=s)
driver.get(url="https://www.tinder.com")
time.sleep(5)
driver.find_element(
    'xpath', 
    '//*[@id="q-1470728188"]/div/div[2]/div/div/div[1]/div[1]/button').click()
driver.find_element(
    'xpath', 
    '//*[@id="q-1470728188"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]').click()
time.sleep(1)
try:
    driver.find_element(
        'xpath', 
        '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button').click()
except NoSuchElementException:
    driver.find_element(
        'xpath', 
        '//*[@id="q1095858032"]/main/div/div[1]/div/div/div[3]/span/button').click()
    time.sleep(1)
    driver.find_element(
        'xpath', 
        '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button').click()
time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
driver.find_element('xpath', '//*[@id="email"]').send_keys('guptakaran094@gmail.com')
driver.find_element('xpath', '//*[@id="pass"]').send_keys('kenway8899')
driver.find_element('xpath', '//*[@id="loginbutton"]').click()
time.sleep(15)
driver.switch_to.window(base_window)
driver.find_element('xpath', '//*[@id="q1095858032"]/main/div/div/div/div[3]/button[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[@id="q1095858032"]/main/div/div/div/div[3]/button[2]').click()
time.sleep(10)
for i in range(5):
    try:
        driver.find_element('css selector','body').send_keys(Keys.RIGHT)
        time.sleep(2)
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element('css selector','.itsAMatch a')
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
    
driver.quit()
