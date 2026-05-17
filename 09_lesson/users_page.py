from typing import Optional

from sqlalchemy import text
from sqlalchemy.engine import Engine, Row

from db_config import get_engine


class UsersTable:
    """Обёртка над таблицей users."""

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def create_user(self, user_id: int, email: str, subject_id: int) -> None:
        query = text(
            "insert into users (user_id, user_email, subject_id) "
            "values (:user_id, :user_email, :subject_id)"
        )
        with self.engine.begin() as conn:
            conn.execute(
                query,
                {
                    "user_id": user_id,
                    "user_email": email,
                    "subject_id": subject_id,
                },
            )

    def get_user(self, user_id: int) -> Optional[Row]:
        query = text(
            "select user_id, user_email, subject_id "
            "from users where user_id = :user_id"
        )
        with self.engine.connect() as conn:
            return conn.execute(
                query, {"user_id": user_id}
            ).fetchone()

    def update_user_email(self, user_id: int, new_email: str) -> None:
        query = text(
            "update users "
            "set user_email = :user_email "
            "where user_id = :user_id"
        )
        with self.engine.begin() as conn:
            conn.execute(
                query,
                {"user_email": new_email, "user_id": user_id},
            )

    def delete_user(self, user_id: int) -> None:
        query = text(
            "delete from users where user_id = :user_id"
        )
        with self.engine.begin() as conn:
            conn.execute(query, {"user_id": user_id})

    def get_max_user_id(self) -> int:
        """Вернуть макс. user_id в таблице (или 0, если таблица пуста)."""
        query = text(
            "select coalesce(max(user_id), 0) as max_id "
            "from users"
        )
        with self.engine.connect() as conn:
            row = conn.execute(query).fetchone()
            return int(row.max_id)


def get_users_page() -> UsersTable:
    engine = get_engine()
    return UsersTable(engine)
