from typing import Any
import jwt
from app.config import MyAppConfig
from datetime import datetime, timedelta, timezone
import uuid

from app.utils.response import ErrorResponse

ACCESS_TOKEN_EXPIRE = 60


def create_access_token(
    user_data: dict[str, Any],
    expire: timedelta | None = None,
) -> str:
    """生成 JWT token"""
    expire_time = (
        expire if expire is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRE)
    )
    exp_datetime = datetime.now(timezone.utc) + expire_time
    return jwt.encode(
        payload={"user": user_data, "exp": exp_datetime, "jti": str(uuid.uuid4())},
        key=MyAppConfig.SECRET_KEY,
        algorithm=MyAppConfig.ALGORITHM,
        headers={"typ": "JWT"},
    )


def decode_token(token: str):
    try:
        token_data = jwt.decode(
            jwt=token, key=MyAppConfig.SECRET_KEY, algorithms=[MyAppConfig.ALGORITHM]
        )
        return token_data
    except jwt.ExpiredSignatureError:
        raise ErrorResponse(data="Token expired", code=401)
    except jwt.InvalidTokenError:
        raise ErrorResponse(data="Invalid token", code=401)
    except Exception as e:
        raise ErrorResponse(code=401, data=str(e))
