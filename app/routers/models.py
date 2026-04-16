from typing import Any
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from app.config import MyAppConfig
from app.routers.schemas import ChatModelsList, TokenPayload
from app.services.model_service import ModelService
from app.utils.response import (
    ResponseModel,
    StandardResponse,
    success_response,
)
from app.db.phsql import get_session

models_router = APIRouter(
    prefix=f"{MyAppConfig.API_BASE_URL}/{MyAppConfig.APP_VERSION}/models",
    tags=["model"],
)

model_service = ModelService()


@models_router.post("/add", response_model=ResponseModel[ChatModelsList])
async def add_model(model: ChatModelsList, session: Session = Depends(get_session)):
    return success_response(model_service.add_model(session=session, model=model))


@models_router.get("/list", response_model=ResponseModel[list[ChatModelsList]])
async def list_models(session: Session = Depends(get_session)):
    return success_response(model_service.list_models(session=session))


@models_router.post("/token", response_model=ResponseModel[str])
async def get_token(model: TokenPayload):
    return success_response(model_service.get_token(model.model_dump()))


@models_router.get("/analysis", response_model=ResponseModel[dict[str, Any]])
async def analysis_token(token: str = Query(default=...)) -> StandardResponse:
    return success_response(data=model_service.analysis_token(token))
