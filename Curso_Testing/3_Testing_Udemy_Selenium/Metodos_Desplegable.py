# Dropdown, menú desplegable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import unittest

class menu_desplegable(unittest.TestCase):
    def setUp(self):
        self.service = Service(executable_path="S:\\_Django_ft_Testing\\Curso_Testing\\Drivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def test_recorrer(self):
        self.driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")

        menu = Select(self.driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/select"))
        time.sleep(3)

        menu.select_by_index(11)
        time.sleep(5)

        menu.select_by_value("6")
        time.sleep(5)

        menu.select_by_visible_text("Ford")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
