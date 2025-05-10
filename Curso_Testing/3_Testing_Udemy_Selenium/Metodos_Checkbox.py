from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="S:\\_Django_ft_Testing\\Curso_Testing\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")

checkbox = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[2]")

print(checkbox.is_selected())
print(checkbox.is_enabled())
print(checkbox.is_displayed())
time.sleep(5)

driver.quit()