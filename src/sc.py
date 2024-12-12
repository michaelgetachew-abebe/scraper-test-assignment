from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import undetected_chromedriver as webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--use_subprocess")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--ignore-ssl-errors=yes")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-urlfetcher-cert-requests')
chrome_options.accept_insecure_certs = True

driver = webdriver.Chrome(options=chrome_options)

n_links = []

driver = webdriver.Chrome(options=chrome_options)
url = "https://www.walmart.com/"
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='Departments']/div/div/ul")))

search = driver.find_element_by_xpath("//*[@id='Departments']/div/div/ul").text
driver.find_element_by_xpath("//*[@id='Departments']/div/div/button/span").click()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='Departments']/div/div/div/div")))

search2 = driver.find_element_by_xpath("//*[@id='Departments']/div/div/div/div").text

sep = search.split('\n')
sep2 = search2.split('\n')

lngth = len(sep)
lngth2 = len(sep2)

for i in range(1, lngth):
    path = "//*[@id='Departments']/div/div/ul/li[" + str(i) + "]/a"
    nav_links = driver.find_element_by_xpath(path).get_attribute('href')
    n_links.append(nav_links)

for i in range(1, lngth2):
    path = "//*[@id='Departments']/div/div/div/div/ul/li[" + str(i) + "]/a"
    nav_links2 = driver.find_element_by_xpath(path).get_attribute('href')
    n_links.append(nav_links2)

print(n_links)
print(len(n_links))

driver.quit()