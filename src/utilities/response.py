from datetime import datetime
from http import HTTPStatus
from typing import Optional

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


async def response(
    code: int,
    message: Optional[str] = None,
    page: Optional[dict] = None,
    data=None
):
    status = None
    try:
        code = HTTPStatus(code)
        status = code.phrase
    except Exception as e:
        print(f"\nError: {e}\n")
        message = str(e)
        data = None

    result = {
        "datetime": str(datetime.now()),
        "statusCode": code,
        "status": status,
        "statusMessage": message if message != None else status,
    }
    result.update({"page": page} if page != None else {})
    result.update({"data": jsonable_encoder(data)})

    try:
        code = HTTPStatus(code)
    except:
        code = 500

    return JSONResponse(result, code)
