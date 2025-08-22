from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, dal, database

router = APIRouter()


async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session


@router.post("/", response_model=schemas.AlumnoResponse)
async def crear(alumno: schemas.AlumnoCreateRequest, db:
AsyncSession = Depends(get_db)):
    return await dal.crear_alumno(db, alumno)


@router.get("/", response_model=list[schemas.AlumnoResponse])
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_alumnos(db)
