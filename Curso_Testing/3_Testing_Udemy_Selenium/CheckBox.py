from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="S:\\_Django_ft_Testing\\Curso_Testing\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")

checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for cheque in checkbox:
    if  cheque.is_displayed() == True and cheque.is_selected() == False:
        time.sleep(3)
        cheque.click()
        time.sleep(1)
