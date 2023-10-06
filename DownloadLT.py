import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from senhas import loginlt, senhalt
from funcoes import set_tempo, loginlt, senhalt


browser = webdriver.Firefox()
browser.get("https://client.scriptcase.host/clientarea.php")
browser.maximize_window()

set_tempo(5)

browser.find_element(By.ID, "username").send_keys(loginlt)
browser.find_element(By.ID, "password").send_keys(senhalt)
browser.find_element(By.ID, "login").click()
sys.exit()
set_tempo(10)

browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/nav/ul/li[2]/a").click()

set_tempo(1)

browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/nav/ul/li[2]/ul/li[1]/a").click()

set_tempo(5)

browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/section/section/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/table/tbody/tr/td[1]/a").click()

set_tempo(5)

browser.find_element(By.ID, "cPanelBackup").click()

set_tempo(15)

#Obter ID da aba em foco
tabFocus = browser.current_window_handle

#Obter ID da primeira aba
oldTab = browser.window_handles[0]

#Obter ID da nova aba
newTab = browser.window_handles[1]

#Mudar o foco pra nova tab
browser.switch_to.window(oldTab)

#close browser parent window
browser.close()

browser.switch_to.window(newTab)

set_tempo(2)

browser.find_element(By.ID, "lnkHomeDirBackup").click()
set_tempo(1)
browser.find_element(By.ID, "databases_1").click()
set_tempo(1)
browser.find_element(By.ID, "databases_2").click()

print("Aguarde finalizar o download")



    









