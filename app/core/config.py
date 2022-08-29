from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool
    project_name: str
    version: str
    db_async_connection_str: str
    db_async_test_connection_str: str
