from enum import Enum
from typing import Any, ClassVar
from langchain_core.messages import AnyMessage
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class ModelConfig(BaseModel):
    """模型配置"""

    modelName: str = Field(..., description="模型名称")
    provider: str = Field("openai", description="模型提供方")
    baseUrl: str = Field(..., description="模型基础URL")
    apiKey: str = Field(..., description="模型API密钥")


class ModelSource(str, Enum):
    """模型来源"""

    default = "default"
    custom = "custom"


class ChatModelsList(ModelConfig):
    """模型列表"""

    id: str = Field(description="模型ID")
    modelSource: ModelSource = Field(description="模型来源")
    createdAt: datetime = Field(description="创建时间")
    updatedAt: datetime = Field(description="更新时间")
    model_config: ClassVar[ConfigDict] = ConfigDict(from_attributes=True, extra="allow")


class TokenPayload(BaseModel):
    """令牌载荷"""

    username: str = Field(..., description="用户名")
    model: str = Field(..., description="模型名称")


class FunctionDefinition(BaseModel):
    """函数定义"""

    name: str
    description: str
    parameters: dict[str, Any]


class ChatRequest(BaseModel):
    """聊天请求"""

    model: str = Field(..., description="模型名称")
    messages: list[AnyMessage] = Field(..., description="对话历史")
    temperature: float | None = Field(0.7, ge=0.0, le=2.0, description="温度参数")
    top_p: float | None = Field(0.95, ge=0.0, le=1.0, description="核采样参数")
    max_tokens: int | None = Field(1024, ge=1, description="最大生成长度")
    presence_penalty: float | None = Field(0.0, ge=-2.0, le=2.0, description="存在惩罚")
    frequency_penalty: float | None = Field(
        0.0, ge=-2.0, le=2.0, description="频率惩罚"
    )
    functions: list[FunctionDefinition] | None = Field(None, description="可用函数列表")
    function_call: str | dict[str, Any] | None = Field(None, description="函数调用策略")
    stream: bool | None = Field(False, description="是否流式响应")
    stop: str | list[str] | None = Field(None, description="停止词")
