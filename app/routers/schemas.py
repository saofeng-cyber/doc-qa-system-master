from enum import Enum
from typing import List, Optional, Union, Dict, Any
from langchain_core.messages import AnyMessage
from pydantic import BaseModel, Field
import uuid
from datetime import datetime


class ModelConfig(BaseModel):
    """模型配置"""

    modelName: str
    provider: str = Field("openai", description="模型提供方")
    baseUrl: str = Field(..., description="模型基础URL")
    apiKey: str = Field(..., description="模型API密钥")


class ModelSource(str, Enum):
    """模型来源"""

    default = "default"
    custom = "custom"


class ChatModelsList(ModelConfig):
    """模型列表"""

    id: str = Field(default=str(uuid.uuid4()), description="模型ID")
    modelSource: ModelSource = Field(
        default=ModelSource.default, description="模型来源"
    )
    createdAt: str = Field(default=datetime.now(), description="创建时间")
    updatedAt: str = Field(default=datetime.now(), description="更新时间")


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
