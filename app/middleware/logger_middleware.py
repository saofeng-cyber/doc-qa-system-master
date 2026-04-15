from fastapi import FastAPI
from fastapi.requests import Request
import uuid
import time
from app.utils import logger


def apply_logger_middleware(app: FastAPI):
    @app.middleware(middleware_type="http")
    async def load_log(request: Request, call_next):
        """HTTP请求日志中间件"""
        # 生成请求ID用于追踪
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        # 记录请求开始时间
        start_time = time.time()
        # 记录请求信息
        logger.info(
            f"Request started | ID: {request_id} | "
            f"Method: {request.method} | Path: {request.url.path} | "
            f"Client: {request.client.host if request.client else 'unknown'}"
        )
        try:
            # 处理请求
            response = await call_next(request)

            # 计算处理时间
            process_time = time.time() - start_time

            # 记录响应信息
            logger.info(
                f"Request completed | ID: {request_id} | "
                f"Status: {response.status_code} | "
                f"Duration: {process_time:.3f}s"
            )

            # 添加自定义响应头
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Process-Time"] = str(process_time)

            return response

        except Exception as e:
            # 记录异常信息
            logger.error(
                f"Request failed | ID: {request_id} | "
                f"Error: {str(e)} | "
                f"Duration: {time.time() - start_time:.3f}s",
                exc_info=True
            )
            raise