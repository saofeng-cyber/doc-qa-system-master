import uuid
from datetime import datetime
from typing import ClassVar
from sqlmodel import SQLModel, Field

class UserModel(SQLModel, table=True):
    __tablename__: ClassVar[str] = "model"
    
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        max_length=36
    )
    modelName: str = Field(nullable=False, max_length=255, alias="model_name")
    provider: str = Field(nullable=False, max_length=100)
    baseUrl: str = Field(nullable=False, max_length=500, alias="base_url")
    apiKey: str = Field(nullable=False, max_length=255, alias="api_key")
    modelSource: str = Field(nullable=False, max_length=100, alias="model_source")
    createdAt: datetime = Field(default_factory=datetime.now, alias="created_at")
    updatedAt: datetime = Field(default_factory=datetime.now, alias="updated_at")
    
    model_config = {"populate_by_name": True}  # 允许使用字段名或别名