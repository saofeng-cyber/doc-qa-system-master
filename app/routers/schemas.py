from typing import List, Optional, Union, Dict, Any
from langchain_core.messages import AnyMessage
from pydantic import BaseModel, Field


class ChatModelsList(BaseModel):
    """模型列表"""

    id: str
    model_name: str
    provider: str


class FunctionDefinition(BaseModel):
    """函数定义"""

    name: str
    description: str
    parameters: Dict[str, Any]


class ChatRequest(BaseModel):
    """聊天请求"""

    model: str = Field(..., description="模型名称")
    messages: List[AnyMessage] = Field(..., description="对话历史")
    temperature: Optional[float] = Field(0.7, ge=0.0, le=2.0, description="温度参数")
    top_p: Optional[float] = Field(0.95, ge=0.0, le=1.0, description="核采样参数")
    max_tokens: Optional[int] = Field(1024, ge=1, description="最大生成长度")
    presence_penalty: Optional[float] = Field(
        0.0, ge=-2.0, le=2.0, description="存在惩罚"
    )
    frequency_penalty: Optional[float] = Field(
        0.0, ge=-2.0, le=2.0, description="频率惩罚"
    )
    functions: Optional[List[FunctionDefinition]] = Field(
        None, description="可用函数列表"
    )
    function_call: Optional[Union[str, Dict[str, Any]]] = Field(
        None, description="函数调用策略"
    )
    stream: Optional[bool] = Field(False, description="是否流式响应")
    stop: Optional[Union[str, List[str]]] = Field(None, description="停止词")
