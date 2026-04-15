from pydantic import BaseModel


class UvicornConfig(BaseModel):
    app: str = "app.main:app"
    host: str = "0.0.0.0"
    port: int = 8080
    reload: bool = True
    workers: int = 1
    log_level: str = "info"
    access_log: bool = True
    timeout_keep_alive: int = 5


if __name__ == "__main__":
    import uvicorn

    config = UvicornConfig()
    uvicorn.run(
        app=config.app,
        host=config.host,
        port=config.port,
        reload=config.reload,
        log_level=config.log_level,
        access_log=config.access_log,
        timeout_keep_alive=config.timeout_keep_alive,
        workers=config.workers,
    )
