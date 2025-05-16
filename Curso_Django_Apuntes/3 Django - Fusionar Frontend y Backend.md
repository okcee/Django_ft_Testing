# Fusionar Backend y Frontend en Django

Django es un framework de desarrollo web que permite integrar fácilmente el backend (lógica del servidor, base de datos) con el frontend (HTML, CSS, JS) mediante su sistema de templates. Esta fusión facilita el desarrollo de aplicaciones web completas y coherentes.

---

## ⚙️ ¿Cómo funciona la integración?

Django usa su motor de **templates** para renderizar contenido dinámico desde el backend y enviarlo al navegador del cliente como HTML. Esto se hace utilizando vistas que devuelven respuestas basadas en templates, los cuales pueden incluir variables, estructuras de control y componentes reutilizables.

---

## 🧩 Estructura típica del proyecto

```
mi_proyecto/
├── app/
│   ├── views.py
│   ├── templates/
│   │   └── app/
│   │       └── index.html
├── static/
│   └── app/
│       ├── style.css
│       └── script.js
├── urls.py
```

---

## 📝 1. Vista en `views.py`

```python
from django.shortcuts import render

def inicio(request):
    contexto = {
        'titulo': 'Bienvenido a mi sitio',
        'usuario': 'Carlos'
    }
    return render(request, 'app/index.html', contexto)
```

---

## 🌐 2. Template HTML (`templates/app/index.html`)

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ titulo }}</title>
    <link rel="stylesheet" href="{% static 'app/style.css' %}">
</head>
<body>
    <h1>{{ titulo }}</h1>
    <p>Hola, {{ usuario }}.</p>

    <script src="{% static 'app/script.js' %}"></script>
</body>
</html>
```

---

## 🔗 3. Configuración de rutas (`urls.py`)

```python
from django.urls import path
from app import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
```

---

## 🧷 4. Habilitar archivos estáticos (`settings.py`)

```python
STATIC_URL = '/static/'

# Para desarrollo local:
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

---

## 🔒 5. Usar el tag `{% load static %}`

Para usar archivos estáticos como CSS o JS en un template:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'app/style.css' %}">
```

---

## 🧠 ¿Qué pasa internamente?

1. El usuario hace una petición (por ejemplo, a `/`).
2. Django busca una coincidencia en `urls.py`.
3. La vista correspondiente genera contexto y llama a un template.
4. El motor de templates inserta datos en el HTML.
5. El HTML resultante se envía al navegador.

---

## ✅ Buenas prácticas

- Usa el sistema de templates de Django para lógica simple de presentación.
- Centraliza archivos estáticos (CSS/JS) en la carpeta `static/`.
- Mantén tus templates organizados por aplicación.
- Usa variables del contexto para evitar hardcodear contenido.

---

## 📎 Referencias

- [Documentación oficial de Django sobre templates](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Uso de archivos estáticos](https://docs.djangoproject.com/en/stable/howto/static-files/)
