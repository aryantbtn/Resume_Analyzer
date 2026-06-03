import re


class ResumeSectionParser:

    @staticmethod
    def extract_section(
        text,
        start_keyword,
        end_keywords
    ):

        pattern = (
            rf"{start_keyword}(.*?)"
            rf"(?={'|'.join(end_keywords)}|$)"
        )

        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:

            return (
                match.group(1)
                .strip()
            )

        return ""

    @staticmethod
    def extract_skills_section(
        text
    ):

        return (
            ResumeSectionParser.extract_section(
                text,
                "Skills",
                [
                    "Extracurricular",
                    "Achievements",
                    "$"
                ]
            )
        )

    @staticmethod
    def extract_projects_section(
        text
    ):

        return (
            ResumeSectionParser.extract_section(
                text,
                "Projects",
                [
                    "Skills",
                    "Technical Skills",
                    "Extracurricular"
                ]
            )
        )

    @staticmethod
    def extract_experience_section(
        text
    ):

        return (
            ResumeSectionParser.extract_section(
                text,
                "Experience",
                [
                    "Projects",
                    "Skills"
                ]
            )
        )

    @staticmethod
    def extract_education_section(
        text
    ):

        return (
            ResumeSectionParser.extract_section(
                text,
                "Education",
                [
                    "Experience",
                    "Projects"
                ]
            )
        )