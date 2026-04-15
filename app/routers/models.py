from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config import MyAppConfig
from app.routers.schemas import ChatModelsList
from app.services.model_service import ModelService
from app.utils.response import ResponseModel, success_response, error_response
from app.db.phsql import get_session

models_router = APIRouter(
    prefix=f"{MyAppConfig.API_BASE_URL}/{MyAppConfig.APP_VERSION}/models",
    tags=["model"],
)

model_service = ModelService()

@models_router.post("/add", response_model=ResponseModel[ChatModelsList])


async def add_model(model: ChatModelsList, session: Session = Depends(get_session)):

    try:

        result = model_service.add_model(session=session, model=model)

        return success_response(result)

    except Exception as e:
        return error_response(str(e))


@models_router.get("/list", response_model=ResponseModel[list[ChatModelsList]])
async def list_models(session: Session = Depends(get_session)):
    try:
        models = model_service.list_models(session=session)
        return success_response(models)
    except Exception as e:
        return error_response(str(e))
