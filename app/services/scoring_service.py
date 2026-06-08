class ScoringService:

    SKILLS_WEIGHT = 0.40

    EXPERIENCE_WEIGHT = 0.30

    PROJECTS_WEIGHT = 0.20

    EDUCATION_WEIGHT = 0.10

    @staticmethod
    def calculate_overall_score(

            skills_score,

            experience_score,

            projects_score,

            education_score
    ):

        overall_score = (

                skills_score *
                ScoringService.SKILLS_WEIGHT

                +

                experience_score *
                ScoringService.EXPERIENCE_WEIGHT

                +

                projects_score *
                ScoringService.PROJECTS_WEIGHT

                +

                education_score *
                ScoringService.EDUCATION_WEIGHT
        )

        return round(
            overall_score,
            2
        )