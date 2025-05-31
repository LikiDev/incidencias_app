from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

import models

# Crear una nueva incidencia
def crear_incidencia(db: Session, incidencia: models.Incidencia):
    db_incidencia = models.IncidenciaDB(
        latitud=incidencia.latitud,
        longitud=incidencia.longitud,
        descripcion=incidencia.descripcion,
        email=incidencia.email,
        estado=incidencia.estado or models.EstadoIncidencia.abierta,
        fecha=datetime.now() if incidencia.fecha is None else incidencia.fecha
    )
    db.add(db_incidencia)
    db.commit()
    db.refresh(db_incidencia)
    return db_incidencia

# Obtener incidencias por email de usuario
def obtener_incidencias_por_usuario(db: Session, email: str) -> List[models.IncidenciaDB]:
    return db.query(models.IncidenciaDB).filter(models.IncidenciaDB.email == email).all()

# Obtener incidencias por estado
def obtener_incidencias_por_estado(db: Session, estado: models.EstadoIncidencia) -> List[models.IncidenciaDB]:
    return db.query(models.IncidenciaDB).filter(models.IncidenciaDB.estado == estado).all()

# Cambiar el estado de una incidencia
def cambiar_estado(db: Session, incidencia_id: int, nuevo_estado: models.EstadoIncidencia):
    incidencia = db.query(models.IncidenciaDB).filter(models.IncidenciaDB.id == incidencia_id).first()
    if incidencia is not None:
        incidencia.estado = nuevo_estado
        db.commit()
        db.refresh(incidencia)
    return incidencia

# Eliminar una incidencia
def borrar_incidencia(db: Session, incidencia_id: int):
    incidencia = db.query(models.IncidenciaDB).filter(models.IncidenciaDB.id == incidencia_id).first()
    if incidencia:
        db.delete(incidencia)
        db.commit()
    return incidencia
