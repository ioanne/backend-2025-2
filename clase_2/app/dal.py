from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app import models, schemas


async def crear_usuario(db: AsyncSession, usuario: schemas.UsuarioCreateRequest):
    nuevo_usuario = models.Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    await db.commit()
    await db.refresh(nuevo_usuario)
    return nuevo_usuario


async def crear_alumno(db: AsyncSession, alumno: schemas.AlumnoCreateRequest):
    nuevo_alumno = models.Alumno(**alumno.dict())
    db.add(nuevo_alumno)
    await db.commit()
    await db.refresh(nuevo_alumno)
    result = await db.execute(
        select(models.Alumno).options(selectinload(models.Alumno.usuario)
    ).where(models.Alumno.id == nuevo_alumno.id))
    alumno_con_relacion = result.scalar_one()
    return alumno_con_relacion


async def obtener_usuarios(db: AsyncSession):
    result = await db.execute(select(models.Usuario))
    return result.scalars().all()


async def obtener_alumnos(db: AsyncSession):
    result = await db.execute(
        select(models.Alumno).options(selectinload(models.Alumno.usuario))
    )
    return result.scalars().all()
