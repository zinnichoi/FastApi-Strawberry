from datetime import date
from typing import Optional

import strawberry

from app.author import models


@strawberry.type
class Author:
    id: int
    name: str
    email: str
    birthdate: date
    gender: str
    address: Optional[str]

    @classmethod
    def from_instance(cls, instance: models.Author):
        return cls(
            instance=instance,
            id=instance.id,
            name=instance.name,
            email=instance.email,
            birthdate=instance.birthdate,
            gender=instance.gender,
            address=instance.address,
        )
