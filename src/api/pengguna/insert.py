from typing import Optional

from fastapi import APIRouter

from src.config.database import session
from src.config.response import response

router = APIRouter()


@router.post(
    path="/",
    name="insert pengguna",
    description="api for insert into pengguna",
)
async def insert(
    name: str,
    description: Optional[str] = None,
):
    try:
        session.execute(
            """
            INSERT INTO pengguna
            SET
                name = :name,
                description = :description,
                created_at = now(),
                updated_at = now()
            """,
            {
                "name": name,
                "description": description,
            }
        )

        session.commit()
        return await response(code=201)
    except Exception as e:
        session.rollback()
        print("\n", str(e), "\n")
        return await response(code=500)
    finally:
        session.close()
