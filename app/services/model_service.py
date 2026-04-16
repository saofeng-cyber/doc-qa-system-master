from typing import Any
from app.db.model import UserModel
from sqlmodel import Session, select
from app.routers.schemas import ChatModelsList
from app.utils.jwt import create_access_token, decode_token


class ModelService:
    def add_model(self, session: Session, model: ChatModelsList):
        user_model = UserModel(**model.model_dump())
        session.add(user_model)
        session.commit()
        session.refresh(user_model)
        return user_model

    def list_models(self, session: Session):
        return session.exec(select(UserModel)).all()

    def get_token(self, payload: dict[str, Any]):
        return create_access_token(user_data=payload)

    def analysis_token(self, token: str):
        return decode_token(token)
