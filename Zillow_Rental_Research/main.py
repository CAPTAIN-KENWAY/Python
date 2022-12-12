import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ZILLOW_URL = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.975290796040426%2C%22east%22%3A-122.25136844042969%2C%22south%22%3A37.57475060679124%2C%22west%22%3A-122.61529055957031%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D'
GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSfqJcTnEi6a691GyxcL_g8EzkthxpHoGGbdv5RVcJduIWKvLQ/viewform?usp=sf_link'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en,en-GB;q=0.9"
}
response = requests.get(ZILLOW_URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.findAll('script', attrs={'type': 'application/json'})
rent_data = data[1].text
rent_data = rent_data.replace('<!--', '')
rent_data = rent_data.replace('-->', '')
rent_data = json.loads(rent_data)
rent_data = rent_data['cat1']['searchResults']['listResults']
links = [link['detailUrl'] for link in rent_data]
for i in range(len(links)):
    if 'http' not in links[i]:
        links[i] = 'https://www.zillow.com' + links[i]

addresses = [address['address'] for address in rent_data]
prices = []
for price in rent_data:
    try:
        prices.append(price['price'].split('/')[0].strip('+'))
    except KeyError:
        prices.append(price['units'][0]['price'].strip('+'))

CHROME_DRIVER_PATH = "C:\Dell\Chrome Driver\chromedriver.exe"
s = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=s)
for i in range(len(links)):
    driver.get(url=GOOGLE_FORM_URL)
    time.sleep(2)
    driver.find_element(
        'xpath',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    ).send_keys(addresses[i])
    driver.find_element(
        'xpath',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    ).send_keys(prices[i])
    driver.find_element(
        'xpath',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    ).send_keys(links[i])
    driver.find_element(
        'xpath',
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
    ).click()
    time.sleep(3)
driver.quit()
