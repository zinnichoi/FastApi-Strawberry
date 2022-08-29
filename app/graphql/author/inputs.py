from datetime import date
from typing import Optional

import strawberry


@strawberry.input
class AuthorCreateInput:
    name: str
    email: str
    birthdate: date
    gender: str
    address: Optional[str] = None


@strawberry.input
class AuthorUpdateInput:
    name: Optional[str]
    email: Optional[str]
    birthdate: Optional[date]
    gender: Optional[str]
    address: Optional[str] = None
