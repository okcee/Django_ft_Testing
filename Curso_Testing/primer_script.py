# Asegúrate de que este archivo NO se llama webdriver_manager.py
# Puedes llamarlo, por ejemplo, test_selenium.py

# --- Método Automático (Recomendado) ---
# Requiere que hayas instalado: pip install selenium webdriver-manager
# Requiere que hayas instalado: pip install selenium

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    print("--- Iniciando webdriver_manager ---")

    # webdriver_manager se encarga de descargar y gestionar el driver
    # Esto descarga el driver compatible con tu versión de Chrome
    service_auto = Service(ChromeDriverManager().install())
    driver_auto = webdriver.Chrome(service=service_auto)

    print("WebDriver Chrome iniciado con éxito (Automático).")
    driver_auto.get("https://www.udemy.com/join/passwordless-auth/?locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html&action=login&mode") # Reemplaza con la URL que quieras probar

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

