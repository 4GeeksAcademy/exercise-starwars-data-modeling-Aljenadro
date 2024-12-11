import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    lastname = Column(String(120), nullable=False)
    password = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    suscription = Column(String(255), nullable=False)
    favorites = relationship("Favorite", back_populates="user")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    climate = Column(String(255))
    terrain = Column(String(255))  # Corregido de 'land' a 'terrain'
    population = Column(Integer)
    favorites = relationship("Favorite", back_populates="planet")

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    gender = Column(String(255))
    specie = Column(String(255))
    favorites = relationship("Favorite", back_populates="people")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=True)
    id_planet = Column(Integer, ForeignKey('planet.id'), nullable=True)
    id_people = Column(Integer, ForeignKey('people.id'), nullable=True)
    
    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")
    people = relationship("People", back_populates="favorites")

# Generar el diagrama
render_er(Base, 'diagram.png')
