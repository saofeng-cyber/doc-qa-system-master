from typing import Any, AsyncGenerator
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.phsql import engine
from sqlmodel import SQLModel
from app.middleware import apply_logger_middleware
from app.routers.models import models_router


@asynccontextmanager
async def lifespan(app: FastAPI | None) -> AsyncGenerator[None, Any]:
    if app is not None:
        print("应用启动")
        SQLModel.metadata.create_all(engine)
        print("数据库表创建完成")
        yield
        print("应用关闭")


app = FastAPI(lifespan=lifespan, description="RAG系统")
# 挂载静态文件目录
app.mount("/web", StaticFiles(directory="app/web"), name="web")
apply_logger_middleware(app)
# 包含模型路由
app.include_router(router=models_router)


@app.get("/")
async def read_root():
    return FileResponse("app/web/index.html")
