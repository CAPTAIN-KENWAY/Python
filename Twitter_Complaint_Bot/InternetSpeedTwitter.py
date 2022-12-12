from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "C:\Dell\Chrome Driver\chromedriver.exe"
TWITTER_USERNAME = 'EdwardK74384674'
TWITTER_EMAIL = 'guptakaran094@gmail.com'
TWITTER_PASSWORD = 'kenway8899'



class InternetSpeedTwitterBot:
    def __init__(self):
        s = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=s)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net/')
        time.sleep(3)
        self.driver.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]').click()
        self.driver.find_element(
            'xpath',
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(60)
        try:
            self.down = self.driver.find_element(
                'xpath',
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
            ).text
            self.up = self.driver.find_element(
                'xpath',
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
            ).text
        except NoSuchElementException:
            time.sleep(10)
            self.down = self.driver.find_element(
                'xpath',
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
            ).text
            self.up = self.driver.find_element(
                'xpath',
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
            ).text

    def tweet_at_provider(self, msg):
        self.driver.get(url="https://www.twitter.com")
        time.sleep(5)
        self.driver.find_element(
            'xpath',
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span'
        ).click()
        time.sleep(5)
        self.driver.find_element(
            'xpath',
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
        ).send_keys(TWITTER_EMAIL)
        self.driver.find_element(
            'xpath',
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]'
        ).click()
        time.sleep(2)
        self.driver.find_element(
            'xpath',
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        ).send_keys(TWITTER_USERNAME)
        time.sleep(1)
        self.driver.find_element(
            'xpath',
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span'
        ).click()
        time.sleep(2)
        self.driver.find_element(
            'xpath',
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        ).send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        self.driver.find_element(
            'xpath',
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span'
        ).click()
        time.sleep(10)
        self.driver.find_element(
            'xpath',
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
        ).click()
        time.sleep(1)
        self.driver.find_element(
            'xpath',
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        ).send_keys(msg)
        self.driver.find_element(
            'xpath',
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'
        ).click()        
        time.sleep(3)
        self.driver.quit()
