from app.config import MyAppConfig
from typing import Any


class ModelService:
    def __init__(self):
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def list_models(self) -> list:
        models = MyAppConfig.AVAILABLE_MODELS.split(",")
        print(MyAppConfig.AVAILABLE_MODELS)
        provider = MyAppConfig.MODEL_PROVIDER
        result = []
        for item in models:
            model = item.strip()
            result.append({"id": model, "model_name": model, "provider": provider})
        return result
