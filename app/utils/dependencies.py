from fastapi import Request
from langchain_core.language_models import BaseChatModel


async def get_llm_from_request(request: Request) -> BaseChatModel:
    """从请求中获取大模型客户端"""
    if not hasattr(request.app.state, "llm_client"):
        raise RuntimeError("大模型客户端未初始化")
    return request.app.state.llm_client
