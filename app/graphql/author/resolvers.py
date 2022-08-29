from typing import Optional
from uuid import UUID

from sqlalchemy import select, delete
from sqlalchemy.orm import sessionmaker

from app.core.utils import unpack_row
from app.graphql.author.inputs import AuthorCreateInput, AuthorUpdateInput
from app.graphql.validators import validate_email
from app.author.models import Author


async def get_author(author_id: UUID, session_maker: sessionmaker) -> Optional[Author]:
    async with session_maker() as session:
        statement = select(Author).where(Author.id == author_id)
        result = await session.execute(statement=statement)
    return result.scalar_one_or_none()


async def get_author_by(
        session_maker: sessionmaker,
        email: str = None,
        exclude_id: UUID = None,
) -> Author or None:
    statement = select(Author)
    if not email:
        return None

    if email:
        statement = statement.where(Author.email == email)

    if exclude_id:
        statement = statement.where(Author.id != exclude_id)

    async with session_maker() as session:
        result = await session.execute(statement=statement)
    return result.scalar_one_or_none()


async def get_authors(session_maker: sessionmaker) -> list[Author]:
    statement = select(Author)
    async with session_maker() as session:
        result = await session.execute(statement=statement)
    return unpack_row(rows=result, object_name=Author.__name__)


async def create_author(author_create_input: AuthorCreateInput, session_maker: sessionmaker) -> Author:
    if author_create_input.email and not validate_email(author_create_input.email):
        raise Exception('Email is invalid!')

    author = await get_author_by(email=author_create_input.email, session_maker=session_maker)
    if author:
        raise Exception(f'Author with email {author_create_input.email} existed!')

    values = dict(vars(author_create_input))
    author = Author(**values)
    async with session_maker() as session:
        session.add(author)
        await session.commit()
        await session.refresh(author)

    return author


async def update_author(author_id: UUID, author_update_input: AuthorUpdateInput, session_maker: sessionmaker) -> author:
    if author_update_input.email:
        if not validate_email(author_update_input.email):
            raise Exception('Email is invalid!')

        if await get_author_by(session_maker=session_maker, email=author_update_input.email, exclude_id=author_id):
            raise Exception('Email is used by another author!')

    author = await get_author(author_id=author_id, session_maker=session_maker)
    if not author:
        raise Exception('Author has not been found!')

    values = dict(vars(author_update_input))

    for k, v in values.items():
        if v:
            setattr(author, k, v)

    async with session_maker() as session:
        session.add(author)
        await session.commit()
        await session.refresh(author)

    return author


async def delete_author(author_id: UUID, session_maker: sessionmaker) -> bool:
    statement = delete(Author).where(Author.id == author_id)
    async with session_maker() as session:
        await session.execute(statement=statement)
        await session.commit()

    return True
