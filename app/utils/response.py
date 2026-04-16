from fastapi import HTTPException, status
from pydantic import BaseModel
from typing import Any, TypeVar, Generic


class StandardResponse(BaseModel):
    code: int = 200
    message: str = "success"
    data: Any = None


class ErrorResponse(HTTPException):
    def __init__(
        self,
        data: Any = None,
        message: str = "failed",
        code: int = status.HTTP_400_BAD_REQUEST,
    ):
        super().__init__(status_code=code, detail=message)
        self.code = code
        self.message = message
        self.data = data


def success_response(data: Any = None, message: str = "success", code: int = 200):
    return StandardResponse(code=code, message=message, data=data)


# 定义一个类型变量 T
DataT = TypeVar("DataT")


# 通用响应基类
class ResponseModel(BaseModel, Generic[DataT]):
    code: int = 200
    message: str = "success"
    data: DataT | None = None
