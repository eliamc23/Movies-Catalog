from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.models import Movie
from sqlalchemy import select
from app.database import get_db
from app.schemas import Movie_Create, Movie_Update, Movie_Out

router = APIRouter(prefix="/api/v1/movies", tags=["movies"])

@router.get("/", response_model=list[Movie_Out])
def get_movies(db: Session = Depends(get_db)):
    return db.scalars(select(Movie)).all()

@router.post("/", response_model=Movie_Out, status_code=status.HTTP_201_CREATED)
def create_movie(movie: Movie_Create, db: Session = Depends(get_db)):
    new_movie = Movie(title=movie.title, year=movie.year, genre=movie.genre)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

@router.get("/{movie_id}", response_model=Movie_Out)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.get(Movie, movie_id)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return movie

@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.get(Movie, movie_id)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    db.delete(movie)
    db.commit()

@router.put("/{movie_id}", response_model=Movie_Out)
def update_movie(movie_id: int, movie_update: Movie_Update, db: Session = Depends(get_db)):
    movie = db.get(Movie, movie_id)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    for key, value in movie_update.model_dump(exclude_unset=True).items():
        setattr(movie, key, value)
    db.commit()
    return movie