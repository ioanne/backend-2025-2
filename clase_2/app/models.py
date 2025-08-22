from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)

    alumno = relationship("Alumno", back_populates="usuario", uselist=False)


class Alumno(Base):
    __tablename__ = "alumno"
    id = Column(Integer, primary_key=True, index=True)
    carrera = Column(String, nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    usuario = relationship("Usuario", back_populates="alumno")
