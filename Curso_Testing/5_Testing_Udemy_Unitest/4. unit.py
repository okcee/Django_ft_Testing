import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.service = Service(executable_path=r"S:\_Django_ft_Testing\Curso_Testing\Drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
    
    def test_usando_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        select_element = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/select")
        # Para obtener todas las opciones, usa find_elements (plural)
        lista_de_opciones = select_element.find_elements(By.TAG_NAME,"option")
        time.sleep(3)
        # Itera sobre la lista de WebElements de las opciones
        for una_opcion in lista_de_opciones:
            print("Value is: %s" % una_opcion.get_attribute("value"))
            una_opcion.click()
            time.sleep(1)
        seleccionar = Select(driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
