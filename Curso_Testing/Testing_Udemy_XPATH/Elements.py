from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("S:\\_Django_ft_Testing\\Curso_Testing\\Drivers\\chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
driver.maximize_window()

varios = driver.find_element(By.CLASS_NAME, "form-control")
for i in varios:
    time.sleep(1)
    i.send_keys("123456789")