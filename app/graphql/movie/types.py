import strawberry

from app.movie import models
from app.graphql.author.types import Author


@strawberry.type
class Movie:
    id: int
    name: str
    genres: str
    author_id: int
    author: Author

    @classmethod
    def from_instance(cls, instance: models.Movie):
        return cls(
            instance=instance,
            id=instance.id,
            name=instance.name,
            genres=instance.genres,
            author_id=instance.author_id,
            author=instance.author,
        )
