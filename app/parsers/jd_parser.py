import re


class JDParser:

    @staticmethod
    def extract_skills(
        text
    ):

        known_skills = [

            "python",
            "java",
            "c++",
            "sql",
            "mysql",
            "fastapi",
            "docker",
            "kubernetes",
            "aws",
            "git",
            "linux",
            "javascript",
            "react",
            "nodejs",
            "mongodb",
            "swift",
            "ios"
        ]

        text_lower = (
            text.lower()
        )

        skills = []

        for skill in known_skills:

            if skill in text_lower:

                skills.append(
                    skill
                )

        return list(
            set(skills)
        )

    @staticmethod
    def extract_experience(
        text
    ):

        match = re.search(
            r'(\d+)\+?\s*years?',
            text,
            re.IGNORECASE
        )

        if match:

            return (
                int(
                    match.group(1)
                )
            )

        return 0

    @staticmethod
    def extract_education(
        text
    ):

        education_keywords = [

            "b.tech",
            "bachelor",
            "master",
            "m.tech",
            "degree"
        ]

        results = []

        lower_text = (
            text.lower()
        )

        for item in education_keywords:

            if item in lower_text:

                results.append(
                    item
                )

        return results