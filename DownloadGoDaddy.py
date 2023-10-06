import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

options.add_experimental_option('detach', True)

options.add_experimental_option("excludeSwitches", ["enable-logging"])

options.add_argument("javascript.enabled")

s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s, options=options)

driver.get('https://sso.godaddy.com/?realm=idp&app=dashboard.api&path=%2fvh-login-redirect&marketid=pt-BR')

driver.maximize_window()   

time.sleep(10)

driver.find_element(By.ID, "username").click()

driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div/div/div/div[3]/div[3]/div[1]/div/div/input').send_keys("ti@vancouros.com.br")


