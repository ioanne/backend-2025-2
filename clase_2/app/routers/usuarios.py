from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, dal, database

router = APIRouter()


async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session


@router.post("/", response_model=schemas.UsuarioResponse)
async def crear(usuario: schemas.UsuarioCreateRequest, db: AsyncSession = Depends(get_db)):
    return await dal.crear_usuario(db, usuario)


@router.get("/", response_model=list[schemas.UsuarioResponse])
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_usuarios(db)
