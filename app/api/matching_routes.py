from fastapi import (
    APIRouter,
    HTTPException
)

from app.repositories.parsed_resume_repository import (
    ParsedResumeRepository
)

from app.repositories.parsed_jd_repository import (
    ParsedJDRepository
)

from app.services.matching_services import (
    MatchingService
)

router = APIRouter(
    prefix="/match",
    tags=["Matching"]
)


@router.get(
    "/{resume_id}/{jd_id}"
)
def match_resume_jd(
    resume_id,
    jd_id
):

    resume = (
        ParsedResumeRepository
        .get_parsed_resume(
            resume_id
        )
    )

    jd = (
        ParsedJDRepository
        .get_parsed_jd(
            jd_id
        )
    )

    if not resume:

        raise HTTPException(
            status_code=404,
            detail="Resume Not Found"
        )

    if not jd:

        raise HTTPException(
            status_code=404,
            detail="JD Not Found"
        )

    resume_data = (
        resume[
            "parsed_json"
        ]
    )

    jd_data = (
        jd[
            "parsed_json"
        ]
    )

    skill_scores = (
        MatchingService
        .hybrid_skill_score(
            resume_data[
                "skills"
            ],
            jd_data[
                "skills"
            ]
        )
    )

    return {

        "resume_id":
            resume_id,

        "jd_id":
            jd_id,

        "skills":
            skill_scores
    }