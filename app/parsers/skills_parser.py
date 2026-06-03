import re


class SkillsParser:

    @staticmethod
    def extract_skills(
        skills_section
    ):

        skills = []

        lines = (
            skills_section.splitlines()
        )

        for line in lines:

            if ":" in line:

                _, values = (
                    line.split(
                        ":",
                        1
                    )
                )

                extracted = [

                    skill.strip()

                    for skill in values.split(
                        ","
                    )

                    if skill.strip()
                ]

                skills.extend(
                    extracted
                )

        return list(
            set(skills)
        )