from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint
from models.seeder import BaseModel



class Alumnos(BaseModel):
    __tablename__ = "alumnos"
    dni = Column(String)
    clave_comillas = Column(Integer,  primary_key=True)
    nombre = Column(String)
    apellido_1 = Column(String)
    apellido_2 = Column(String)

    rel_clave_notas = relationship('Notas', backref='Alumnos.clave_comillas', primaryjoin='Alumnos.clave_comillas==Notas.clave_comillas', lazy='dynamic')


class Asignaturas(BaseModel):
    __tablename__ = "asignaturas"
    id_asignatura = Column(Integer, primary_key=True)
    nombre_asignatura = Column(String)

    rel_id_notas = relationship('Notas', backref='Asignatura.id_asignatura', primaryjoin='Asignaturas.id_asignatura==Notas.id_asignatura', lazy='dynamic')
    rel_id_alias = relationship('Aliases_asignaturas', backref='Asignaturas.id_asignatura', primaryjoin='Asignaturas.id_asignatura==Aliases_asignaturas.id_asignatura', lazy='dynamic')
    rel_id_curric = relationship('Curriculos', backref='Asignaturas.id_asignatura',primaryjoin='Asignaturas.id_asignatura==Curriculos.id_asignatura', lazy='dynamic')


class Cursos(BaseModel):
    __tablename__ = "cursos"
    id_curso = Column(Integer, primary_key=True)
    nombre_curso = Column(String)

    rel_id_curso = relationship('Curriculos', backref='Cursos.id_curso', primaryjoin='Cursos.id_curso==Curriculos.id_curso', lazy='dynamic')

class Curriculos(BaseModel):
    __tablename__ = "curriculos"
    id_curriculo = Column(Integer, primary_key=True)
    id_curso = Column(Integer, ForeignKey(Cursos.id_curso)) 
    id_asignatura = Column(Integer, ForeignKey(Asignaturas.id_asignatura)) 

    rel_id_curriculo = relationship('Notas', backref='Curriculos.id_curriculo', primaryjoin='Curriculos.id_curriculo==Notas.id_curriculo', lazy='dynamic')

class Notas(BaseModel):
    __tablename__ = "notas"
    id_asignatura = Column(Integer, ForeignKey(Asignaturas.id_asignatura))  
    clave_comillas = Column(Integer, ForeignKey(Alumnos.clave_comillas)) 
    nota = Column(Float)
    id_curriculo = Column(Integer, ForeignKey(Curriculos.id_curriculo))

    __table_args__ = (PrimaryKeyConstraint("clave_comillas", "id_asignatura"),)

class Aliases_asignaturas(BaseModel):
    __tablename__ = "aliases_asignaturas"
    id_asignatura = Column(Integer, ForeignKey(Asignaturas.id_asignatura))
    nombre_alias = Column(String)
    id_alias = Column(Integer, primary_key=True)





