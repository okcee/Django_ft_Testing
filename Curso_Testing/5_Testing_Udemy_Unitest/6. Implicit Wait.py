import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service # Importar Service

class usando_unittest(unittest.TestCase):
    def setUp (self):
        self.service = Service(executable_path=r"S:\_Django_ft_Testing\Curso_Testing\Drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.w3schools.com/howto/howto_css_button_group.asp")
        self.driver.maximize_window()
    
    def test_usando_implicit_wait(self):
        # Buscamos un botón con el texto "Apple" usando XPath.
        apple_button = self.driver.find_element(By.XPATH, "//button[text()='Apple']")
        # Puedes añadir una aserción si quieres verificar algo sobre el botón
        self.assertTrue(apple_button.is_displayed(), "El botón Apple no está visible.")
        print("Botón 'Apple' encontrado.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()