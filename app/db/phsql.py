from sqlmodel import create_engine
from app.config import MyAppConfig
from sqlmodel import Session


engine = create_engine(MyAppConfig.DATABASE_URL, echo=MyAppConfig.DATABASE_ECHO)


def get_session():
    with Session(bind=engine) as session:
        yield session

