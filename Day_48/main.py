from selenium import webdriver
from selenium.webdriver.chrome.service import Service


webdriver_path = "C:\Dell\Chrome Driver\chromedriver.exe"
s=Service(webdriver_path)
driver = webdriver.Chrome(service=s)
driver.get(url="https://www.python.org")
events = {}
for i in range(1,6):
    event = driver.find_element('xpath', f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
    date = driver.find_element('xpath', f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
    events[i-1] = {'time': date.text.split('T')[0],
                 'name': event.text}
print(events)
driver.quit()
