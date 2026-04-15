from typing import Any, List
from app.routers.schemas import ChatModelsList


class ModelService:
    def __init__(self):
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def list_models(self) -> List[ChatModelsList]:
        models: List[ChatModelsList] = [
            ChatModelsList(
                modelName="deepseek-chat",
                provider="openai",
                baseUrl="https://api.deepseek.com/v1",
                apiKey="sk-ed7c607651294fea9f54cd245c048fc3",
            ),
            ChatModelsList(
                modelName="qwen3.5-27b",
                provider="openai",
                baseUrl="https://dashscope.aliyuncs.com/compatible-mode/v1",
                apiKey="sk-bb9e8f7f7cd14e0aade523eb7f1c4de6",
            ),
        ]
        return models
