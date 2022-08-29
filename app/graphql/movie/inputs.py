from typing import Optional

import strawberry


@strawberry.input
class MovieCreateInput:
    name: str
    genres: str
    author_id: int


@strawberry.input
class MovieUpdateInput:
    name: Optional[str]
    genres: Optional[str]
    author_id: Optional[int]
