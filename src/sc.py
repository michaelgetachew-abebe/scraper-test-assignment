from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
 
options = Options()
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
 
driver = webdriver.Chrome(options=options)
driver.get("https://www.walmart.com/")
 
human_dialog = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div[1]")
 
driver.implicitly_wait(15)
while human_dialog:
    driver.refresh()
    time.sleep(1)
    human_dialog = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div[1]")
 
departments = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/span/div/div/nav/ul/li[1]/section/div/div/a')
print(departments)