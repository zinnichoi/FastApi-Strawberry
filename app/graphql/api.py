import strawberry
from strawberry.extensions import Extension
from strawberry.tools import merge_types

from app.core.db import async_session
from app.graphql.movie.schema import (
    MovieQueries,
    MovieMutations,
)
from app.graphql.author.schema import (
    AuthorQueries,
    AuthorMutations,
)

Query = merge_types('SuperQuery', (
    MovieQueries,
    AuthorQueries,
))

Mutation = merge_types('SuperMutation', (
    MovieMutations,
    AuthorMutations,
))


class SQLAlchemySession(Extension):
    def on_request_start(self):
        self.execution_context.context['session'] = async_session


schema = strawberry.Schema(query=Query, mutation=Mutation, extensions=[SQLAlchemySession])
