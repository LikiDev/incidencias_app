from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from enum import Enum

from sqlalchemy import Column, Integer, String, Float, DateTime, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# Enum del estado de la incidencia
class EstadoIncidencia(str, Enum):
    abierta = "Abierta"
    en_curso = "En curso"
    resuelta = "Resuelta"

# Modelo SQLAlchemy para la tabla de incidencias
class IncidenciaDB(Base):
    __tablename__ = "incidencias"

    id = Column(Integer, primary_key=True, index=True)
    latitud = Column(Float, nullable=False)
    longitud = Column(Float, nullable=False)
    descripcion = Column(String, nullable=False)
    email = Column(String, ForeignKey("users.email"), nullable=False)
    estado = Column(SqlEnum(EstadoIncidencia), default=EstadoIncidencia.abierta)
    fecha = Column(DateTime, default=datetime.utcnow)

# Modelo Pydantic para recibir y devolver incidencias vía API
class Incidencia(BaseModel):
    id: Optional[int] = None
    latitud: float
    longitud: float
    descripcion: str
    email: EmailStr
    estado: Optional[EstadoIncidencia] = EstadoIncidencia.abierta
    fecha: Optional[datetime] = None

    class Config:
        orm_mode = True

# Modelo SQLAlchemy para la tabla de usuarios
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=True)

    incidencias = relationship("IncidenciaDB", backref="usuario")

# Modelo Pydantic para representar usuarios en la API
class User(BaseModel):
    email: EmailStr
    nombre: Optional[str] = None

    class Config:
        orm_mode = True
