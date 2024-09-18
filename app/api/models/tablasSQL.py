from sqlalchemy import column, Integer,String,Float,Date,ForeignKey

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

#llamado a la base para crear una tabla

Base = declarative_base()

#definicion de las tablas de mi modelo

#tabla usuario

class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=column(String(50))
    fechaNacimiento=column(Date)
    ubicacion=column(String(100))
    metaAhorro=column(float)


class Gasto(Base):
    __tablename__='Gasto'
    id=column(Integer, primary_key=True, autoincrement=True)
    descripcion=(String(50))
    categoria=column(String(50))
    valor=column(float)
    fecha=column(Date)

class Categoria(Base):
    __tablename__='Categoria'
    nombre=column(String(50))
    id=column(Integer, primary_key=True, autoincrement=True)
    descripcion=(String(50))
    fotoCategoria=(String(100))


class Ingreso(Base):
    __tablename__='Ingreso'
    id=column(Integer, primary_key=True, autoincrement=True)
    valor=column(float)
    fechaIngreso=column(Date)

