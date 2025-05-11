import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class usando_unittest(unittest.TestCase):
    def setUp (self):
        self.service = Service(executable_path=r"S:\_Django_ft_Testing\Curso_Testing\Drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        # Nos aseguramos de no tener una espera implícita para este test de espera explícita
        self.driver.get("https://www.w3schools.com/howto/howto_css_button_group.asp") # URL del escenario de Implicit Wait
        self.driver.maximize_window()
    
    def test_usando_Explicit_wait (self):
        driver = self.driver
        
        # Localizador para el botón "Apple"
        apple_button_locator = (By.XPATH, "//button[text()='Apple']")
        
        print(f"Esperando que el botón Apple ({apple_button_locator}) sea visible...")
        try:
            # Esperar explícitamente hasta 10 segundos para que el botón sea visible
            apple_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(apple_button_locator)
            )
            
            # Si el elemento se encuentra y es visible, la espera explícita tiene éxito
            self.assertTrue(apple_button.is_displayed(), "El botón Apple no está visible después de la espera.")
            print("Botón 'Apple' encontrado y visible.")
            
            # Opcional: realizar alguna acción con el botón
            # apple_button.click()
            # print("Botón 'Apple' clickeado.")

        except TimeoutException:
            self.fail(f"Timeout esperando el botón Apple ({apple_button_locator}). El elemento no se hizo visible a tiempo.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
