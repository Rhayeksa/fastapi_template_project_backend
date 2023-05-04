from typing import Optional

from fastapi import APIRouter

from src.config.response import response

router = APIRouter()


@router.get(
    path="/",
    name="api project todo",
    description="api project todo",
)
async def root(
    projectName: Optional[str] = None,
):
    data = f"{projectName} Project" if projectName != None else "TODO Project"

    return await response(code=200, data=data)
