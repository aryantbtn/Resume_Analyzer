from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.auth_schema import (
    RegisterRequest,
    LoginRequest
)

from app.services.auth_services import (
    AuthService
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: RegisterRequest
):

    try:

        user_id = (
            AuthService.register_user(
                request
            )
        )

        return {
            "success": True,
            "user_id": user_id
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/login")
def login(
    request: LoginRequest
):

    try:

        token = (
            AuthService.login_user(
                request
            )
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )