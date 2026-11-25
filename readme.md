# Blog Playground Final Project - Sebastian Muñoz

Este es el proyecto final para el curso de Python en CoderHouse (Tercera Entrega). Es una plataforma web desarrollada con Django que combina un sistema de blogs, una tienda básica y un sistema de mensajería entre usuarios.

## 🚀 Funcionalidades Principales

### 👤 Usuarios y Perfiles
- **Autenticación:** Sistema de Registro, Inicio de Sesión y Cierre de Sesión.
- **Perfil de Usuario:** Cada usuario tiene un perfil donde puede ver y editar su nombre, apellido, email, biografía y **avatar**.
- **Seguridad:** Opción de cambiar la contraseña desde el perfil.

### 📝 Sistema de Blogs (Pages)
- **CRUD Completo:** Creación, Lectura, Edición y Borrado de blogs.
- **Texto Enriquecido:** Uso de CKEditor para formato avanzado en los artículos.
- **Imágenes:** Soporte para subir imágenes en cada blog.
- **Buscador:** Filtrado de blogs por título con mensajes de error si no hay resultados.

### 💬 Mensajería Directa
- **Bandeja de Entrada:** Los usuarios pueden recibir mensajes de otros usuarios.
- **Mensajes Enviados:** Historial de mensajes mandados.
- **Comunicación:** Interfaz para enviar mensajes nuevos seleccionando el destinatario.

## 🛠️ Tecnologías Utilizadas
- Django 4.2+ / Python 3.x
- SQLite
- django-ckeditor
- Pillow (Manejo de imágenes)

## 📦 Instalación y Ejecución

1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`.
3. Ejecutar migraciones: `python gestionar.py migrate`.
4. Iniciar servidor: `python gestionar.py runserver`.

### Variables de entorno

| Variable | Uso | Por defecto |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Clave criptográfica de Django. Obligatoria si `DJANGO_DEBUG=False`. | En desarrollo se genera una aleatoria en cada arranque |
| `DJANGO_DEBUG` | Modo depuración | `True` |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos, separados por coma | vacío |

---
*Sebastian Muñoz - CoderHouse 2026*
