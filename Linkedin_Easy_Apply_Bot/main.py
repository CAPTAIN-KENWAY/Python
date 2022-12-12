from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

def scroll_to_last():
    last_scroll_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(5)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_scroll_height:
            break
        last_scroll_height = new_height

webdriver_path = "C:\Dell\Chrome Driver\chromedriver.exe"
s = Service(webdriver_path)
driver = webdriver.Chrome(service=s)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3279725514&f_LF=f_AL&geoId=115884833&keywords=python%20developer&location=Gurugram%2C%20Haryana%2C%20India&refresh=true")
driver.find_element('xpath', '/html/body/div[1]/header/nav/div/a[2]').click()
time.sleep(3)
driver.find_element('xpath', '//*[@id="username"]').send_keys('guptakaran094@gmail.com')
driver.find_element('xpath', '//*[@id="password"]').send_keys('kenway8899')
driver.find_element('xpath', '//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(5)
jobs = driver.find_elements('class name','job-card-list__title')
for job in jobs:
    driver.find_element('link text', job.text).click()
    scroll_to_last()
    time.sleep(2)
    try:
        driver.find_element('class name','follow').click()
    except NoSuchElementException:
        continue
time.sleep(5)
driver.quit()