import math


async def pagination(
    currentPage: int,
    pageSize: int,
    totalData: int,
):
    for v in [currentPage, pageSize]:
        if v <= 0:
            return {"message": "pageSize, totalData and currentPage cannot be less than equal to 0"}
    return {
        "currentPage": currentPage,
        "pageSize": pageSize,
        "totalPage": math.ceil(totalData/pageSize),
        "totalData": totalData,
    }
