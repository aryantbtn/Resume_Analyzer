import json

from app.database.mysql_connection import (
    Database
)


class ParsedJDRepository:

    @staticmethod
    def save_parsed_jd(
        jd_id,
        parsed_data
    ):

        conn = Database.get_connection()

        cursor = conn.cursor()

        query = """
        INSERT INTO
        parsed_job_descriptions
        (
            jd_id,
            parsed_json
        )
        VALUES
        (
            %s,
            %s
        )
        """

        cursor.execute(
            query,
            (
                jd_id,
                json.dumps(
                    parsed_data
                )
            )
        )

        parsed_jd_id = (
            cursor.lastrowid
        )

        cursor.close()
        conn.close()

        return parsed_jd_id


    @staticmethod
    def get_parsed_jd(
            jd_id
    ):
        conn = Database.get_connection()

        cursor = conn.cursor(
            dictionary=True,
            buffered=True
        )

        query = """
        SELECT *
        FROM parsed_job_descriptions
        WHERE jd_id = %s
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

        if result:
            result[
                "parsed_json"
            ] = json.loads(
                result[
                    "parsed_json"
                ]
            )

        return result