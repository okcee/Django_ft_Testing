from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Creamos el objeto Service
ruta_driver = "S:\\_Django_ft_Testing\\Curso_Testing\\Drivers\\chromedriver.exe"
s = Service(ruta_driver)
controlador = webdriver.Chrome(service=s) # Usamos el objeto Service

controlador.maximize_window() # Maximizamos la ventana
controlador.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

# Intentar aceptar el banner de cookies si aparece
try:
    # Intenta encontrar el botón de "Rechazar todo"
    reject_button_locator = (By.ID, "onetrust-reject-all-handler")
    reject_button = WebDriverWait(controlador, 5).until(EC.element_to_be_clickable(reject_button_locator))
    reject_button.click()
    print("Banner de cookies rechazado (opción directa).")
except TimeoutException:
    print("Botón de 'Rechazar todo' directo no encontrado.")
    # Aquí podrías intentar la opción de "Configurar" cookies

usuario = controlador.find_element(By.NAME, "email")

usuario.send_keys("dfdflujogramas@gmail.com")
time.sleep(0.5)

try:
    wait = WebDriverWait(controlador, 20) # Aumentamos el tiempo de espera a 20 segundos
    # Usamos un selector un poco más específico, combinando type y data-purpose
    boton_locator = (By.CSS_SELECTOR, "button[type='submit'][class*='passwordless-auth-mx-code-generation-form--submit-button']")
    boton = wait.until(EC.element_to_be_clickable(boton_locator))
    boton.click()
    print("Botón de 'Continuar' clickeado.")
    print(f"URL actual después del clic: {controlador.current_url}")
    try:
        wait_siguiente_pagina = WebDriverWait(controlador, 15) # Esperar hasta 15 segundos
        # Esperamos el encabezado que suele aparecer en la pantalla de OTP de Udemy
        otp_header_locator = (By.CSS_SELECTOR, "h2[data-purpose='otp-header']")
        elemento_siguiente = wait_siguiente_pagina.until(EC.presence_of_element_located(otp_header_locator))
        print("Elemento de la siguiente página encontrado. ¡Parece que cargó!")
        # Aquí podrías interactuar con 'elemento_siguiente'
        time.sleep(5) # Pausa para observar
    except TimeoutException:
        print("Timeout: No se encontró el elemento esperado de la siguiente página/estado.")
        controlador.save_screenshot("s:\\_Django_ft_Testing\\Curso_Testing\\despues_del_clic_name_py.png")
        print("Captura de pantalla guardada en 's:\\_Django_ft_Testing\\Curso_Testing\\despues_del_clic_name_py.png'")
    
except TimeoutException:
    print("Timeout: El botón de 'Continuar' no se volvió clickeable a tiempo.")
    controlador.save_screenshot("s:\\_Django_ft_Testing\\Curso_Testing\\error_screenshot_name_py.png")
    print("Captura de pantalla guardada en 's:\\_Django_ft_Testing\\Curso_Testing\\error_screenshot_name_py.png'")
    raise # Volvemos a lanzar la excepción para que el script falle como antes si es necesario

controlador.quit()