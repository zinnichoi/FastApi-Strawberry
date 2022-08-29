from typing import Optional
from uuid import UUID

from sqlalchemy import select, delete
from sqlalchemy.orm import sessionmaker

from app.core.utils import unpack_row
from app.graphql.movie.inputs import MovieCreateInput, MovieUpdateInput
from app.movie.models import Movie


async def get_movie(movie_id: UUID, session_maker: sessionmaker) -> Optional[Movie]:
    async with session_maker() as session:
        statement = select(Movie).where(Movie.id == movie_id)
        result = await session.execute(statement=statement)
    return result.scalar_one_or_none()


async def get_movies(session_maker: sessionmaker) -> list[Movie]:
    statement = select(Movie)
    async with session_maker() as session:
        result = await session.execute(statement=statement)
    return unpack_row(rows=result, object_name=Movie.__name__)


async def create_movie(movie_create_input: MovieCreateInput, session_maker: sessionmaker) -> Movie:
    values = dict(vars(movie_create_input))
    movie = Movie(**values)
    async with session_maker() as session:
        session.add(movie)
        await session.commit()
        await session.refresh(movie)

    return movie


async def update_movie(movie_id: UUID, movie_update_input: MovieUpdateInput, session_maker: sessionmaker) -> Movie:
    movie = await get_movie(movie_id=movie_id, session_maker=session_maker)
    if not movie:
        raise Exception('Movie has not been found!')

    values = dict(vars(movie_update_input))

    for k, v in values.items():
        if v:
            setattr(movie, k, v)

    async with session_maker() as session:
        session.add(movie)
        await session.commit()
        await session.refresh(movie)

    return movie


async def delete_movie(movie_id: UUID, session_maker: sessionmaker) -> bool:
    statement = delete(Movie).where(Movie.id == movie_id)
    async with session_maker() as session:
        await session.execute(statement=statement)
        await session.commit()

    return True
