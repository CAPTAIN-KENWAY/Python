from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

webdriver_path = "C:\Dell\Chrome Driver\chromedriver.exe"
s = Service(webdriver_path)
driver = webdriver.Chrome(service=s)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
timeout = time.time() + 5
five_min = time.time() + 300
store = driver.find_elements('css selector', '#store div')

items = ['buy' + store[i].text.split(' - ')[0] for i in range(len(store)-1)]

while True:
    driver.find_element('id', 'cookie').click()

    money = int(driver.find_element('id', 'money').text.replace(',', ''))
    if time.time() > timeout:
        all_prices = driver.find_elements('css selector', '#store b')
        prices = [int(all_prices[i].text.split(' - ')[1].replace(',', ''))
                  for i in range(len(store) - 1)]
        affordable = {}
        for i in range(0, len(items)):
            if money >= prices[i]:
                affordable[prices[i]] = items[i]
        buy = max(affordable)
        driver.find_element('id', f'{affordable[buy]}').click()
        timeout = time.time() + 5
    if time.time() > five_min:
        print(driver.find_element('id', 'cps').text)
        break

driver.quit()
