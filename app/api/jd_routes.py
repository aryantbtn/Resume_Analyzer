from fastapi import (
    APIRouter,
    Depends
)

from app.schemas.jd_schema import (
    JDRequest
)

from app.repositories.jd_repository import (
    JDRepository
)

from app.repositories.parsed_jd_repository import (
    ParsedJDRepository
)

from app.services.jd_service import (
    JDService
)

from app.utils.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/jd",
    tags=["Job Description"]
)


@router.post(
    "/create"
)
def create_jd(
    request: JDRequest,
    user=Depends(
        get_current_user
    )
):

    jd_id = (
        JDRepository.create_jd(
            user["user_id"],
            request.title,
            request.description
        )
    )

    parsed_data = (
        JDService.parse_jd(
            request.description
        )
    )

    parsed_jd_id = (
        ParsedJDRepository
        .save_parsed_jd(
            jd_id,
            parsed_data
        )
    )

    return {

        "success": True,

        "jd_id": jd_id,

        "parsed_jd_id":
            parsed_jd_id,

        "parsed_data":
            parsed_data
    }