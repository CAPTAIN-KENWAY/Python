from selenium import webdriver
from selenium.webdriver.chrome.service import Service


webdriver_path = "C:\Dell\Chrome Driver\chromedriver.exe"
s=Service(webdriver_path)
driver = webdriver.Chrome(service=s)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")
driver.find_element('name', 'fName').send_keys("Bishal")
driver.find_element('name', 'lName').send_keys("Baate")
driver.find_element('name', 'email').send_keys("bishalbaate@gmail.com")
driver.find_element('css selector', 'form button').click()

