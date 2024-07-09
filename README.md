# Cabañas Doña Arminda

Cabañas Doña Arminda es un proyecto web que ofrece una experiencia única de relajación y conexión con la naturaleza, destacando la historia y el legado de las cabañas fundadas por Doña Arminda. Este proyecto está diseñado para proporcionar información detallada sobre las cabañas, su ubicación, comodidades y opciones de alojamiento.

## Descripción del Proyecto

El sitio web de Cabañas Doña Arminda presenta una estructura clara y accesible, permitiendo a los usuarios obtener información sobre la historia, ubicación, entorno, alojamiento y comodidades de las cabañas. Además, incluye una sección de catálogo que muestra diferentes opciones de cabañas disponibles para los huéspedes.

## Estructura del Proyecto

- **Header**: Incluye el logotipo de la empresa y una barra de navegación con enlaces a las páginas de Inicio, Nosotros, Términos y Condiciones, y Contacto.
- **Main**: Contiene una sección principal con información detallada sobre la historia, ubicación, entorno y comodidades de las cabañas.
- **Catalogue**: Presenta una sección de catálogo con varias opciones de cabañas disponibles.
- **Footer**: Incluye un mensaje de derechos de autor.

## Tecnologías Utilizadas

- **Django**: Framework web para el desarrollo del sitio.
- **HTML5**: Para la estructura del sitio web.
- **CSS3**: Para el diseño y estilo del sitio web.
- **JavaScript**: Para la funcionalidad interactiva.
- **SQLite**: Base de datos por defecto para el proyecto Django.

## Instrucciones de Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/Hatusil/cac_backend.git
    ```

2. Navegar al directorio del proyecto:
    ```sh
    cd cac_backend
    ```

3. Crear y activar el entorno virtual:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate
    ```

4. Instalar las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

5. Realizar las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```

6. Ejecutar el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

7. Abrir el navegador web y acceder a:
    ```
    http://127.0.0.1:8000/
    ```

## Estructura de Directorios

```plaintext
cac_backend/
├── cac_backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── form.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   │   ├── seven.png
│   │   ├── IMG (0).jpeg
│   │   ├── IMG (1).jpeg
│   │   ├── IMG (2).jpeg
│   │   ├── IMG (3).jpeg
│   │   ├── IMG (4).jpeg
│   │   ├── IMG (5).jpeg
│   │   └── IMG (6).jpeg
├── manage.py
├── requirements.txt
```
## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes alguna idea para mejorar el proyecto, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama:
    ```sh
    git checkout -b feature/nueva-funcionalidad
    ```
3. Realiza los cambios necesarios y haz commit:
    ```sh
    git commit -m 'Agregar nueva funcionalidad'
    ```
4. Sube los cambios a tu rama:
    ```sh
    git push origin feature/nueva-funcionalidad
    ```
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

## Contacto

Para preguntas o comentarios, puedes contactarnos en [GitHub](https://github.com/Manuelfg1985) o a través del correo [hatusil@proton.me](mailto:hatusil@proton.me).

Derechos de autor © 2024 - Todos los derechos reservados.
