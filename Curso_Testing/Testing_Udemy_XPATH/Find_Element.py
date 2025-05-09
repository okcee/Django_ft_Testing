from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="S:\\_Django_ft_Testing\\Curso_Testing\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F")
driver.maximize_window()
time.sleep(5)

correo = driver.find_element(By, "form-control")
clave = driver.find_element(By.CLASS_NAME, "textInput")
time.sleep(5)

correo = driver.find_element(By.CLASS_NAME, "form-control") # Asumo que querías buscar por CLASS_NAME aquí
time.sleep(5)
clave.send_keys("12345678910")
time.sleep(5)

boton = driver.find_element(By.CLASS_NAME, "btn-primary")
boton.click()
time.sleep(5)

driver.quit()