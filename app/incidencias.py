from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import crud
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/incidencias", response_model=models.Incidencia)
def crear_incidencia(incidencia: models.Incidencia, db: Session = Depends(get_db)):
    return crud.crear_incidencia(db, incidencia)

@router.get("/incidencias/usuario/{email}", response_model=List[models.Incidencia])
def listar_por_usuario(email: str, db: Session = Depends(get_db)):
    return crud.obtener_incidencias_por_usuario(db, email)

@router.get("/incidencias/estado/{estado}", response_model=List[models.Incidencia])
def listar_por_estado(estado: models.EstadoIncidencia, db: Session = Depends(get_db)):
    return crud.obtener_incidencias_por_estado(db, estado)

@router.put("/incidencias/{id}/estado", response_model=models.Incidencia)
def cambiar_estado(id: int, nuevo_estado: models.EstadoIncidencia, db: Session = Depends(get_db)):
    incidencia = crud.cambiar_estado(db, id, nuevo_estado)
    if not incidencia:
        raise HTTPException(status_code=404, detail="Incidencia no encontrada")
    return incidencia

@router.delete("/incidencias/{id}")
def borrar(id: int, db: Session = Depends(get_db)):
    incidencia = crud.borrar_incidencia(db, id)
    if not incidencia:
        raise HTTPException(status_code=404, detail="Incidencia no encontrada")
    return {"mensaje": "Incidencia eliminada"}
