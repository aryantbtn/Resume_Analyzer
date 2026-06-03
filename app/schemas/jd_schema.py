from pydantic import BaseModel


class JDRequest(
    BaseModel
):

    title: str

    description: str