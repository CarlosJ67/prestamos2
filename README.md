# CRUD-PY-MYSQL

Este proyecto implementa un sistema CRUD (Crear, Leer, Actualizar, Eliminar) utilizando **FastAPI**, **SQLAlchemy** y **MySQL** para gestionar usuarios, materiales y préstamos.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

## Tabla de contenidos

- [CRUD-PY-MYSQL](#crud-py-mysql)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [Descripción](#descripción)
  - [Características](#características)
  - [Requisitos](#requisitos)
  - [Instalación](#instalación)
  - [Uso](#uso)
    - [Documentación interactiva](#documentación-interactiva)
    - [Ejemplo de JSON para crear un usuario](#ejemplo-de-json-para-crear-un-usuario)
  - [Endpoints](#endpoints)
    - [Usuarios](#usuarios)
    - [Materiales](#materiales)
    - [Préstamos](#préstamos)
  - [Contribuciones](#contribuciones)
  - [Licencia](#licencia)
  - [Contacto](#contacto)
- [CRUD-PRESTAMOS-FASTAPI](#crud-prestamos-fastapi)

---

## Descripción

Este proyecto permite gestionar:
- **Usuarios**: Crear, leer, actualizar y eliminar usuarios.
- **Materiales**: Registrar y gestionar materiales disponibles.
- **Préstamos**: Asignar materiales a usuarios y gestionar su estado.

Utiliza las siguientes tecnologías:
- **FastAPI**: Framework moderno para construir APIs RESTful.
- **SQLAlchemy**: ORM para interactuar con la base de datos MySQL.
- **Pydantic**: Validación de datos y serialización.
- **MySQL**: Base de datos relacional para almacenar información.

---

## Características

- API RESTful con documentación interactiva (`/docs` y `/redoc`).
- Validación automática de datos mediante Pydantic.
- Soporte para múltiples entidades: usuarios, materiales y préstamos.
- Manejo de estados y relaciones entre tablas.
- Autenticación segura (opcional, no implementada en esta versión).

---

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

1. **Python 3.8+**
2. **MySQL Server**
3. **Dependencias del proyecto** (ver `requirements.txt`)
4. **Cryptography** (necesario para autenticación MySQL):
   ```bash
   pip install cryptography
   ```

---

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/AlejandroRomero17/CRUD-PRESTAMOS-FASTAPI
   cd CRUD-PY-MYSQL
   ```

2. **Crea un entorno virtual**:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la conexión a la base de datos**:
   Edita el archivo `config/db.py` y actualiza la URL de conexión:
   ```python
   SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:tu_contraseña@localhost:3306/base_prueba"
   ```

5. **Ejecuta las migraciones** (si usas Alembic):
   ```bash
   alembic upgrade head
   ```

6. **Inicia la aplicación**:
   ```bash
   uvicorn main:app --reload
   ```

La API estará disponible en `http://127.0.0.1:8000`.

---

## Uso

### Documentación interactiva

- **Swagger UI**: Accede a `/docs` para explorar y probar los endpoints.
- **ReDoc**: Accede a `/redoc` para una vista más limpia de la documentación.

### Ejemplo de JSON para crear un usuario

```json
{
    "nombre": "Juan",
    "primer_apellido": "Pérez",
    "segundo_apellido": "García",
    "tipo_usuario": "Alumno",
    "nombre_usuario": "juanperez123",
    "correo_electronico": "juan.perez@example.com",
    "contrasena": "contraseña_segura_123",
    "numero_telefono": "555-1234",
    "estatus": "Activo"
}
```

Envía este JSON a la ruta `POST /users` para crear un nuevo usuario.

---

## Endpoints

### Usuarios
- `GET /users`: Lista todos los usuarios.
- `POST /users`: Crea un nuevo usuario.
- `GET /users/{id}`: Obtiene un usuario por ID.
- `PUT /users/{id}`: Actualiza un usuario existente.
- `DELETE /users/{id}`: Elimina un usuario.

### Materiales
- `GET /materials`: Lista todos los materiales.
- `POST /materials`: Crea un nuevo material.
- `GET /materials/{id}`: Obtiene un material por ID.
- `PUT /materials/{id}`: Actualiza un material existente.
- `DELETE /materials/{id}`: Elimina un material.

### Préstamos
- `GET /loans`: Lista todos los préstamos.
- `POST /loans`: Crea un nuevo préstamo.
- `GET /loans/{id}`: Obtiene un préstamo por ID.
- `PUT /loans/{id}`: Actualiza un préstamo existente.
- `DELETE /loans/{id}`: Elimina un préstamo.

---

## Contribuciones

Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m "Añadir nueva funcionalidad"`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request.

Toda ayuda es bienvenida, ya sea para corregir errores, mejorar la documentación o agregar nuevas características.

---

## Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme:

- **Nombre**: Alejandro Gonzalez Romero
- **Correo electrónico**: gonzalez.romero.alejandroo@gmail.com
- **GitHub**: (https://github.com/AlejandroRomero17)

---
# CRUD-PRESTAMOS-FASTAPI
