from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

CHROME_DRIVER_PATH = "C:\Dell\Chrome Driver\chromedriver.exe"
INSTAGRAM_USERNAME = 'wei_shen_69_'
INSTAGRAM_PASSWORD = 'kenway8899'


class InstaFollower:
    def __init__(self):
        s = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get(url='https://www.instagram.com')
        time.sleep(3)
        self.driver.find_element(
            'xpath',
            '//*[@id="loginForm"]/div/div[1]/div/label/input'
        ).send_keys(INSTAGRAM_USERNAME)
        self.driver.find_element(
            'xpath',
            '//*[@id="loginForm"]/div/div[2]/div/label/input'
        ).send_keys(INSTAGRAM_PASSWORD)
        self.driver.find_element(
            'xpath',
            '//*[@id="loginForm"]/div/div[3]/button'
        ).click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(url='https://www.instagram.com/chefsteps')
        time.sleep(5)
        self.driver.find_element(
            'xpath',
            '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a'
        ).click()

    def scroll_to_last(self):
        fBody = self.driver.find_element(
            'xpath',
            '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
        )
        scroll = 0
        while scroll < 3: 
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(3)
            scroll += 1

    def follow(self):
        time.sleep(5)
        self.scroll_to_last()
        for i in range(1, 30):
            self.driver.find_element(
                'xpath',
                f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div[3]/button'
            ).click()
            time.sleep(2)
        self.driver.quit()

