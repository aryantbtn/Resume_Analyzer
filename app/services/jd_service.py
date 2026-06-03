from app.parsers.jd_parser import (
    JDParser
)


class JDService:

    @staticmethod
    def parse_jd(
        jd_text
    ):

        parsed_data = {

            "skills":
                JDParser.extract_skills(
                    jd_text
                ),

            "experience":
                JDParser.extract_experience(
                    jd_text
                ),

            "education":
                JDParser.extract_education(
                    jd_text
                )
        }

        return parsed_data