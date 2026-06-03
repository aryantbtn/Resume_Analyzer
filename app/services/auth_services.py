from app.repositories.user_repository import UserRepository
from app.utils.hashing import PasswordHasher
from app.utils.json_manager import JSONManager


class AuthService:

    @staticmethod
    def register_user(data):

        existing_user = (
            UserRepository.get_user_by_email(
                data.email
            )
        )

        if existing_user:

            raise Exception(
                "User already exists"
            )

        print("Email:", data.email)
        print("Password:", data.password)
        print("Length:", len(data.password))

        hashed_password = (
            PasswordHasher.hash_password(
                data.password
            )
        )

        print("Hash Generated:", hashed_password)

        user_id = (
            UserRepository.create_user(
                data.full_name,
                data.email,
                hashed_password
            )
        )

        return user_id

    @staticmethod
    def login_user(data):

        user = (
            UserRepository.get_user_by_email(
                data.email
            )
        )

        if not user:

            raise Exception(
                "Invalid Credentials"
            )

        is_valid = (
            PasswordHasher.verify_password(
                data.password,
                user["password_hash"]
            )
        )

        if not is_valid:

            raise Exception(
                "Invalid Credentials"
            )

        token = (
            JSONManager.create_token(
                {
                    "user_id": user["id"],
                    "email": user["email"]
                }
            )
        )

        return token