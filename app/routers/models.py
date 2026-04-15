from fastapi import APIRouter
from app.config import MyAppConfig
from app.routers.schemas import ChatModelsList
from app.services.model_service import ModelService
from app.utils.response import ResponseModel, success_response, error_response
from typing import List

models_router = APIRouter(
    prefix=f"{MyAppConfig.API_BASE_URL}/{MyAppConfig.APP_VERSION}/models",
    tags=["model"],
)

model_service = ModelService()


@models_router.get("/list", response_model=ResponseModel[List[ChatModelsList]])
async def list_models() -> List[ChatModelsList]:
    try:
        models = model_service.list_models()
        return success_response(models)
    except Exception as e:
        return error_response(str(e))
