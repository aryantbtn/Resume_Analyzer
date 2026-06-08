from app.embeddings.embedding_manager import (
    EmbeddingManager
)


class MatchingService:

    @staticmethod
    def keyword_skill_score(
        resume_skills,
        jd_skills
    ):

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
    def embedding_skill_score(
        resume_skills,
        jd_skills
    ):

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

        return similarity * 100

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