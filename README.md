# Catálogo de Películas

API REST y aplicación de consola para gestionar un catálogo de películas. Permite crear, consultar, actualizar y eliminar películas, con persistencia en PostgreSQL mediante SQLAlchemy.

Este proyecto nació como un ejercicio de práctica: partió de una versión con `sqlite3` y SQL escrito a mano, y fue migrado a SQLAlchemy 2.0 (ORM) y PostgreSQL ejecutándose en Docker.

## Características

- API REST con operaciones CRUD completas sobre películas.
- Validación de datos de entrada y salida con Pydantic.
- Documentación interactiva automática (Swagger UI) generada por FastAPI.
- Aplicación de consola (CLI) con menú que comparte la misma capa de datos que la API.
- Configuración de la base de datos mediante variables de entorno.

## Tecnologías

| Área | Tecnología |
|---|---|
| Lenguaje | Python 3.13 |
| API | FastAPI, Uvicorn |
| Validación | Pydantic v2 |
| ORM | SQLAlchemy 2.x |
| Base de datos | PostgreSQL 16 (Docker) |
| Driver | psycopg2 |
| Configuración | python-dotenv |

## Endpoints

Prefijo base: `/api/v1/movies`

| Método | Ruta | Descripción | Respuesta |
|---|---|---|---|
| GET | `/` | Lista todas las películas | 200 |
| POST | `/` | Crea una película | 201 |
| GET | `/{movie_id}` | Obtiene una película por ID | 200 / 404 |
| PUT | `/{movie_id}` | Actualiza los campos enviados | 200 / 404 |
| DELETE | `/{movie_id}` | Elimina una película | 204 / 404 |

Modelo de película:

```json
{
  "id": 1,
  "title": "Alien",
  "year": 1979,
  "genre": "Ciencia ficción"
}
```

## Requisitos

- Python 3.13
- Docker (para PostgreSQL)

## Instalación y ejecución

1. Crear y activar un entorno virtual, e instalar las dependencias: `fastapi`, `uvicorn`, `sqlalchemy`, `psycopg2-binary`, `python-dotenv`.
2. Levantar un contenedor de PostgreSQL y crear una base de datos llamada `movies`.
3. Crear un archivo `.env` en la raíz con la URL de conexión:

   ```
   DATABASE_URL=postgresql+psycopg2://USUARIO:CONTRASEÑA@localhost:5433/movies
   ```

4. Iniciar la API:

   ```
   uvicorn api:app --reload
   ```

   Documentación interactiva en `http://127.0.0.1:8000/docs`.

5. O bien iniciar la aplicación de consola:

   ```
   python main.py
   ```

Las tablas se crean automáticamente al arrancar.

## Estructura del proyecto

```
.
├── api.py              # Punto de entrada de la API (FastAPI)
├── main.py             # Punto de entrada de la aplicación de consola
└── app/
    ├── database.py     # Conexión, sesiones e inicialización de tablas
    ├── models.py       # Modelo SQLAlchemy (tabla movies)
    ├── schemas.py      # Esquemas Pydantic (entrada y salida)
    └── routes/
        └── movies.py   # Endpoints de películas
```

## Próximos pasos

- Migraciones de esquema con Alembic.
- Pruebas automáticas con pytest.
- Orquestación del entorno con Docker Compose.
