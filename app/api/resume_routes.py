from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from app.services.resume_services import (
    ResumeService
)

from app.utils.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
def upload_resume(
    file: UploadFile = File(...),
    user=Depends(
        get_current_user
    )
):

    try:

        resume_id = (
            ResumeService.upload_resume(
                file,
                user["user_id"]
            )
        )

        return {
            "success": True,
            "resume_id": resume_id
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )