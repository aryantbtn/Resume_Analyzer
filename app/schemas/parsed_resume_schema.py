from pydantic import BaseModel


class ParsedResumeResponse(
    BaseModel
):

    name: str | None
    email: str | None
    phone: str | None