from typing import Any
from app.db.model import UserModel
from sqlmodel import  Session, select
from app.routers.schemas import ChatModelsList


class ModelService:
    
    def add_model(self, session: Session, model: ChatModelsList):

        user_model = UserModel(**model.model_dump())

        session.add(user_model)

        session.commit()

        session.refresh(user_model)

        return user_model

    def list_models(self, session: Session):
        # models: list[ChatModelsList] = [
        #     ChatModelsList(
        #         modelName="deepseek-chat",
        #         provider="openai",
        #         baseUrl="https://api.deepseek.com/v1",
        #         apiKey="sk-ed7c607651294fea9f54cd245c048fc3",
        #     ),
        #     ChatModelsList(
        #         modelName="qwen3.5-27b",
        #         provider="openai",
        #         baseUrl="https://dashscope.aliyuncs.com/compatible-mode/v1",
        #         apiKey="sk-bb9e8f7f7cd14e0aade523eb7f1c4de6",
        #     ),
        # ]
        statement = select(UserModel)
        results = session.exec(statement)
        return results.all()