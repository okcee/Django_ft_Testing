# La App Django (Core)

**Comando**
Sintaxis básica:    `python manage.py startapp <nombre_app>`
Por convención:     `python manage.py startapp core`

Esta es la primera *"App"* a crear dentro del proyecto web de Django. No se refiere al núcleo del proyecto Django, si no a una aplicación que por convención también lleva el nombre de Core, que se usa para entender y gestionar el flujo de datos del proyecto.  

Esto es algo muy común en los proyectos Django: crear una app llamada core (o similar) para contener funcionalidades que son transversales, de base o utilizadas por múltiples partes del proyecto, en lugar de estar ligadas a una funcionalidad de negocio específica (como una app de "blog" o "tienda").  

Si ejecutas python `manage.py startapp core`, estás creando una aplicación llamada `core`. Esta app no es inherentemente "el" núcleo de Django (como los archivos de configuración principales del proyecto), sino que tú la has nombrado así para indicar que contendrá funcionalidades que consideras centrales o de propósito general para *tu proyecto* en particular.  

La estructura que se genera es la estándar para cualquier app de Django:  
```RTF
core/  
├── migrations/  
│   └── __init__.py  
├── __init__.py  
├── admin.py  
├── apps.py  
├── models.py  
├── tests.py  
└── views.py  
```

## `core/__init__.py`

* **Qué es:** Es un archivo vacío (generalmente).
* **Para qué vale:** Indica a Python que el directorio `core/` debe ser tratado como un paquete Python. Es necesario para que puedas importar módulos y objetos desde dentro de `core` (por ejemplo, `from core import models`).

## `core/admin.py`

* **Qué es:** Un módulo donde registras tus modelos para que aparezcan en el panel de administración de Django.
* **Para qué vale:** Si defines modelos en `core/models.py` (ver abajo) y quieres poder ver, crear, editar o eliminar registros de esos modelos usando la interfaz web del admin de Django, debes registrarlos aquí usando `admin.site.register()`.

## `core/apps.py`

* **Qué es:** El archivo de configuración de la aplicación.
* **Para qué vale:** Contiene la clase `AppConfig` para tu app (`CoreConfig` en este caso). Define propiedades como el nombre legible de la app. Esta es la clase que se añade a la lista `INSTALLED_APPS` en tu archivo `settings.py` para activar la aplicación `core` en tu proyecto. Puede usarse para lógica de inicialización avanzada cuando la app se carga.

## `core/models.py`

* **Qué es:** Un módulo donde defines los modelos de base de datos de tu aplicación `core`.
* **Para qué vale:** Aquí creas clases Python que heredan de `django.db.models.Model`. Cada clase representa una tabla en tu base de datos y define sus campos y relaciones. Dado que esta app se llama `core`, aquí podrías definir modelos que sean fundamentales o transversales para todo el proyecto (por ejemplo, un modelo `TimestampedModel` abstracto del que hereden otros modelos, o modelos para configuraciones globales del sitio).

## `core/tests.py`

* **Qué es:** Un módulo donde escribes pruebas automatizadas para tu aplicación.
* **Para qué vale:** Contiene clases y funciones para verificar que la lógica de tu app (modelos, vistas, etc.) funciona como esperas. Es crucial para asegurar la calidad y estabilidad de tu código a medida que evoluciona.

## `core/views.py`

* **Qué es:** Un módulo donde defines las funciones o clases que manejan las peticiones web (vistas).
* **Para qué vale:** Aquí escribes la lógica que recibe una petición `HttpRequest`, interactúa con los modelos si es necesario y devuelve una `HttpResponse` (por ejemplo, renderizando un template HTML, devolviendo JSON, etc.). En una app `core`, podrías poner vistas que no encajan en otras apps, como una vista para la página de inicio genérica, páginas de errores personalizadas, etc.
* `HttpResponse` **HttpResponse** para añadir un método que permite contestar a una petición devolviendo un código.  

## `core/migrations/`

* **Qué es:** Un directorio que almacena los archivos de migración de base de datos para la aplicación `core`.
* **Para qué vale:** Cuando haces cambios en tu `core/models.py` (añades/modificas/eliminas modelos o campos), ejecutas `python manage.py makemigrations core`. Django genera archivos aquí (como `0001_initial.py`) que describen esos cambios. Luego, `python manage.py migrate` aplica esos cambios a tu base de datos.
* **`core/migrations/__init__.py`**: Simplemente le dice a Python que `migrations/` es un paquete.