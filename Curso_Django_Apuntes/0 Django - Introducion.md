# Django: Un Framework Web de Python

Django es un framework web de alto nivel, de código abierto y basado en Python, diseñado para el desarrollo web rápido y pragmático. Sigue el principio "Don't Repeat Yourself" (DRY - No te repitas) y se adhiere a la arquitectura Model-View-Template (MVT), que es una variación del patrón Model-View-Controller (MVC). Su objetivo es facilitar la creación de aplicaciones web complejas de forma eficiente y segura.  

## Funcionalidades Principales

Django viene con muchas características "de fábrica" que cubren la mayor parte de las necesidades de desarrollo web:  
    1. ORM (Object-Relational Mapper): Permite interactuar con tu base de datos usando código Python en lugar de SQL directamente. Soporta múltiples bases de datos (PostgreSQL, MySQL, SQLite, Oracle).  
    2. Sistema de URLs: Un potente sistema para definir patrones de URL y mapearlos a funciones o clases (vistas) que manejan las peticiones.  
    3. Motor de Plantillas: Un sistema para generar HTML de forma dinámica, separando la lógica de presentación del código Python.  
    4. Sistema de Autenticación y Autorización: Maneja usuarios, grupos, permisos y sesiones de forma segura.  
    5. Panel de Administración Automático: Genera una interfaz de administración (CRUD - Create, Read, Update, Delete) para tus modelos de forma automática, lo que ahorra muchísimo tiempo.  
    6. Sistema de Formularios: Facilita la creación, procesamiento y validación de formularios HTML.  
    7. Cacheo: Un framework configurable para almacenar en caché partes de tu sitio web y mejorar el rendimiento.
    8. Seguridad: Protección integrada contra muchas amenazas comunes como CSRF (Cross-Site Request Forgery), XSS (Cross-Site Scripting), SQL Injection, etc.
    9. Manejo de Archivos Estáticos y Multimedia: Facilita la gestión y el servicio de archivos como CSS, JavaScript, imágenes, etc.

## Apps Preinstaladas `(django.contrib)`

Cuando creas un nuevo proyecto Django, viene configurado por defecto con varias aplicaciones incluidas en django.contrib. Estas apps proporcionan funcionalidades comunes y esenciales:  
1. `django.contrib.admin:`
   - Qué es: El panel de administración automático de Django.
   - Para qué vale: Permite a los usuarios con los permisos adecuados gestionar el contenido de los modelos registrados en la base de datos a través de una interfaz web amigable, sin necesidad de escribir código de interfaz.
2. `django.contrib.auth:`
   - Qué es: El sistema de autenticación y autorización de Django.
   - Para qué vale: Maneja usuarios, grupos, permisos y proporciona vistas y formularios para el registro de usuarios, login, logout, restablecimiento de contraseñas, etc. Es la base para controlar quién puede acceder a qué partes de tu sitio.
3. `django.contrib.contenttypes:`
   - Qué es: Un framework que permite trabajar con diferentes tipos de modelos instalados en tu proyecto.
   - Para qué vale: Es utilizado internamente por otras partes de Django (como el sistema de permisos o los comentarios genéricos) para referenciar modelos de forma genérica, independientemente de la app a la que pertenezcan.
4. `django.contrib.sessions:`
   - Qué es: El framework de sesiones de Django.
   - Para qué vale: Permite almacenar datos específicos del usuario entre peticiones. Es fundamental para mantener el estado del usuario (por ejemplo, si ha iniciado sesión, el contenido de un carrito de compra, etc.).
5. `django.contrib.messages:`
   - Qué es: El framework de mensajes (o "mensajes flash").
   - Para qué vale: Proporciona una forma de mostrar notificaciones temporales y únicas a los usuarios (por ejemplo, "Tu perfil se ha actualizado correctamente", "Contraseña incorrecta"), generalmente después de una redirección HTTP.
6. `django.contrib.staticfiles:`
   - Qué es: El framework para gestionar archivos estáticos.
   - Para qué vale: Ayuda a organizar, encontrar y servir archivos estáticos (CSS, JavaScript, imágenes, fuentes) durante el desarrollo y, de forma crucial, a recolectarlos (`collectstatic`) para su despliegue en producción.

## Archivos Iniciales de un Proyecto Django

Cuando creas un proyecto Django con django-admin startproject `<nombre_proyecto>`, se genera una estructura de directorios y archivos iniciales:  

`<nombre_proyecto>/`  
├── `manage.py`  
└── `<nombre_proyecto>/`  
    ├── `__init__.py`  
    ├── `asgi.py`  
    ├── `settings.py`  
    ├── `urls.py`  
    └── `wsgi.py`  

Estos archivos constituyen la estructura básica para comenzar a construir una aplicación web con Django.  

1. `manage.py:`  
    - Qué es: Un script de línea de comandos.  
    - Para qué vale: Es la utilidad principal para interactuar con tu proyecto Django. Lo usas para ejecutar comandos como runserver (iniciar el servidor de desarrollo), makemigrations, migrate (gestionar la base de datos), createsuperuser, startapp (crear nuevas aplicaciones), etc. Es tu punto de entrada para muchas operaciones de desarrollo y administración.  
2. `<nombre_proyecto>/__init__.py:`  
    - Qué es: Un archivo vacío (por defecto).  
    - Para qué vale: Indica a Python que este directorio (<nombre_proyecto>/) debe ser considerado un paquete Python.
3. `<nombre_proyecto>/asgi.py:`  
   - Qué es: Un archivo de configuración para servidores ASGI (Asynchronous Server Gateway Interface).
   - Para qué vale: Define el punto de entrada para servidores web asíncronos (como Daphne o Uvicorn) para servir tu proyecto. Es necesario si planeas usar funcionalidades asíncronas como WebSockets o vistas async/await (disponibles en versiones recientes de Django).
4. `<nombre_proyecto>/settings.py:`  
   - Qué es: El archivo de configuración principal de tu proyecto.
   - Para qué vale: Contiene todas las configuraciones del proyecto: la configuración de la base de datos (DATABASES), la lista de aplicaciones instaladas (INSTALLED_APPS), la clave secreta (SECRET_KEY), la configuración de archivos estáticos y multimedia, plantillas, middleware, zonas horarias, etc. Es el centro neurálgico de la configuración de tu proyecto.
5. `<nombre_proyecto>/urls.py:`  
   - Qué es: El archivo de configuración de URLs raíz del proyecto.
   - Para qué vale: Define los patrones de URL a nivel de proyecto. Generalmente, incluye URLs para las apps instaladas (usando include()) y URLs a nivel global (como el admin). Es donde se mapean las URLs entrantes a las vistas correspondientes.
6. `<nombre_proyecto>/wsgi.py:`
   - Qué es: Un archivo de configuración para servidores WSGI (Web Server Gateway Interface).
   - Para qué vale: Define el punto de entrada para servidores web síncronos compatibles con WSGI (el estándar tradicional para servir aplicaciones web Python, como Gunicorn o uWSGI) para servir tu proyecto. Es el archivo que los servidores web usan para comunicarse con tu aplicación Django.