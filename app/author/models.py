from typing import Optional
from datetime import date
from pydantic import EmailStr
from sqlmodel import Field, SQLModel, Relationship


class Author(SQLModel, table=True):
    __tablename__ = 'author'
    id: int = Field(primary_key=True, index=True, nullable=False)
    name: str = Field(nullable=False)
    email: EmailStr = Field(nullable=False, sa_column_kwargs={'unique': True})
    birthdate: date = Field(nullable=False)
    gender: str
    address: Optional[str]
    movies: Optional[list['Movie']] = Relationship(
        back_populates='author',
        sa_relationship_kwargs={'lazy': 'selectin', 'cascade': 'delete'}
    )
