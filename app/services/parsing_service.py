import os

from app.parsers.pdf_parser import (
    PDFParser
)

from app.parsers.section_parser import (
    SectionParser
)

from app.parsers.resume_section_parser import (
    ResumeSectionParser
)

from app.parsers.skills_parser import (
    SkillsParser
)

from app.parsers.project_parser import (
    ProjectParser
)

from app.parsers.experience_parser import (
    ExperienceParser
)

from app.parsers.education_parser import (
    EducationParser
)


class ParsingService:

    @staticmethod
    def parse_resume(
        stored_filename
    ):

        file_path = os.path.join(
            "app",
            "uploads",
            stored_filename
        )

        full_text = (
            PDFParser.extract_text(
                file_path
            )
        )

        skills_section = (
            ResumeSectionParser
            .extract_skills_section(
                full_text
            )
        )

        projects_section = (
            ResumeSectionParser
            .extract_projects_section(
                full_text
            )
        )

        experience_section = (
            ResumeSectionParser
            .extract_experience_section(
                full_text
            )
        )

        education_section = (
            ResumeSectionParser
            .extract_education_section(
                full_text
            )
        )

        parsed_data = {

            "name":
                SectionParser.extract_name(
                    full_text
                ),

            "email":
                SectionParser.extract_email(
                    full_text
                ),

            "phone":
                SectionParser.extract_phone(
                    full_text
                ),

            "skills":
                SkillsParser.extract_skills(
                    skills_section
                ),

            "projects":
                ProjectParser.extract_projects(
                    projects_section
                ),

            "experience":
                ExperienceParser.extract_experience(
                    experience_section
                ),

            "education":
                EducationParser.extract_education(
                    education_section
                )
        }

        return (
            full_text,
            parsed_data
        )