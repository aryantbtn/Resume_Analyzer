from app.database.mysql_connection import (
    Database
)


class JDRepository:

    @staticmethod
    def create_jd(
        user_id,
        title,
        full_text
    ):

        conn = Database.get_connection()

        cursor = conn.cursor()

        query = """
        INSERT INTO
        job_descriptions
        (
            user_id,
            title,
            full_text
        )
        VALUES
        (
            %s,
            %s,
            %s
        )
        """

        cursor.execute(
            query,
            (
                user_id,
                title,
                full_text
            )
        )

        jd_id = (
            cursor.lastrowid
        )

        cursor.close()
        conn.close()

        return jd_id

    @staticmethod
    def get_jd_by_id(
        jd_id
    ):

        conn = Database.get_connection()

        cursor = conn.cursor(
            dictionary=True
        )

        query = """
        SELECT *
        FROM job_descriptions
        WHERE id = %s
        """

        cursor.execute(
            query,
            (jd_id,)
        )

        result = (
            cursor.fetchone()
        )

        cursor.close()
        conn.close()

        return result