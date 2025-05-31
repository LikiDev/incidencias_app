from fastapi import FastAPI
from database import engine
import models
import incidencias

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

# Instanciar la app FastAPI
app = FastAPI()

# Incluir las rutas definidas en incidencias.py
app.include_router(incidencias.router)
