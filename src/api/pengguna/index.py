from fastapi import APIRouter

from src.api.pengguna.get_all import router as get_all
from src.api.pengguna.get_by_id import router as get_by_id
from src.api.pengguna.insert import router as insert
from src.api.pengguna.delete_by_id import router as delete_by_id
from src.api.pengguna.update_by_id import router as update_by_id

router = APIRouter(
    prefix="/pengguna",
    tags=["Pengguna"]
)

routes = [
    get_all,
    get_by_id,
    insert,
    delete_by_id,
    update_by_id,
]

for route in routes:
    router.include_router(route)
