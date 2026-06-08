from app.embeddings.embedding_manager import (
    EmbeddingManager
)

class MatchingService:

    @staticmethod
    def keyword_skill_score(resume_skills, jd_skills):

        if not jd_skills:

            return 0

        matched = len(

            set(
                skill.lower()
                for skill
                in resume_skills
            )

            &

            set(
                skill.lower()
                for skill
                in jd_skills
            )
        )

        return (
            matched
            /
            len(jd_skills)
        ) * 100

    @staticmethod
    def embedding_skill_score(resume_skills, jd_skills):
        resume_text = " ".join(
            resume_skills
        )

        jd_text = " ".join(
            jd_skills
        )

        similarity = (
            EmbeddingManager
            .similarity_score(
                resume_text,
                jd_text
            )
        )
        return similarity*100

    # HELPER function for SCORING
    @staticmethod
    def calculate_experience_score(resume_exp, jd_exp):
        return round(
            EmbeddingManager.similarity_score(
                str(resume_exp),
                str(jd_exp)
            ) * 100,
            2
        )

    @staticmethod
    def calculate_projects_score(resume_projects, jd_projects):
        resume_text = " ".join(map(str, resume_projects))

        jd_text = " ".join(map(str, jd_projects))

        return round(
            EmbeddingManager.similarity_score(
                resume_text,
                jd_text
            ) * 100,
            2
        )

    @staticmethod
    def calculate_education_score(resume_education, jd_education):
        resume_education = str(
            resume_education
        ).lower()

        jd_education = str(jd_education).lower()

        if ("bachelor" in jd_education and ("b.tech" in resume_education or "bachelor" in resume_education)):
            return 100

        return 50

    @staticmethod
    def hybrid_skill_score(
        resume_skills,
        jd_skills
    ):

        keyword_score = (
            MatchingService
            .keyword_skill_score(
                resume_skills,
                jd_skills
            )
        )

        embedding_score = (
            MatchingService
            .embedding_skill_score(
                resume_skills,
                jd_skills
            )
        )

        return {

            "keyword_score":
                round(
                    keyword_score,
                    2
                ),

            "embedding_score":
                round(
                    embedding_score,
                    2
                ),

            "hybrid_score":
                round(
                    (
                        keyword_score
                        +
                        embedding_score
                    )
                    /
                    2,
                    2
                )
        }