# --- Método Manual ---
# Requiere que hayas descargado chromedriver.exe manualmente
# y especifiques su ruta.

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    import os # Importa el módulo os para manejar rutas

    print("--- Probando Método Manual ---")

    # Epecifica la ruta completa del driver:
    driver_path_manual = 'S:\\_Django_ft_Testing\\Curso_Testing\\Drivers\\chromedriver.exe' 

    # Verifica si el archivo del driver existe en la ruta especificada
    if not os.path.exists(driver_path_manual):
        print(f"Error: No se encontró el archivo del driver en la ruta especificada: {driver_path_manual}")
    else:
        service_manual = Service(driver_path_manual)

        # Intenta iniciar el driver
        try:
            driver_manual = webdriver.Chrome(service=service_manual)
            print("WebDriver Chrome iniciado con éxito (Manual).")
            driver_manual.maximize_window()
            driver_manual.get("https://www.udemy.com/join/passwordless-auth/?locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html&action=login&mode") # Reemplaza con la URL que quieras probar

            # Espera un poco para ver la página (opcional, para depuración)
            import time
            time.sleep(5)

            print(f"Título de la página (Manual): {driver_manual.title}")

            # Cierra el navegador
            driver_manual.quit()
            print("Navegador cerrado (Manual).")

        except Exception as e:
            print(f"Ocurrió un error al iniciar o usar el driver manual: {e}")
            print("Verifica que la versión de tu Chrome coincide con la versión de chromedriver.exe.")
            print("Asegúrate de que chromedriver.exe no está corrupto (re-descárgalo si es necesario).")


except ModuleNotFoundError:
    print("Error: No se encontró el módulo 'selenium'.")
    print("Asegúrate de haber instalado 'selenium' con 'pip install selenium'.")
except Exception as e:
    print(f"Ocurrió un error general durante la ejecución del método manual: {e}")