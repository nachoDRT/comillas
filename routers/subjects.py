from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
# from uuid import UUID
import models.models as Models
from models.seeder import engine, SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

Models.BaseModel.metadata.create_all(bind=engine)


def get_db_aliases_asignaturas():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_db_asignaturas():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_db_curriculo():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_db_curso():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Aliases_asignaturas(BaseModel):
    id_alias: int = Field(gt=0)
    nombre_alias: str = Field(min_length=1)
    id_asignatura: int = Field(gt=0, lt=9999999)


class Asignaturas(BaseModel):
    id_asignatura: int = Field(gt=0)
    nombre_asignatura: str = Field(min_length=1)
    

class Curriculo(BaseModel):
    id_curriculo: int = Field(gt=0, lt=9999999)
    id_curso: int = Field(gt=0, lt=9999999)
    id_asig: int = Field(gt=0, lt=9999999)

class Curso(BaseModel):
    id_curso: int = Field(gt=0, lt=9999999)
    descripcion: str = Field(min_length=1)
    
@router.get('/subjects')
async def leer_subjects(db: Session=Depends(get_db_asignaturas)):
    return db.query(Models.Asignaturas).all()

@router.get('/subjects/aliases')
async def leer_aliases(db: Session=Depends(get_db_aliases_asignaturas)):
    return db.query(Models.Aliases_asignaturas).all()

@router.get('/subjects/curriculo')
async def leer_curriculo(db: Session=Depends(get_db_curriculo)):
    return db.query(Models.Curriculos).all()

@router.get('/subjects/curso')
async def leer_curso(db: Session=Depends(get_db_curso)):
    return db.query(Models.Cursos).all()

@router.post('/subjects/add_subject')
async def crear_asignatura(asignatura: Asignaturas, db: SessionLocal = Depends(get_db_asignaturas)):
    asignatura_model = Models.Asignaturas()
    asignatura_model.id_asignatura = asignatura.id_asignatura
    asignatura_model.nombre_asignatura = asignatura.nombre_asignatura

    db.add(asignatura_model)
    db.commit()

    return asignatura

@router.post('/subjects/add_alias') ###poner vector como paeametro. que haga cambio a json
async def crear_alias_asignatura(alias: Aliases_asignaturas, db: SessionLocal = Depends(get_db_aliases_asignaturas)):
    aliases_model = Models.Aliases_asignaturas()
    aliases_model.id_alias = alias.id_alias
    aliases_model.nombre_alias = alias.nombre_alias
    aliases_model.id_asignatura = alias.id_asignatura

    db.add(aliases_model)
    db.commit()

    return alias

@router.post('/subjects/curriculo')
async def crear_curriculo(curriculo: Curriculo, db: SessionLocal = Depends(get_db_curriculo)):
    curr_model = Models.Curriculos()
    curr_model.id_curriculo = curriculo.id_curriculo
    curr_model.id_asignatura = curriculo.id_asig
    curr_model.id_curso = curriculo.id_curso

    db.add(curr_model)
    db.commit()

    return curriculo

@router.post('/subjects/curso')
async def crear_curso(curso: Curso,db: SessionLocal =Depends(get_db_curso)):
    curso_model = Models.Cursos()
    curso_model.id_curso = curso.id_curso
    curso_model.nombre_curso = curso.descripcion

    db.add(curso_model)
    db.commit()
    return curso