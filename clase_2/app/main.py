from fastapi import FastAPI
from app.routers import usuarios, alumnos

app = FastAPI() # Creando la instancia de fastapi
app.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
app.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])


# @app.get("/")
# async def hola_mundo():
#     return {"mensaje": "Hola mundo"}
