# Proyecto de Evaluaciones Virtuales Asistidas (EVA)

Este repositorio contiene el código fuente y los recursos para la plataforma de Evaluaciones Virtuales Asistidas (EVA).

## Descripción

EVA es una aplicación web diseñada para facilitar la evaluación virtual de estudiantes. Proporciona funcionalidades para administrar perfiles de estudiantes, gestionar asignaturas y facilitar la comunicación con los profesores.

## Características

- **Gestión de Perfiles:** Los estudiantes pueden acceder y actualizar sus perfiles.
- **Administración de Asignaturas:** Visualización de las asignaturas disponibles y acceso a recursos relacionados.
- **Comunicación con Profesores:** Facilita la comunicación y consulta con los profesores a través de la plataforma.

## Tecnologías Utilizadas

- **Frontend:** HTML, CSS (Bootstrap), JavaScript (jQuery)
- **Backend:** Python (Django)
- **Base de Datos:** SQLite (para desarrollo), PostgreSQL (para producción)

## Instalación

Para ejecutar localmente el proyecto, sigue estos pasos:

1. Clona este repositorio: `git clone https://github.com/tu_usuario/eva.git`
2. Crea un entorno virtual: `python -m venv env`
3. Activa el entorno virtual:
   - Windows: `env\Scripts\activate`
   - macOS/Linux: `source env/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Configura las variables de entorno en un archivo `.env` (opcional pero recomendado).
6. Ejecuta las migraciones de la base de datos: `python manage.py migrate`
7. Carga datos iniciales (opcional): `python manage.py loaddata initial_data`
8. Inicia el servidor de desarrollo: `python manage.py runserver`

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio y clónalo en tu máquina local.
2. Crea una rama para tu funcionalidad: `git checkout -b feature/nueva-funcionalidad`
3. Haz tus cambios y realiza commits: `git commit -m 'Agrega nueva funcionalidad'`
4. Empuja tus cambios a tu repositorio remoto: `git push origin feature/nueva-funcionalidad`
5. Haz un pull request en GitHub.

## Créditos

Este proyecto fue desarrollado por ""

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE]) para más detalles.

