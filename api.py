from fastapi import FastAPI
from app.database import init_db
from app.routes.movies import router as movies_router

init_db()
app = FastAPI()
app.include_router(movies_router)



@app.get("/")
def home():
    return {"message": "Catalogo de peliculas"}

