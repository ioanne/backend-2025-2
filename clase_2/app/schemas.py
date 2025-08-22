from pydantic import BaseModel
from typing import Optional

# REQUEST
class UsuarioCreateRequest(BaseModel):
    nombre: Optional[str] = None
    email: str

class AlumnoCreateRequest(BaseModel):
    carrera: Optional[str] = None
    usuario_id: int

# RESPONSE
class UsuarioResponse(BaseModel):
    id: int
    nombre: Optional[str]
    email: str

class Config:
    orm_mode = True

class AlumnoResponse(BaseModel):
    id: int
    carrera: Optional[str]
    usuario: UsuarioResponse

class Config:
    orm_mode = True