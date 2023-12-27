from datetime import datetime, timedelta
from jose import jwt
from core.config import settings

def create_access_token(data: dict, expired_time:timedelta|None = None):
    to_encode = data.copy()
    if expired_time:
        expire = datetime.utcnow() + expired_time
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGRITHM)
    return encoded_jwt
