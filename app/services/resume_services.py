import os
import uuid

from pydantic.v1.main import generate_hash_function

from app.utils.file_hashing import (
    FileHasher
)

from app.repositories.resume_repository import (
    ResumeRepository
)


class ResumeService:

    UPLOAD_DIR = "app/uploads"

    @staticmethod
    def upload_resume(
        file,
        user_id
    ):

        file_bytes = file.file.read()

        file_hash = (
            FileHasher.generate_hash(
                file_bytes
            )
        )

        existing_resume = (
            ResumeRepository
            .get_resume_by_hash(
                file_hash
            )
        )

        if existing_resume:

            raise Exception(
                "Duplicate Resume Detected"
            )

        extension = (
            file.filename.split(".")[-1]
        )

        stored_filename = (
            f"{uuid.uuid4()}.{extension}"
        )

        file_path = os.path.join(
            ResumeService.UPLOAD_DIR,
            stored_filename
        )

        with open(
            file_path,
            "wb"
        ) as resume_file:

            resume_file.write(
                file_bytes
            )

        resume_id = (
            ResumeRepository.save_resume(
                user_id,
                file.filename,
                stored_filename,
                file_hash
            )
        )

        return resume_id