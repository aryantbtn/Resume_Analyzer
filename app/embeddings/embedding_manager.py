from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)


class EmbeddingManager:

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    @classmethod
    def generate_embedding(
        cls,
        text
    ):

        return cls.model.encode(
            text
        )

    @classmethod
    def similarity_score(
        cls,
        text1,
        text2
    ):

        embedding1 = (
            cls.generate_embedding(
                text1
            )
        )

        embedding2 = (
            cls.generate_embedding(
                text2
            )
        )

        similarity = cosine_similarity(
            [embedding1],
            [embedding2]
        )[0][0]

        return float(
            similarity
        )