import sys
import time
import senhas
from selenium import webdriver
from senhas import loginlt, senhalt
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

options.add_experimental_option('detach', True)

options.add_experimental_option("excludeSwitches", ["enable-logging"])

s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s, options=options)

driver.get('https://client.scriptcase.host/clientarea.php')

driver.maximize_window()

timeout = 5

try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")


driver.find_element("xpath", '/html/body/div[2]/div[1]/section/section/form/div/div/div/div[2]/div[3]/div[1]/div[1]/input').send_keys(loginlt)

driver.find_element("xpath", '/html/body/div[2]/div[1]/section/section/form/div/div/div/div[2]/div[3]/div[1]/div[2]/input').send_keys(senhalt)

driver.find_element("xpath", '/html/body/div[2]/div[1]/section/section/form/div/div/div/div[3]/input').click()

driver.find_element("xpath", '/html/body/div[2]/div[1]/nav/ul/li[2]/a').click()

driver.find_element("xpath", '/html/body/div[2]/div[1]/nav/ul/li[2]/ul/li[1]/a').click()

driver.find_element("xpath", '/html/body/div[2]/div[1]/section/section/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/table/tbody/tr/td[1]/a').click()

# Click the link which opens in a new window
driver.find_element(By.LINK_TEXT, "Backup/Cópia de Segurança").click()

#obtain window handle of browser in focus
p = driver.current_window_handle

#obtain parent window handle
parent = driver.window_handles[0]

#obtain browser tab window
chld = driver.window_handles[1]

#switch to browser tab
driver.switch_to.window(chld)

#switch to parent window
driver.switch_to.window(parent)

#close browser parent window
driver.close()

driver.switch_to.window(chld)

time.sleep(5)

driver.find_element("xpath", '/html/body/div[6]/div[2]/div/div/div/div[3]/div[1]/div[1]/a').click()

driver.find_element("xpath", '/html/body/div[6]/div[2]/div/div/div/div[3]/div[2]/div[1]/table/tbody/tr[1]/td/a').click()

driver.find_element("xpath", '/html/body/div[6]/div[2]/div/div/div/div[3]/div[2]/div[1]/table/tbody/tr[2]/td/a').click()

time.sleep(5)

print('Finished')

sys.exit()
