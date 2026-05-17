import os

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_db_connection_string() -> str:
    user = os.environ.get("DB_USER", "postgres")
    password = os.environ.get("DB_PASSWORD", "password")
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5432")
    db_name = os.environ.get("DB_NAME", "BASA_Date")

    return (
        f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    )


def get_engine() -> Engine:
    connection_string = get_db_connection_string()
    return create_engine(connection_string)
