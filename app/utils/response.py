from pydantic import BaseModel
from typing import Optional, Any, TypeVar, Generic


class StandardResponse(BaseModel):
    code: int = 200
    message: str = "success"
    data: Optional[Any] = None


def success_response(data: Any = None, message: str = "success", code: int = 200):
    return StandardResponse(code=code, message=message, data=data)


def error_response(data: Any = None, message: str = "failed", code: int = 400):
    return StandardResponse(code=code, message=message, data=data)


# 定义一个类型变量 T
DataT = TypeVar("DataT")


# 通用响应基类
class ResponseModel(BaseModel, Generic[DataT]):
    code: int = 200
    message: str = "success"
    data: Optional[DataT] = None
