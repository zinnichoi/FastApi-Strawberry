from typing import Optional
from uuid import UUID

import strawberry
from strawberry.types import Info

from app.author.models import Author
from app.graphql.author.inputs import AuthorCreateInput, AuthorUpdateInput
from app.graphql.author.resolvers import get_authors, get_author, create_author, update_author, delete_author


@strawberry.type
class AuthorQueries:
    @strawberry.field
    async def authors(self, info: Info) -> list[Author]:
        return await get_authors(session_maker=info.context.get('session'))

    @strawberry.field
    async def author(self, info: Info, author_id: UUID) -> Optional[Author]:
        return await get_author(author_id=author_id, session_maker=info.context.get('session'))


@strawberry.type
class AuthorMutations:
    @strawberry.mutation
    async def author_create(self, info: Info, author_create_input: AuthorCreateInput) -> Author:
        return await create_author(author_create_input=author_create_input, session_maker=info.context.get('session'))

    @strawberry.mutation
    async def author_update(self, info: Info, author_id: UUID, author_update_input: AuthorUpdateInput) -> Author:
        return await update_author(
            author_id=author_id,
            author_update_input=author_update_input,
            session_maker=info.context.get('session'),
        )

    @strawberry.mutation
    async def author_delete(self, info: Info, author_id: UUID) -> bool:
        return await delete_author(author_id=author_id, session_maker=info.context.get('session'))
