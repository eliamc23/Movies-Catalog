from app.database import init_db
from app.models import Movie
from sqlalchemy import select
from app.database import SessionLocal
from app.database import init_db

init_db()


print("===== Catalogo de Peliculas =====")

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def input_int_optional(prompt):
    while True:
        try:
            value = input(prompt)
            if value == "":
                return None
            return int(value)
        except ValueError:
            print("Por favor, ingrese un numero entero valido o deje el campo vacio.")



def add_movie():
    new_movie = Movie(
        title=input("Ingrese el titulo de la pelicula:"),
        year=input_int("Ingrese el año de lanzamiento de la pelicula:"),
        genre=input("Genero:")
    )
    with SessionLocal() as db:
        db.add(new_movie)
        db.commit()
        print(f"La pelicula '{new_movie.title}' ha sido agregada al catalogo.")


def show_movies():
    with SessionLocal() as db:
        movies = db.scalars(select(Movie)).all()
        if movies:
            print("===== Lista de Peliculas =====")
            for movie in movies:
                print(f"ID: {movie.id}, Titulo: {movie.title}, Año: {movie.year}, Genero: {movie.genre}")
        else:
            print("No hay peliculas en el catalogo.")


def search_movie():
    movie_id = input_int("Ingrese el ID de la pelicula que desea buscar: ")
    with SessionLocal() as db:
        movie = db.get(Movie, movie_id)
    if movie:
        print(f"ID: {movie.id}, Titulo: {movie.title}, Año: {movie.year}, Genero: {movie.genre}")
    else:
        print("Pelicula no encontrada.")





def delete_movie():
    movie_id = input_int("Ingrese el ID de la pelicula que desea eliminar: ")
    with SessionLocal() as db:
        movie = db.get(Movie, movie_id)
        if movie:
            db.delete(movie)
            db.commit()
            print(f"La pelicula ha sido eliminada del catalogo.")
        else:
            print("Pelicula no encontrada.")

def update_movie():
    movie_id = input_int("Ingrese el ID de la pelicula que desea actualizar: ")
    title=input("Ingrese el nuevo titulo de la pelicula:")
    year=input_int_optional("Ingrese el nuevo año de lanzamiento de la pelicula (deje en blanco para no cambiar):")
    genre=input("Ingrese el nuevo genero de la pelicula (deje en blanco para no cambiar):")
    
    with SessionLocal() as db:
        movie = db.get(Movie, movie_id)
        if movie:
            if title:
                movie.title = title
            if year is not None:
                movie.year = year
            if genre:
                movie.genre = genre
            db.commit()
            print("La pelicula ha sido actualizada.")
        else:
            print("Pelicula no encontrada.")




while True:
    print("1. Agregar pelicula")
    print("2. Ver peliculas")
    print("3. Buscar pelicula")
    print("4. Eliminar pelicula")
    print("5. Actualizar pelicula")
    print("6. Salir")
    option = input_int("Seleccione una opción (1-6): ")
    if option == 1:
        print("Has seleccionado agregar una pelicula")
        add_movie()
    elif option == 2:
        print("Has seleccionado ver peliculas")
        show_movies()
    elif option == 3:
        print("Has seleccionado buscar una pelicula")
        search_movie()
    elif option == 4:
        print("Has seleccionado eliminar una pelicula")
        delete_movie()
    elif option == 5:
        print("Has seleccionado actualizar una pelicula")
        update_movie()
    elif option == 6:
        print("Has seleccionado salir")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

