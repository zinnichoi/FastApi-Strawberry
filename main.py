import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app import settings
from app.core.models import HealthCheck
from app.graphql.api import schema

app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    debug=settings.debug
)


@app.get("/", response_model=HealthCheck, tags=["status"])
async def health_check():
    return {
        "name": settings.project_name,
        "version": settings.version
    }

app.include_router(GraphQLRouter(schema=schema, graphiql=True), prefix="/graphql")

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True)
