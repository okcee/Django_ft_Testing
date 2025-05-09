from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

s = Service("S:\\_Django_ft_Testing\\Curso_Testing\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.udemy.com/join/passwordless-auth/?locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fes%2F&response_type=html&action=login&mode") # Con el método get le damos la url a testear
time.sleep(1)

usuario = driver.find_element(By.ID, "form-group--1") # Inicia el testing con el elemento ID
# clave = driver.find_element(By.ID, "id_password")
time.sleep(1)

usuario.send_keys("dfdflujogramas@gmail.com")
time.sleep(5)

# clave.send_keys("12345678910")
# time.sleep(5)

boton = driver.find_element(By.ID, "submit-id-submit")
boton.click()
time.sleep(5)

driver.quit()