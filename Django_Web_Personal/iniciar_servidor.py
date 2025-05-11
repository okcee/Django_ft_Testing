import subprocess
import os
import sys

# Directorio del proyecto Django (donde se encuentra manage.py)
# Según tu indicación, manage.py está en: S:\_Django_ft_Testing\Django_Web_Personal\webpersonal\manage.py
DJANGO_PROJECT_DIR = r"S:\_Django_ft_Testing\Django_Web_Personal\webpersonal"
MANAGE_PY_SCRIPT_NAME = "manage.py" # Nombre del script de Django

def run_django_server():
    """
    Inicia el servidor de desarrollo de Django.
    """
    manage_py_path = os.path.join(DJANGO_PROJECT_DIR, MANAGE_PY_SCRIPT_NAME)

    # Verificar que el directorio del proyecto y manage.py existen
    if not os.path.isdir(DJANGO_PROJECT_DIR):
        print(f"Error: El directorio del proyecto Django '{DJANGO_PROJECT_DIR}' no existe.")
        return

    if not os.path.isfile(manage_py_path):
        print(f"Error: El script '{MANAGE_PY_SCRIPT_NAME}' no se encontró en '{DJANGO_PROJECT_DIR}'.")
        print("Asegúrate de que la ruta es correcta y que estás en el directorio correcto del proyecto Django.")
        return

    print(f"Iniciando el servidor de desarrollo de Django desde: {DJANGO_PROJECT_DIR}")
    print(f"Comando a ejecutar: {sys.executable} {MANAGE_PY_SCRIPT_NAME} runserver")
    print("Presiona CTRL+C para detener el servidor.")

    try:
        # Ejecutar el comando 'python manage.py runserver'
        # cwd (current working directory) se establece al directorio del proyecto Django
        # sys.executable asegura que se usa el mismo intérprete de Python que ejecuta este script
        process = subprocess.run(
            [sys.executable, MANAGE_PY_SCRIPT_NAME, "runserver"],
            cwd=DJANGO_PROJECT_DIR,
            check=False # No lanzar excepción en Ctrl+C, Django maneja esto.
        )
        if process.returncode != 0:
            print(f"El servidor de Django parece haberse detenido con un código de error: {process.returncode}")
            print("Revisa los mensajes anteriores para ver si hay errores específicos de Django.")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el ejecutable de Python ('{sys.executable}').")
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario (CTRL+C).")
    except Exception as e:
        print(f"Ocurrió un error inesperado al intentar iniciar el servidor: {e}")

if __name__ == "__main__":
    run_django_server()