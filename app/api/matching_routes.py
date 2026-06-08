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

from app.services.scoring_service import (
    ScoringService
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
    print("PHASE 7 ROUTE EXECUTED")

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

    experience_score = (
        MatchingService
        .calculate_experience_score(
            resume_data.get(
                "experience",
                []
            ),
            jd_data.get(
                "experience",
                []
            )
        )
    )

    projects_score = (
        MatchingService
        .calculate_projects_score(
            resume_data.get(
                "projects",
                []
            ),
            jd_data.get(
                "projects",
                []
            )
        )
    )

    education_score = (
        MatchingService
        .calculate_education_score(
            resume_data.get(
                "education",
                ""
            ),
            jd_data.get(
                "education",
                ""
            )
        )
    )

    overall_score = (
        ScoringService
        .calculate_overall_score(
            skill_scores[
                "hybrid_score"
            ],
            experience_score,
            projects_score,
            education_score
        )
    )

    return {
        "resume_id": resume_id,
        "jd_id": jd_id,
        "overall_score": overall_score,
        "section_scores": {
            "skills": skill_scores["hybrid_score"],
            "experience": experience_score,
            "projects": projects_score,
            "education": education_score
        }
    }