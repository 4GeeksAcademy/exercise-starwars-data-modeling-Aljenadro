import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    apellido = Column(String(255))
    password = Column(String(255))
    email = Column(String(255))
    fecha_suscripcion = Column(String(255))

class Planeta(Base):
    __tablename__ = 'planeta'
    id_planeta = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    clima = Column(String(255))
    terreno = Column(String(255))
    poblacion = Column(Integer)

class Personaje(Base):
    __tablename__ = 'personaje'
    id_personaje = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    altura = Column(Float)
    peso = Column(Float)
    genero = Column(String(255))
    especie = Column(String(255))

class Favorito(Base):
    __tablename__ = 'favorito'
    id_favorito = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=True)
    id_planeta = Column(Integer, ForeignKey('planet.id_planeta'), nullable=True)
    id_personaje = Column(Integer, ForeignKey('personaje.id_personaje'), nullable=True)
    
    usuario = relationship("Usuario", foreign_keys=[id_usuario])
    planeta = relationship("Planeta", foreign_keys=[id_planeta])
    personaje = relationship("Personaje", foreign_keys=[id_personaje])

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
