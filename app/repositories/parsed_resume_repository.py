import json

from app.database.mysql_connection import Database


class ParsedResumeRepository:

    @staticmethod
    def save_parsed_resume(
        resume_id,
        full_text,
        parsed_data
    ):

        conn = Database.get_connection()

        cursor = conn.cursor()

        query = """
        INSERT INTO parsed_resumes
        (
            resume_id,
            full_text,
            parsed_json
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
                resume_id,
                full_text,
                json.dumps(parsed_data)
            )
        )

        parsed_resume_id = (
            cursor.lastrowid
        )

        cursor.close()
        conn.close()

        return parsed_resume_id

    @staticmethod
    def get_parsed_resume(
        resume_id
    ):

        conn = Database.get_connection()

        cursor = conn.cursor(
            dictionary=True,
            buffered=True
        )

        query = """
        SELECT *
        FROM parsed_resumes
        WHERE resume_id = %s
        """

        cursor.execute(
            query,
            (resume_id,)
        )

        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            result["parsed_json"] = json.loads(
                result["parsed_json"]
            )

        return result