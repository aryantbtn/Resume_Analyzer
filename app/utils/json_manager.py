from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()


class JWTManager:

    SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY"
    )

    ALGORITHM = os.getenv(
        "JWT_ALGORITHM"
    )

    @staticmethod
    def create_token(data: dict):

        payload = data.copy()

        expire = datetime.utcnow() + timedelta(
            minutes=60
        )

        payload["exp"] = expire

        token = jwt.encode(
            payload,
            JWTManager.SECRET_KEY,
            algorithm=JWTManager.ALGORITHM
        )

        return token

    @staticmethod
    def verify_token(token):

        return jwt.decode(
            token,
            JWTManager.SECRET_KEY,
            algorithms=[
                JWTManager.ALGORITHM
            ]
        )