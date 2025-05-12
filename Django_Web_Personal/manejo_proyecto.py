'''
Script para seguir usando la terminal desde el directorio raíz para el manejo de comandos de manage.py

En vez de tener que abrir una terminal desde el directorio donte se aloja manage.py y escribir:
python manage.py *comando

O escribir el comando con el directorio entero
python "S:\_Django_ft_Testing\Django_Web_Personal\webpersonal\manage.py" *comando

Escribiremos:
python manejo_proyecto.py *comando
Por ejemplo:    python manejo_proyecto.py runserver
De esta manera, ya se encarga el script de enlazar con el directorio de manage.py
'''


import os
import sys
import subprocess

DJANGO_PROJECT_DIR = r"S:\_Django_ft_Testing\Django_Web_Personal\webpersonal"
MANAGE_PY_SCRIPT_NAME = "manage.py" # Nombre del script de Django

def run_django_command(command_args):
    """
    Ejecuta un comando de gestión de Django.
    command_args: una lista de argumentos para manage.py (ej: ["migrate"] o ["runserver", "0.0.0.0:8001"])
    """
    manage_py_path = os.path.join(DJANGO_PROJECT_DIR, MANAGE_PY_SCRIPT_NAME)

    # Verificar que el directorio del proyecto y manage.py existen
    if not os.path.isdir(DJANGO_PROJECT_DIR):
        print(f"Error: El directorio del proyecto Django '{DJANGO_PROJECT_DIR}' no existe.")
        return

    if not os.path.isfile(manage_py_path):
        print(f"Error: El script '{MANAGE_PY_SCRIPT_NAME}' no se encontró en '{DJANGO_PROJECT_DIR}'.")
        print("Asegúrate de que la ruta es correcta.")
        return

    full_command = [sys.executable, MANAGE_PY_SCRIPT_NAME] + command_args
    print(f"Ejecutando comando Django desde: {DJANGO_PROJECT_DIR}")
    print(f"Comando: {' '.join(full_command)}")
    if command_args and command_args[0] == "runserver": # Mostrar mensaje de CTRL+C solo para runserver
        print("Presiona CTRL+C para detener el servidor.")

    try:
        # Ejecutar el comando de Django
        # cwd (current working directory) se establece al directorio del proyecto Django
        # sys.executable asegura que se usa el mismo intérprete de Python que ejecuta este script
        process = subprocess.run(
            full_command,
            cwd=DJANGO_PROJECT_DIR,
            check=False # No lanzar excepción en Ctrl+C para runserver, Django maneja esto.
                        # Para otros comandos, podrías querer check=True o un manejo de errores más específico.
        )
        if process.returncode != 0:
            print(f"El comando de Django ('{' '.join(command_args)}') parece haberse detenido con un código de error: {process.returncode}")
            print("Revisa los mensajes anteriores para ver si hay errores específicos de Django.")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el ejecutable de Python ('{sys.executable}').")
    except KeyboardInterrupt:
        print("\nComando detenido por el usuario (CTRL+C).") # Principalmente para runserver
    except Exception as e:
        print(f"Ocurrió un error inesperado al intentar ejecutar el comando: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python iniciar_servidor.py <comando_django> [argumentos...]")
        print("Ejemplo para iniciar servidor: python iniciar_servidor.py runserver")
        print("Ejemplo para migrar: python iniciar_servidor.py migrate")
        sys.exit(1)

    django_command_and_args = sys.argv[1:] # Todos los argumentos después del nombre del script
    run_django_command(django_command_and_args)

