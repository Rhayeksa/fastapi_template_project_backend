from typing import Optional
from fastapi import APIRouter, Body

from src.config.database import session
from src.config.response import response

router = APIRouter()


@router.put(
    path="/{id}",
    name="update pengguna by id",
    description="api for update pengguna by id",
)
async def update_by_id(
    id: int,
    name: str = Body(""),
    description: str = Body(""),
):
    try:
        query = session.execute(
            f"""
            SELECT
                name,
                description
            FROM pengguna WHERE id = :id
            """,
            {"id": id}
        ).fetchall()

        if len(query) < 1:
            code = 404
            message = f"Data with ID {id} not found"
        elif len(query) > 1:
            code = 409
            message = f"Data with ID {id} duplicate"
        else:
            if name in [None, ""]:
                name = query[0]["name"]
            if description in [None, ""]:
                description = query[0]["description"]

            session.execute(
                """
                UPDATE pengguna
                SET
                    name = :name,
                    description = :description,
                    updated_at = now()
                WHERE id = :id
                """,
                {
                    "id": id,
                    "name": name,
                    "description": description,
                }
            )
            code = 200
            message = f"Data with ID {id} successfully updated"

        session.commit()
        return await response(code=code, message=message)
    except Exception as e:
        session.rollback()
        print("\n", str(e), "\n")
        return await response(code=500)
    finally:
        session.close()
