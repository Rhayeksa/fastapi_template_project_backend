from fastapi import APIRouter

from src.config.database import session
from src.config.response import response

router = APIRouter()


@router.delete(
    path="/{id}",
    name="delete pengguna by id",
    description="api for delete pengguna by id",
)
async def delete_by_id(
    id: int,
):
    try:
        query = session.execute(
            f"""
            SELECT * FROM pengguna WHERE id = :id
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
            session.execute(
                """
                DELETE FROM pengguna
                WHERE id = :id
                """,
                {"id": id}
            )
            code = 200
            message = f"Data with ID {id} successfully deleted"

        session.commit()
        return await response(code=code, message=message)
    except Exception as e:
        session.rollback()
        print("\n", str(e), "\n")
        return await response(code=500)
    finally:
        session.close()
