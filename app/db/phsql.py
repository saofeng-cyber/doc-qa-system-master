from sqlmodel import create_engine, Session
from app.config import MyAppConfig
from fastapi import Depends
from typing import Annotated


engine = create_engine(MyAppConfig.DATABASE_URL, echo=MyAppConfig.DATABASE_ECHO)


async def get_session():
    async with Session(bind=engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
