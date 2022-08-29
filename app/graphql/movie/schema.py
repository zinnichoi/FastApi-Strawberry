from typing import Optional
from uuid import UUID

import strawberry
from strawberry.types import Info

from app.movie.models import Movie
from app.graphql.movie.inputs import MovieCreateInput, MovieUpdateInput
from app.graphql.movie.resolvers import get_movies, get_movie, create_movie, update_movie, delete_movie


@strawberry.type
class MovieQueries:
    @strawberry.field
    async def movies(self, info: Info) -> list[Movie]:
        return await get_movies(session_maker=info.context.get('session'))

    @strawberry.field
    async def movie(self, info: Info, movie_id: UUID) -> Optional[Movie]:
        return await get_movie(movie_id=movie_id, session_maker=info.context.get('session'))


@strawberry.type
class MovieMutations:
    @strawberry.mutation
    async def movie_create(self, info: Info, movie_create_input: MovieCreateInput) -> Movie:
        return await create_movie(movie_create_input=movie_create_input, session_maker=info.context.get('session'))

    @strawberry.mutation
    async def movie_update(self, info: Info, movie_id: UUID, movie_update_input: MovieUpdateInput) -> Movie:
        return await update_movie(
            movie_id=movie_id,
            movie_update_input=movie_update_input,
            session_maker=info.context.get('session'),
        )

    @strawberry.mutation
    async def movie_delete(self, info: Info, movie_id: UUID) -> bool:
        return await delete_movie(movie_id=movie_id, session_maker=info.context.get('session'))
