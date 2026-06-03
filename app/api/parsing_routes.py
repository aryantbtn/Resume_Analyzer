from fastapi import (
    APIRouter,
    HTTPException
)

from app.repositories.resume_repository import (
    ResumeRepository
)

from app.services.parsing_service import (
    ParsingService
)

from app.repositories.parsed_resume_repository import (
    ParsedResumeRepository
)

router = APIRouter(
    prefix="/parse",
    tags=["Parsing"]
)


@router.post(
    "/resume/{resume_id}"
)
def parse_resume(
    resume_id: int
):

    resume = (
        ResumeRepository
        .get_resume_by_id(
            resume_id
        )
    )

    if not resume:

        raise HTTPException(
            status_code=404,
            detail="Resume Not Found"
        )

    full_text, parsed_data = (
        ParsingService.parse_resume(
            resume[
                "stored_filename"
            ]
        )
    )

    parsed_resume_id = (
        ParsedResumeRepository
        .save_parsed_resume(
            resume_id,
            full_text,
            parsed_data
        )
    )

    return {

        "success": True,

        "parsed_resume_id":
            parsed_resume_id,

        "parsed_data":
            parsed_data
    }

@router.get(
    "/resume/{resume_id}"
)
def get_parsed_resume(
    resume_id: int
):

    result = (
        ParsedResumeRepository
        .get_parsed_resume(
            resume_id
        )
    )

    if not result:

        raise HTTPException(
            status_code=404,
            detail="Parsed Resume Not Found"
        )

    return result