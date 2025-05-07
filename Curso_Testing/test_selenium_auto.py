# Asegúrate de que este archivo NO se llama webdriver_manager.py
# Puedes llamarlo, por ejemplo, test_selenium.py

# --- Método Automático (Recomendado) ---
# Requiere que hayas instalado: pip install selenium webdriver-manager
# Requiere que hayas instalado: pip install selenium

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    print("--- Probando Método Automático (webdriver_manager) ---")

    # webdriver_manager se encarga de descargar y gestionar el driver
    # Esto descarga el driver compatible con tu versión de Chrome
    service_auto = Service(ChromeDriverManager().install())
    driver_auto = webdriver.Chrome(service=service_auto)
    driver_auto.maximize_window()

    print("WebDriver Chrome iniciado con éxito (Automático).")
    driver_auto.get("https://www.ejemplo.com") # Reemplaza con la URL que quieras probar

    # Espera un poco para ver la página (opcional, para depuración)
    import time
    time.sleep(5)

    print(f"Título de la página (Automático): {driver_auto.title}")

    # Cierra el navegador
    driver_auto.quit()
    print("Navegador cerrado (Automático).")

except ModuleNotFoundError:
    print("Error: No se encontró el módulo 'webdriver_manager'.")
    print("Asegúrate de haber instalado 'webdriver-manager' con 'pip install webdriver-manager'.")
    print("También verifica que no tienes un archivo llamado 'webdriver_manager.py' en tu directorio.")
except Exception as e:
    print(f"Ocurrió un error durante la ejecución del método automático: {e}")

print("\n" + "="*50 + "\n") # Separador

# # --- Método Manual ---
# # Requiere que hayas descargado chromedriver.exe manualmente
# # y especifiques su ruta.

# try:
#     from selenium import webdriver
#     from selenium.webdriver.chrome.service import Service
#     import os # Importa el módulo os para manejar rutas

#     print("--- Probando Método Manual ---")

#     # *** IMPORTANTE: Reemplaza esta ruta con la ruta REAL a tu chromedriver.exe ***
#     # Puedes usar os.path.join si el driver está en el mismo directorio que el script
#     # driver_path_manual = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')
#     # O especifica la ruta completa:
#     driver_path_manual = 'C:\\ruta\\completa\\a\\tu\\carpeta\\chromedriver.exe' # Ejemplo Windows
#     # driver_path_manual = '/ruta/completa/a/tu/carpeta/chromedriver' # Ejemplo Linux/macOS

#     # Verifica si el archivo del driver existe en la ruta especificada
#     if not os.path.exists(driver_path_manual):
#         print(f"Error: No se encontró el archivo del driver en la ruta especificada: {driver_path_manual}")
#     else:
#         service_manual = Service(driver_path_manual)

#         # Intenta iniciar el driver
#         try:
#             driver_manual = webdriver.Chrome(service=service_manual)
#             print("WebDriver Chrome iniciado con éxito (Manual).")
#             driver_manual.get("https://www.ejemplo.com") # Reemplaza con la URL que quieras probar

#             # Espera un poco para ver la página (opcional, para depuración)
#             # import time
#             # time.sleep(5)

#             print(f"Título de la página (Manual): {driver_manual.title}")

#             # Cierra el navegador
#             driver_manual.quit()
#             print("Navegador cerrado (Manual).")

#         except Exception as e:
#             print(f"Ocurrió un error al iniciar o usar el driver manual: {e}")
#             print("Verifica que la versión de tu Chrome coincide con la versión de chromedriver.exe.")
#             print("Asegúrate de que chromedriver.exe no está corrupto (re-descárgalo si es necesario).")


# except ModuleNotFoundError:
#     print("Error: No se encontró el módulo 'selenium'.")
#     print("Asegúrate de haber instalado 'selenium' con 'pip install selenium'.")
# except Exception as e:
#     print(f"Ocurrió un error general durante la ejecución del método manual: {e}")
