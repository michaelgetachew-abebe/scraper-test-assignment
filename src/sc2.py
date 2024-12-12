import time
from selenium import webdriver as wd
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
 
options = Options()
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
 
driver = webdriver.Chrome(options=options)

target_url = 'https://www.walmart.com/blocked?url=L2lwL0Nsb3JveC1EaXNpbmZlY3RpbmctV2lwZXMtMjI1LUNvdW50LVZhbHVlLVBhY2stQ3Jpc3AtTGVtb24tYW5kLUZyZXNoLVNjZW50LTMtUGFjay03NS1Db3VudC1FYWNoLzE0ODk4MzY1&uuid=9ed7f800-f288-11eb-ad50-1b3c9c7d7310&vid=9cf07351-f288-11eb-9ab5-ef26d206453b&g=b'
driver.get(target_url)
driver.maximize_window()

driver.implicitly_wait(20)
print("Wait is complete")
element = driver.find_element(By.XPATH, '//*[@id="zgFSUubPzDBSvIb"]')
action = ActionChains(driver)
action.click_and_hold(element)
action.perform()
time.sleep(10)
action.release(element)
action.perform()
time.sleep(0.2)
action.release(element)