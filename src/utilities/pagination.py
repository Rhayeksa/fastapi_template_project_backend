import math


async def pagination(pageSize: int, totalData: int, currentPage: int):
    return {
        "pageSize": pageSize,
        "totalData": totalData,
        "totalPage": math.ceil(totalData/pageSize),
        "currentPage": currentPage
    }
