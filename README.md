# Sistema de Incidencias Ciudadanas

Este proyecto implementa una API básica gestionar incidencias reportadas por ciudadanos. He reutilizado la idea que fué mi proyecto de un master anterior de programación avanzada Full Stack.

---

## Funcionalidades implementadas

He hecho un crear, dos listar, un cambiar (en este caso cambiar estado) y un eliminar:

- **Crear una incidencia ciudadana** geolocalizable, con descripcion, email, fecha y estado.
- **Listar incidencias por usuario** (email como parámetro).
- **Listar incidencias por estado** (Abierta, En curso, Resuelta).
- **Cambiar el estado** de una incidencia existente.
- **Eliminar una incidencia**. 

Aquí he visto un pequeño fallo ya corregido: inicialmente en el Modelo (base model) no devolvía el ID de la Incidencia, por lo que, cuando quería borrar una incidencia no sabía qué id borrar. Así que he añadido : 
id: Optional[int] 
al modelo y ahora ya puedo saber el ID en los GET 

---

##  Modelo de datos

Cada incidencia tiene los siguientes campos:

- `id`: Identificador único (autogenerado).
- `latitud` y `longitud`: Coordenadas del incidente.
- `descripcion`: Texto libre con el problema.
- `email`: Correo del ciudadano que la reporta.
- `estado`: Uno de `Abierta`, `En curso`, `Resuelta`. (por defecto: `Abierta`)
- `fecha`: Fecha de creación (automática).

También he definido al usuario como `User`, para eventualmente (como mejora no implementada), relacionarlo como FK con incidencia usando el mail.

---

## Cómo ejecutar la aplicación

### 1. Instala dependencias
pip install fastapi uvicorn sqlalchemy pydantic email-validator requests

### 2. Ejecuta el servidor
uvicorn main:app --reload

### 3. He testeado la API usando Swagger de fastapi
- http://127.0.0.1:8000/docs

### 4. Y el juego de pruebas esta en test_requests.py
python test_requests.py

##  Estructura del proyecto

app/
├── main.py            # Punto de entrada FastAPI
├── database.py        # Configuración SQLAlchemy + SQLite
├── models.py          # Modelos SQLAlchemy y Pydantic
├── crud.py            # Funciones de acceso a la base de datos
├── incidencias.py     # Endpoints de la API
├── test_requests.py   # Script para pruebas manuales con requests

