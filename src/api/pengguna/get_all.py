from typing import Optional

from fastapi import APIRouter

from src.config.database import session
from src.config.pagination import pagination
from src.config.response import response
from pydantic import BaseModel


router = APIRouter()


@router.get(
    path="/",
    name="get all pengguna",
    description="api for get all from pengguna",
)
async def get_all(
    pageNum: Optional[int] = None,
    pageSize: Optional[int] = None,
):
    try:
        pageSize = 5 if pageSize is None else pageSize
        pageNum = 1 if pageNum is None else pageNum

        data = session.execute(
            f"""
            SELECT * FROM pengguna LIMIT :limit OFFSET :offset
            """,
            {
                "limit": pageSize,
                "offset": (pageNum-1) * pageSize,
            }
        ).fetchall()

        rows = session.execute(
            """
            SELECT COUNT(1) 'rows' FROM pengguna
            """
        ).fetchall()[0]["rows"]

        session.commit()
        return await response(code=200, data=data, page=await pagination(currentPage=pageNum, pageSize=pageSize, totalData=rows))
    except Exception as e:
        session.rollback()
        print("\n", str(e), "\n")
        return await response(code=500)
    finally:
        session.close()
