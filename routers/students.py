from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
#from uuid import UUID
import models.models as Models
from models.seeder import engine, SessionLocal

from sqlalchemy.orm import Session

router = APIRouter()

Models.BaseModel.metadata.create_all(bind=engine)


def get_db_alumnos():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_db_notas():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Alumno(BaseModel):
    dni: str = Field(min_length=1)
    clave_comillas:int = Field(gt=0, lt=999999999)
    nombre: str = Field(min_length=1)
    apellido_1: str = Field(min_length=1)
    apellido_2: str = Field(min_length=1)

class Notas(BaseModel):
    id_asignatura: int = Field(gt=0, lt=20)
    clave_comillas: int = Field(gt=0, lt=999999999)
    nota: float = Field(gt=0, lt=10)
    id_curriculo: int = Field(gt=0, lt=999999999)

ALUMNOS = []

@router.get('/students')
async def leer_api(db: Session=Depends(get_db_alumnos)):
    return db.query(Models.Alumnos).all()

@router.get('/{clave_comillas}')
async def ver_alumno(clave_comillas: int, db : SessionLocal = Depends(get_db_alumnos)):
    alumno_model = db.query(Models.Alumnos).filter(Models.Alumnos.clave_comillas == clave_comillas).first()
    if alumno_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"{clave_comillas} : El alumno no está agregado"
        )
    return alumno_model

@router.post('/add_student')
async def crear_alumno(alumno: Alumno, db: SessionLocal = Depends(get_db_alumnos)):
    alumno_model = Models.Alumnos()
    alumno_model.dni = alumno.dni
    alumno_model.clave_comillas = alumno.clave_comillas
    alumno_model.nombre = alumno.nombre
    alumno_model.apellido_1 = alumno.apellido_1
    alumno_model.apellido_2 = alumno.apellido_2

    db.add(alumno_model)
    db.commit()

    return alumno

@router.get('/{clave_comillas}/grades')
async def ver_alumno(clave_comillas: int, db : SessionLocal = Depends(get_db_notas)):
    alumno_model = db.query(Models.Notas).filter(Models.Notas.clave_comillas == clave_comillas).first()
    if alumno_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"{clave_comillas} : El alumno no está agregado"
        )
    return alumno_model

@router.post('/grades')
async def ver_alumno(nota_alumno: Notas,  db : SessionLocal = Depends(get_db_notas)):
    alumno_model = Models.Notas()
    alumno_model.clave_comillas = nota_alumno.clave_comillas
    alumno_model.id_asignatura = nota_alumno.id_asignatura
    alumno_model.nota = nota_alumno.nota
    alumno_model.id_curriculo = nota_alumno.id_curriculo

    db.add(alumno_model)
    db.commit()

    return nota_alumno



