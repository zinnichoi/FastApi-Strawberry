from sqlalchemy import Column, ForeignKey
from sqlmodel import Field, SQLModel, Relationship

from app.author.models import Author


class Movie(SQLModel, table=True):
    __tablename__ = 'movie'
    id: int = Field(primary_key=True, index=True, nullable=False, )
    name: str = Field(nullable=False)
    genres: str = Field(nullable=False)
    author_id: int = Field(nullable=False, sa_column=Column(ForeignKey('users.id', ondelete='CASCADE')))
    author: Author = Relationship(back_populates='movies', sa_relationship_kwargs={'lazy': 'selectin'})
