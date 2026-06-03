from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()


class JSONManager:

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

        return jwt.encode(
            payload,
            JSONManager.SECRET_KEY,
            algorithm=JSONManager.ALGORITHM
        )

    @staticmethod
    def verify_token(token):

        return jwt.decode(
            token,
            JSONManager.SECRET_KEY,
            algorithms=[
                JSONManager.ALGORITHM
            ]
        )