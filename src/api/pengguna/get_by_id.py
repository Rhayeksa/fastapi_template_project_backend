from fastapi import APIRouter

from src.config.database import session
from src.config.response import response

router = APIRouter()


@router.get(
    path="/{id}",
    name="get pengguna by id",
    description="api for get from pengguna by id",
)
async def get_by_id(
    id: int,
):
    try:
        data = session.execute(
            f"""
            SELECT * FROM pengguna WHERE id = :id
            """,
            {"id": id}
        ).fetchall()

        code = 404 if len(data) <= 0 else 200
        message = f"Data with ID {id} not found" if len(data) <= 0 else None
        data = None if len(data) <= 0 else data

        session.commit()
        return await response(code=code, message=message, data=data)
    except Exception as e:
        session.rollback()
        print("\n", str(e), "\n")
        return await response(code=500)
    finally:
        session.close()
